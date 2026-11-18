"""Tests for the EDGAR client: User-Agent, throttle, retries and cache.

No network: every test uses httpx.MockTransport, a fake clock and a fake sleep.
"""

import json
from pathlib import Path

import httpx
import pytest

from sourcebound.edgar.client import EdgarClient, EdgarError

UA = "Test Person test@example.com"
URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000000001.json"
URL2 = "https://data.sec.gov/submissions/CIK0000000001.json"


class FakeClock:
    """A clock that only moves when the code under test sleeps."""

    def __init__(self) -> None:
        self.now = 1000.0
        self.sleeps: list[float] = []

    def time(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def make_client(tmp_path: Path, handler, clock: FakeClock, **kwargs) -> EdgarClient:
    return EdgarClient(
        user_agent=UA,
        cache_dir=tmp_path,
        transport=httpx.MockTransport(handler),
        sleep=clock.sleep,
        clock=clock.time,
        jitter=lambda: 0.0,
        **kwargs,
    )


def ok_handler(calls: list):
    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json={"url": str(request.url)})

    return handler


def test_sends_declared_user_agent(tmp_path):
    calls: list[httpx.Request] = []
    client = make_client(tmp_path, ok_handler(calls), FakeClock())
    client.get_json(URL)
    assert calls[0].headers["User-Agent"] == UA


@pytest.mark.parametrize("bad", ["", "   ", "Just A Name"])
def test_refuses_without_valid_user_agent(tmp_path, bad):
    with pytest.raises(ValueError):
        EdgarClient(user_agent=bad, cache_dir=tmp_path)


def test_from_env_refuses_when_unset(tmp_path, monkeypatch):
    monkeypatch.delenv("EDGAR_USER_AGENT", raising=False)
    with pytest.raises(ValueError, match="EDGAR_USER_AGENT"):
        EdgarClient.from_env(cache_dir=tmp_path)


def test_from_env_reads_variable(tmp_path, monkeypatch):
    monkeypatch.setenv("EDGAR_USER_AGENT", UA)
    client = EdgarClient.from_env(cache_dir=tmp_path)
    assert client.user_agent == UA


def test_throttle_spaces_requests(tmp_path):
    clock = FakeClock()
    request_times: list[float] = []

    def handler(request):
        request_times.append(clock.time())
        return httpx.Response(200, json={})

    client = make_client(tmp_path, handler, clock, min_interval=0.2)
    client.get_json(URL)
    client.get_json(URL2)
    client.get_json(URL2 + "?x=1")
    gaps = [b - a for a, b in zip(request_times, request_times[1:])]
    assert all(gap >= 0.2 - 1e-9 for gap in gaps)


def test_default_rate_is_at_most_five_per_second(tmp_path):
    client = EdgarClient(user_agent=UA, cache_dir=tmp_path)
    assert client.min_interval >= 0.2


def test_retries_on_429_honouring_retry_after(tmp_path):
    clock = FakeClock()
    responses = [httpx.Response(429, headers={"Retry-After": "3"}), httpx.Response(200, json={"a": 1})]
    calls = []

    def handler(request):
        calls.append(request)
        return responses.pop(0)

    client = make_client(tmp_path, handler, clock)
    assert client.get_json(URL) == {"a": 1}
    assert len(calls) == 2
    assert 3.0 in clock.sleeps


def test_retries_with_exponential_backoff_without_retry_after(tmp_path):
    clock = FakeClock()
    responses = [httpx.Response(503), httpx.Response(429), httpx.Response(200, json={})]

    def handler(request):
        return responses.pop(0)

    client = make_client(tmp_path, handler, clock)
    client.get_json(URL)
    backoffs = [s for s in clock.sleeps if s >= 1.0]
    assert backoffs == [1.0, 2.0]


def test_gives_up_after_max_attempts(tmp_path):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(429)

    client = make_client(tmp_path, handler, FakeClock(), max_attempts=3)
    with pytest.raises(EdgarError, match="429"):
        client.get_json(URL)
    assert len(calls) == 3


def test_does_not_retry_or_cache_client_errors(tmp_path):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(404)

    client = make_client(tmp_path, handler, FakeClock())
    with pytest.raises(EdgarError, match="404"):
        client.get_json(URL)
    assert len(calls) == 1
    assert not client.cache_path(URL).exists()


def test_serves_repeats_from_cache(tmp_path):
    calls = []
    clock = FakeClock()
    client = make_client(tmp_path, ok_handler(calls), clock)
    first = client.get_json(URL)
    second = client.get_json(URL)
    assert first == second
    assert len(calls) == 1

    # A new client over the same cache directory also makes no request.
    other = make_client(tmp_path, ok_handler(calls), clock)
    assert other.get_json(URL) == first
    assert len(calls) == 1


def test_cache_path_mirrors_url_and_records_fetch_time(tmp_path):
    client = make_client(tmp_path, ok_handler([]), FakeClock())
    client.get_json(URL)
    path = client.cache_path(URL)
    assert path == tmp_path / "data.sec.gov/api/xbrl/companyfacts/CIK0000000001.json"
    meta = json.loads(path.with_name(path.name + ".meta.json").read_text())
    assert meta["url"] == URL
    assert client.fetched_at(URL) == meta["fetched_at"]


def test_user_agent_never_written_to_cache(tmp_path):
    client = make_client(tmp_path, ok_handler([]), FakeClock())
    client.get_json(URL)
    for path in tmp_path.rglob("*"):
        if path.is_file():
            assert "test@example.com" not in path.read_text()


DOC_URL = "https://www.sec.gov/Archives/edgar/data/1/000000000026000001/doc.htm"


def test_get_text_caches_html_and_decodes(tmp_path):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, content="<p>Café debt</p>".encode("utf-8"))

    client = make_client(tmp_path, handler, FakeClock())
    assert client.get_text(DOC_URL) == "<p>Café debt</p>"
    assert client.get_text(DOC_URL) == "<p>Café debt</p>"
    assert len(calls) == 1
    assert client.cache_path(DOC_URL).exists()


def test_get_text_falls_back_to_latin1(tmp_path):
    client = make_client(tmp_path, lambda r: httpx.Response(200, content="na\xefve".encode("latin-1")), FakeClock())
    assert client.get_text(DOC_URL) == "naïve"


def test_refresh_downloads_again_and_replaces_the_cache(tmp_path):
    calls = []
    replies = [{"v": 1}, {"v": 2}]

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json=replies.pop(0))

    client = make_client(tmp_path, handler, FakeClock())
    assert client.get_json(URL) == {"v": 1}
    assert client.get_json(URL) == {"v": 1}  # cached
    assert client.get_json(URL, refresh=True) == {"v": 2}
    assert client.get_json(URL) == {"v": 2}  # the refreshed copy is now the cache
    assert len(calls) == 2
