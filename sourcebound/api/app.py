"""The live API, deployed as one Vercel Python function: POST /api/ask and GET /api/health.

Everything else on the site is static JSON. This app answers follow-up questions about one company with the
memo's retrieval and checks (sourcebound/api/ask.py).

Errors are plain sentences, never stack traces or provider detail:
- 400: the request is not {ticker, question} with a known ticker and a question of 1 to 500 characters;
- 429: the model provider is rate-limiting (the per-IP limit is a Vercel Firewall rule, set up in phase 10);
- 503: the provider failed, the answer could not be read, the 60-second limit passed, or no key is set.
The API key is read from the server environment at request time and never appears in a response or log.
"""

from __future__ import annotations

import asyncio
import os
from collections.abc import Callable
from functools import lru_cache, partial
from pathlib import Path

import yaml
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from sourcebound import contracts as c
from sourcebound.api.ask import AskError, AskSettings, answer_question, load_company
from sourcebound.llm.provider import LlmError, LlmSettings, SailClient
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.retrieval.index import INDEX_DIR

PUBLISHED_DIR = PROJECT_ROOT / "data" / "published"
PROVIDER_TIMEOUT_SECONDS = 45.0  # each model request; the whole answer has its own limit (models.yaml)


def ask_config() -> dict:
    config = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())
    return {"ask": config["ask"], "judge_effort": config["reasoning_effort"]["judge"],
            "judge_tokens": config["max_completion_tokens"]["judge"]}


def sail_client() -> SailClient:
    """The real client, built from server environment variables at request time."""
    return SailClient(LlmSettings.from_env(), timeout=PROVIDER_TIMEOUT_SECONDS, max_attempts=2)


def _error(status: int, message: str) -> JSONResponse:
    return JSONResponse(status_code=status, content={"detail": message})


def _validation_message(exc: RequestValidationError) -> str:
    first = exc.errors()[0] if exc.errors() else {}
    where = ".".join(str(p) for p in first.get("loc", []) if p != "body") or "body"
    if first.get("type") == "extra_forbidden":
        return f"Unexpected field '{where}'. Send only ticker and question."
    if first.get("type") == "missing":
        return f"Missing '{where}'. Send ticker and question."
    if where == "question":
        return "The question must be between 1 and 500 characters."
    return f"The request is not valid ({where}: {first.get('msg', 'invalid')})."


def create_app(client_factory: Callable[[], object] = sail_client, *, writer_model: str | None = None,
               judge_model: str | None = None, published_dir: Path = PUBLISHED_DIR, index_dir: Path = INDEX_DIR,
               timeout_seconds: float | None = None) -> FastAPI:
    """writer_model / judge_model default to SAIL_MODEL_WRITER / SAIL_MODEL_JUDGE, read at request time."""
    app = FastAPI(title="Sourcebound live API", docs_url=None, redoc_url=None, openapi_url=None)
    config = ask_config()
    limit = timeout_seconds if timeout_seconds is not None else float(config["ask"]["timeout_seconds"])

    @lru_cache(maxsize=1)
    def tickers() -> tuple[str, ...]:
        site = c.SiteIndex.model_validate_json((published_dir / "index.json").read_text())
        return tuple(entry.ticker for entry in site.companies)

    @lru_cache(maxsize=16)
    def company(ticker: str):
        return load_company(ticker, published_dir, index_dir)

    def settings() -> AskSettings:
        writer = writer_model or os.environ.get("SAIL_MODEL_WRITER", "").strip()
        judge = judge_model or os.environ.get("SAIL_MODEL_JUDGE", "").strip()
        if not writer or not judge:
            raise AskError(503, "The question service is not configured on this server.")
        ask = config["ask"]
        return AskSettings(writer, judge, ask["reasoning_effort"], config["judge_effort"],
                           int(ask["max_completion_tokens"]), int(config["judge_tokens"]),
                           int(ask["max_rounds"]), int(ask["max_claims"]))

    def run(request: c.AskRequest) -> c.AskResponse:
        try:
            client = client_factory()
        except ValueError:  # LlmSettings.from_env: a variable is missing
            raise AskError(503, "The question service is not configured on this server.") from None
        return answer_question(client, settings(), company(request.ticker), request.question)

    @app.exception_handler(RequestValidationError)
    async def bad_request(_: Request, exc: RequestValidationError) -> JSONResponse:
        return _error(400, _validation_message(exc))

    @app.get("/api/health")
    def health() -> dict:
        return {"status": "ok", "companies": len(tickers()),
                "configured": bool(os.environ.get("SAIL_API_KEY", "").strip())}

    @app.post("/api/ask", response_model=c.AskResponse)
    async def ask(request: c.AskRequest):
        if request.ticker not in tickers():
            return _error(400, f"Unknown ticker {request.ticker}. Choose one of: {', '.join(tickers())}.")
        loop = asyncio.get_running_loop()
        try:
            # The work runs in a thread; past the limit the caller gets a 503 and the thread is abandoned
            # (its model requests have their own 45-second timeout).
            return await asyncio.wait_for(loop.run_in_executor(None, partial(run, request)), timeout=limit)
        except TimeoutError:
            return _error(503, f"The answer took longer than {limit:g} seconds. Try a narrower question.")
        except AskError as exc:
            return _error(exc.status, exc.message)
        except LlmError as exc:
            if "HTTP 429" in str(exc):
                return _error(429, "The model service is busy. Try again in a few minutes.")
            return _error(503, "The model service is unavailable right now. Try again later.")

    return app


app = create_app()
