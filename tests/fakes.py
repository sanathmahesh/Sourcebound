"""A scripted stand-in for the Sail client, for tests that must not call a model."""

from sourcebound.llm.provider import LlmResult, ToolCall, Usage


def result(content=None, tool_calls=None, model="fake/model", input_tokens=1000, output_tokens=100) -> LlmResult:
    calls = [ToolCall(f"call_{n}", name, args) for n, (name, args) in enumerate(tool_calls or [])]
    return LlmResult(
        content=content,
        tool_calls=calls,
        finish_reason="tool_calls" if calls else "stop",
        usage=Usage(input_tokens, 0, output_tokens),
        model=model,
        seconds=0.5,
        attempts=1,
        raw={"fake": True, "content": content},
    )


class FakeChatClient:
    """Returns the scripted results in order and records every request."""

    def __init__(self, results: list[LlmResult]) -> None:
        self.results = list(results)
        self.requests: list[dict] = []

    def complete(self, **request) -> LlmResult:
        self.requests.append(request)
        if not self.results:
            raise AssertionError("FakeChatClient ran out of scripted results")
        return self.results.pop(0)
