"""The Sail client: settings from the environment, idempotent retries, usage and cost. No network."""

import json

import httpx
import pytest

from sourcebound.llm.prices import call_cost, load_prices
from sourcebound.llm.provider import LlmError, LlmSettings, SailClient, Usage
from sourcebound.paths import CONFIG_DIR

KEY = "sk-test-not-a-real-key"


def settings() -> LlmSettings:
    return LlmSettings(base_url="https://api.example.invalid/v1", api_key=KEY, writer_model="w", judge_model="j",
                       service_tier="asap")


def completion(content="{}", prompt=100, cached=40, completion_tokens=20, tool_calls=None):
    message = {"role": "assistant", "content": content}
    if tool_calls:
        message["tool_calls"] = tool_calls
    return {
        "id": "chatcmpl-1", "object": "chat.completion", "created": 0, "model": "w",
        "choices": [{"index": 0, "message": message, "finish_reason": "tool_calls" if tool_calls else "stop"}],
        "usage": {"prompt_tokens": prompt, "completion_tokens": completion_tokens, "total_tokens": prompt + completion_tokens,
                  "prompt_tokens_details": {"cached_tokens": cached}},
    }


def client_with(handler, **kwargs) -> SailClient:
    http = httpx.Client(transport=httpx.MockTransport(handler))
    return SailClient(settings(), http_client=http, sleep=lambda s: None, **kwargs)


def test_settings_from_env_refuse_without_key(monkeypatch):
    for name in ["SAIL_BASE_URL", "SAIL_MODEL_WRITER", "SAIL_MODEL_JUDGE", "SAIL_SERVICE_TIER"]:
        monkeypatch.setenv(name, "x")
    monkeypatch.delenv("SAIL_API_KEY", raising=False)
    with pytest.raises(ValueError, match="SAIL_API_KEY"):
        LlmSettings.from_env()


def test_settings_never_show_the_key():
    assert KEY not in repr(settings()) and KEY not in str(settings())


def test_request_carries_model_tier_limit_and_idempotency_key():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=completion('{"a": 1}'))

    result = client_with(handler).complete(model="w", messages=[{"role": "user", "content": "hi"}],
                                           max_completion_tokens=50, reasoning_effort="low")
    body = json.loads(seen[0].content)
    assert body["model"] == "w" and body["service_tier"] == "asap" and body["max_completion_tokens"] == 50
    assert body["reasoning_effort"] == "low" and "max_tokens" not in body
    assert seen[0].headers["Idempotency-Key"]
    assert result.content == '{"a": 1}'
    assert result.usage == Usage(input_tokens=100, cached_input_tokens=40, output_tokens=20)


def test_retries_reuse_the_same_idempotency_key():
    seen, replies = [], [httpx.Response(503, json={"error": {"code": "service_overloaded"}}),
                         httpx.Response(429, headers={"Retry-After": "1"}, json={"error": {}}),
                         httpx.Response(200, json=completion())]

    def handler(request):
        seen.append(request.headers["Idempotency-Key"])
        return replies.pop(0)

    client_with(handler).complete(model="w", messages=[{"role": "user", "content": "hi"}], max_completion_tokens=10)
    assert len(seen) == 3 and len(set(seen)) == 1


def test_bad_request_is_not_retried_and_never_leaks_the_key():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(400, json={"error": {"message": "unsupported parameter"}})

    with pytest.raises(LlmError) as raised:
        client_with(handler).complete(model="w", messages=[{"role": "user", "content": "hi"}], max_completion_tokens=10)
    assert len(calls) == 1
    assert "400" in str(raised.value) and KEY not in str(raised.value)


def test_gives_up_after_max_attempts():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(503, json={"error": {}})

    with pytest.raises(LlmError):
        client_with(handler, max_attempts=3).complete(model="w", messages=[], max_completion_tokens=10)
    assert len(calls) == 3


def test_tool_calls_are_parsed():
    tool_calls = [{"id": "call_1", "type": "function", "function": {"name": "get_metric", "arguments": '{"metric_id": "x"}'}}]
    result = client_with(lambda r: httpx.Response(200, json=completion(None, tool_calls=tool_calls))).complete(
        model="w", messages=[], max_completion_tokens=10)
    assert [(t.name, t.arguments) for t in result.tool_calls] == [("get_metric", '{"metric_id": "x"}')]
    assert result.finish_reason == "tool_calls"


def test_cost_uses_list_prices_and_separates_cached_input():
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    usage = Usage(input_tokens=1_000_000, cached_input_tokens=400_000, output_tokens=100_000)
    # GLM-5.3: 600k x 0.98 + 400k x 0.18 + 100k x 3.08, per million
    assert call_cost(prices, "zai-org/GLM-5.3", usage) == pytest.approx(0.588 + 0.072 + 0.308)
    with pytest.raises(KeyError):
        call_cost(prices, "unknown/model", usage)
