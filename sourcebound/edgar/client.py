"""A small, polite HTTP client for SEC EDGAR.

SEC fair-access rules (re-read 17 November 2026 at
https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data): at most 10 requests per
second, and a User-Agent that names the requester and gives contact details. This client:

- refuses to run without a User-Agent containing an email address (read from EDGAR_USER_AGENT);
- sends one request at a time, at most 5 per second (min_interval = 0.2 s between request starts);
- retries 429 and 5xx responses up to max_attempts, waiting Retry-After if given, else 1, 2, 4 s + jitter;
- caches every successful response on disk, mirroring the URL, so a repeat is never re-downloaded.

The cache never expires: delete data/raw/ to force a fresh download.
"""

from __future__ import annotations

import json
import os
import random
import time
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import httpx

from sourcebound.paths import RAW_CACHE_DIR

RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class EdgarError(RuntimeError):
    """EDGAR returned something we cannot use. The pipeline stops rather than guessing."""


class EdgarClient:
    """Fetches JSON from EDGAR with a declared User-Agent, a throttle, retries and a disk cache."""

    def __init__(
        self,
        user_agent: str,
        cache_dir: Path = RAW_CACHE_DIR,
        *,
        min_interval: float = 0.2,
        max_attempts: int = 4,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.monotonic,
        jitter: Callable[[], float] = lambda: random.uniform(0.0, 0.5),
    ) -> None:
        user_agent = (user_agent or "").strip()
        if not user_agent or "@" not in user_agent:
            raise ValueError(
                "EDGAR_USER_AGENT must name you and give a contact email, e.g. 'Jane Doe jane@example.com'. "
                "SEC fair-access rules require it."
            )
        self.user_agent = user_agent
        self.cache_dir = Path(cache_dir)
        self.min_interval = min_interval
        self.max_attempts = max_attempts
        self._sleep = sleep
        self._clock = clock
        self._jitter = jitter
        self._last_request_at: float | None = None
        self._http = httpx.Client(
            headers={"User-Agent": user_agent},
            timeout=timeout,
            transport=transport,
            follow_redirects=True,
        )

    @classmethod
    def from_env(cls, cache_dir: Path = RAW_CACHE_DIR, **kwargs) -> EdgarClient:
        """Build a client from the EDGAR_USER_AGENT environment variable; refuse if it is unset."""
        user_agent = os.environ.get("EDGAR_USER_AGENT", "")
        if not user_agent.strip():
            raise ValueError("EDGAR_USER_AGENT is not set. Add it to .env (see .env.example).")
        return cls(user_agent, cache_dir, **kwargs)

    # ----- cache -------------------------------------------------------------------------------

    def cache_path(self, url: str) -> Path:
        """Where a URL's response is cached: cache_dir/<host>/<path>, plus the query if any."""
        parts = urlsplit(url)
        relative = parts.path.lstrip("/")
        if parts.query:
            relative += "__" + parts.query.replace("/", "_").replace("&", "_")
        return self.cache_dir / parts.netloc / relative

    def _meta_path(self, url: str) -> Path:
        path = self.cache_path(url)
        return path.with_name(path.name + ".meta.json")

    def fetched_at(self, url: str) -> str | None:
        """UTC time the cached copy of this URL was downloaded, or None if not cached."""
        meta = self._meta_path(url)
        if not meta.exists():
            return None
        return json.loads(meta.read_text())["fetched_at"]

    # ----- fetching ----------------------------------------------------------------------------

    def get_json(self, url: str) -> dict:
        """Return the JSON at url, from the cache if we have it, otherwise from EDGAR."""
        path = self.cache_path(url)
        if path.exists():
            return json.loads(path.read_bytes())
        body = self._download(url)
        try:
            data = json.loads(body)
        except json.JSONDecodeError as exc:
            raise EdgarError(f"EDGAR returned something that is not JSON for {url}") from exc
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
        meta = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        self._meta_path(url).write_text(json.dumps(meta))
        return data

    def _download(self, url: str) -> bytes:
        """GET url with throttle and retries. Raises EdgarError on a final failure."""
        last_problem = ""
        for attempt in range(1, self.max_attempts + 1):
            self._wait_for_turn()
            try:
                response = self._http.get(url)
            except httpx.TransportError as exc:
                last_problem = f"network error {type(exc).__name__}"
                wait = None
            else:
                if response.status_code == 200:
                    return response.content
                if response.status_code not in RETRYABLE_STATUS:
                    raise EdgarError(f"EDGAR returned HTTP {response.status_code} for {url}")
                last_problem = f"HTTP {response.status_code}"
                wait = _retry_after_seconds(response)
            if attempt < self.max_attempts:
                if wait is None:
                    wait = 2.0 ** (attempt - 1) + self._jitter()  # 1, 2, 4 s plus jitter
                self._sleep(wait)
        raise EdgarError(f"EDGAR request failed after {self.max_attempts} attempts ({last_problem}) for {url}")

    def _wait_for_turn(self) -> None:
        """Sleep until at least min_interval has passed since the previous request started."""
        now = self._clock()
        if self._last_request_at is not None:
            remaining = self.min_interval - (now - self._last_request_at)
            if remaining > 0:
                self._sleep(remaining)
                now = self._clock()
        self._last_request_at = now


def _retry_after_seconds(response: httpx.Response) -> float | None:
    """The Retry-After header in seconds, if present and numeric."""
    value = response.headers.get("Retry-After", "").strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        return None
