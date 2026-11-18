"""The one interface to the language models: Sail Research's OpenAI-compatible Chat Completions API.

Configured entirely by environment variables (SAIL_BASE_URL, SAIL_API_KEY, SAIL_MODEL_WRITER,
SAIL_MODEL_JUDGE, SAIL_SERVICE_TIER), so the model is a setting, not code. The API key is never printed,
logged or included in an error message.

Retries (Sail docs, re-read 17 November 2026): a 429 or a 503 "capacity unavailable" means the request never
started; other server errors and timeouts may have started work. Every call therefore carries an
Idempotency-Key, reused on every retry, so a retry returns the original result instead of paying twice.
The OpenAI SDK's own retries are switched off. Backoff: Retry-After if given, else 1, 2, 4 s plus jitter.
"""

from __future__ import annotations

import os
import random
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field

import httpx
import openai

RETRYABLE_STATUS = {409, 429, 500, 502, 503, 504}


class LlmError(RuntimeError):
    """A model call failed. The message never contains the API key."""


@dataclass(frozen=True)
class LlmSettings:
    base_url: str
    api_key: str = field(repr=False)
    writer_model: str
    judge_model: str
    service_tier: str

    @classmethod
    def from_env(cls) -> LlmSettings:
        names = ["SAIL_BASE_URL", "SAIL_API_KEY", "SAIL_MODEL_WRITER", "SAIL_MODEL_JUDGE", "SAIL_SERVICE_TIER"]
        values = {name: os.environ.get(name, "").strip() for name in names}
        missing = [name for name, value in values.items() if not value]
        if missing:
            raise ValueError(f"Set {', '.join(missing)} in .env (see .env.example)")
        return cls(values["SAIL_BASE_URL"], values["SAIL_API_KEY"], values["SAIL_MODEL_WRITER"],
                   values["SAIL_MODEL_JUDGE"], values["SAIL_SERVICE_TIER"])

    def __str__(self) -> str:
        return repr(self)


@dataclass(frozen=True)
class Usage:
    input_tokens: int
    cached_input_tokens: int
    output_tokens: int


@dataclass(frozen=True)
class ToolCall:
    id: str
    name: str
    arguments: str  # JSON text, as the model wrote it


@dataclass
class LlmResult:
    content: str | None
    tool_calls: list[ToolCall]
    finish_reason: str | None
    usage: Usage
    model: str
    seconds: float
    attempts: int
    raw: dict  # the full response, saved so results can be recomputed without new calls


class SailClient:
    def __init__(
        self,
        settings: LlmSettings,
        *,
        timeout: float = 240.0,
        max_attempts: int = 4,
        http_client: httpx.Client | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self.settings = settings
        self.max_attempts = max_attempts
        self._sleep = sleep
        self._openai = openai.OpenAI(
            base_url=settings.base_url,
            api_key=settings.api_key,
            max_retries=0,
            timeout=timeout,
            http_client=http_client,
        )

    def complete(
        self,
        *,
        model: str,
        messages: list[dict],
        max_completion_tokens: int,
        response_format: dict | None = None,
        tools: list[dict] | None = None,
        tool_choice: str | dict | None = None,
        reasoning_effort: str | None = None,
    ) -> LlmResult:
        """One chat completion, retried safely under a single idempotency key."""
        request = {"model": model, "messages": messages, "max_completion_tokens": max_completion_tokens}
        if response_format is not None:
            request["response_format"] = response_format
        if tools is not None:
            request["tools"] = tools
        if tool_choice is not None:
            request["tool_choice"] = tool_choice
        if reasoning_effort is not None:
            request["reasoning_effort"] = reasoning_effort
        key = str(uuid.uuid4())
        started = time.monotonic()
        problem = ""
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self._openai.chat.completions.create(
                    **request,
                    extra_headers={"Idempotency-Key": key},
                    extra_body={"service_tier": self.settings.service_tier},
                )
                return _result(response, time.monotonic() - started, attempt)
            except openai.APIStatusError as exc:
                problem = f"HTTP {exc.status_code}: {_error_message(exc)}"
                if exc.status_code not in RETRYABLE_STATUS:
                    raise LlmError(f"Sail request failed: {problem}") from None
                wait = _retry_after(exc.response)
            except (openai.APITimeoutError, openai.APIConnectionError) as exc:
                problem, wait = type(exc).__name__, None
            if attempt < self.max_attempts:
                self._sleep(wait if wait is not None else 2.0 ** (attempt - 1) + random.uniform(0, 0.5))
        raise LlmError(f"Sail request failed after {self.max_attempts} attempts: {problem}")

    def list_models(self) -> list[dict]:
        """GET /v1/models: the models this API key can use, as Sail returns them."""
        try:
            return [m.model_dump() for m in self._openai.models.list().data]
        except openai.APIError as exc:
            raise LlmError(f"Sail model list failed: {type(exc).__name__}") from None


def _result(response, seconds: float, attempts: int) -> LlmResult:
    choice = response.choices[0]
    usage = response.usage
    cached = 0
    if usage is not None and usage.prompt_tokens_details is not None:
        cached = usage.prompt_tokens_details.cached_tokens or 0
    tool_calls = [
        ToolCall(call.id, call.function.name, call.function.arguments)
        for call in (choice.message.tool_calls or [])
    ]
    return LlmResult(
        content=choice.message.content,
        tool_calls=tool_calls,
        finish_reason=choice.finish_reason,
        usage=Usage(usage.prompt_tokens if usage else 0, cached, usage.completion_tokens if usage else 0),
        model=response.model,
        seconds=seconds,
        attempts=attempts,
        raw=response.model_dump(),
    )


def _error_message(exc: openai.APIStatusError) -> str:
    body = exc.body if isinstance(exc.body, dict) else {}
    error = body.get("error", body) if isinstance(body, dict) else {}
    message = error.get("message") if isinstance(error, dict) else None
    code = error.get("code") if isinstance(error, dict) else None
    return " ".join(str(part) for part in (code, message) if part) or "no detail"


def _retry_after(response: httpx.Response) -> float | None:
    try:
        return max(0.0, float(response.headers.get("Retry-After", "")))
    except ValueError:
        return None
