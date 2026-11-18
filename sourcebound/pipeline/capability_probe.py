"""Capability probe (PLAN.md phase 4): what each writer model actually supports on Sail.

Run:  uv run python -m sourcebound.pipeline.capability_probe

For each model in config/models.yaml it checks, with tiny requests:
1. structured output: response_format json_schema (strict) returns JSON matching the schema exactly;
2. a strict function tool call: the model calls get_metric with exactly the declared arguments;
3. both in one setup: with tools and a response schema in the same request, the model calls the tool,
   receives the result, then answers in the schema (what the follow-up endpoint needs);
4. the same task with tools and the schema in separate requests (tools-only turn, then schema-only turn).
It also records what GET /v1/models returns for each model, and each call's tokens, cost and time.
Writes docs/sail-capability-probe.md and saves raw responses under data/runs/. A failure means stop and ask.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone

import yaml
from dotenv import load_dotenv

from sourcebound.llm.prices import call_cost, load_prices
from sourcebound.llm.provider import LlmResult, LlmSettings, SailClient
from sourcebound.paths import CONFIG_DIR, ENV_FILE, PROJECT_ROOT

SCHEMA = {
    "type": "object",
    "properties": {"answer": {"type": "string"}, "number": {"type": "integer"}},
    "required": ["answer", "number"],
    "additionalProperties": False,
}
RESPONSE_FORMAT = {"type": "json_schema", "json_schema": {"name": "probe_answer", "strict": True, "schema": SCHEMA}}
TOOL = {
    "type": "function",
    "function": {
        "name": "get_metric",
        "description": "Look up a computed credit metric for the company being analysed.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {"metric_id": {"type": "string"}, "period": {"type": "string", "enum": ["FY0", "LTM"]}},
            "required": ["metric_id", "period"],
            "additionalProperties": False,
        },
    },
}
MAX_TOKENS = 2000


@dataclass
class Check:
    name: str
    passed: bool
    detail: str
    calls: list[LlmResult] = field(default_factory=list)


def _json(content: str | None) -> tuple[dict | None, str]:
    try:
        value = json.loads(content or "")
    except json.JSONDecodeError:
        return None, f"not valid JSON: {(content or '')[:80]!r}"
    return (value, "") if isinstance(value, dict) else (None, "JSON is not an object")


def _matches_schema(value: dict, answer: str, number: int) -> str:
    """Empty string if value is exactly {answer, number} with the expected values, else what is wrong."""
    if set(value) != {"answer", "number"}:
        return f"keys {sorted(value)} instead of ['answer', 'number']"
    if not isinstance(value["number"], int) or value["number"] != number:
        return f"number {value['number']!r}, expected {number}"
    if str(value["answer"]).strip().lower() != answer:
        return f"answer {value['answer']!r}, expected {answer!r}"
    return ""


def _good_tool_call(result: LlmResult) -> str:
    if len(result.tool_calls) != 1 or result.tool_calls[0].name != "get_metric":
        return f"expected one get_metric call, got {[c.name for c in result.tool_calls]} (content {str(result.content)[:60]!r})"
    args, problem = _json(result.tool_calls[0].arguments)
    if args is None:
        return f"arguments {problem}"
    if set(args) != {"metric_id", "period"} or args.get("metric_id") != "net_leverage" or args.get("period") != "LTM":
        return f"arguments {args}"
    return ""


def probe_model(client, model: str, reasoning_effort: str) -> list[Check]:
    common = {"model": model, "max_completion_tokens": MAX_TOKENS, "reasoning_effort": reasoning_effort}
    checks = []

    first = client.complete(
        messages=[{"role": "user", "content": "Reply with answer set to the word 'ready' and number set to 7."}],
        response_format=RESPONSE_FORMAT, **common)
    value, problem = _json(first.content)
    problem = problem or _matches_schema(value, "ready", 7)
    checks.append(Check("structured output (json_schema, strict)", not problem, problem or "ok", [first]))

    second = client.complete(
        messages=[{"role": "user", "content": "Use the get_metric tool to look up net_leverage for the LTM period."}],
        tools=[TOOL], tool_choice={"type": "function", "function": {"name": "get_metric"}}, **common)
    problem = _good_tool_call(second)
    checks.append(Check("strict function tool call", not problem, problem or "ok", [second]))

    messages = [
        {"role": "system", "content": "You answer questions about credit metrics. Call get_metric to obtain "
                                      "values; never guess them. Then answer in the required JSON format."},
        {"role": "user", "content": "What is net_leverage for LTM? Put the value you receive in `number` and "
                                    "the word 'done' in `answer`."},
    ]
    turn_one = client.complete(messages=messages, tools=[TOOL], tool_choice="auto",
                               response_format=RESPONSE_FORMAT, **common)
    problem = _good_tool_call(turn_one)
    calls = [turn_one]
    if not problem:
        call = turn_one.tool_calls[0]
        messages += [
            {"role": "assistant", "content": turn_one.content,
             "tool_calls": [{"id": call.id, "type": "function",
                             "function": {"name": call.name, "arguments": call.arguments}}]},
            {"role": "tool", "tool_call_id": call.id, "content": json.dumps({"metric_id": "net_leverage", "value": 3})},
        ]
        turn_two = client.complete(messages=messages, tools=[TOOL], tool_choice="auto",
                                   response_format=RESPONSE_FORMAT, **common)
        calls.append(turn_two)
        value, problem = _json(turn_two.content)
        problem = problem or _matches_schema(value, "done", 3)
    else:
        problem = f"turn 1 did not call the tool: {problem}"
    checks.append(Check("tool call then structured answer, in one request setup", not problem, problem or "ok", calls))

    # The same task with tools and the answer format kept in separate requests.
    messages = messages[:2]
    tool_turn = client.complete(messages=messages, tools=[TOOL], tool_choice="auto", **common)
    problem = _good_tool_call(tool_turn)
    calls = [tool_turn]
    if not problem:
        call = tool_turn.tool_calls[0]
        messages = messages + [
            {"role": "assistant", "content": tool_turn.content,
             "tool_calls": [{"id": call.id, "type": "function",
                             "function": {"name": call.name, "arguments": call.arguments}}]},
            {"role": "tool", "tool_call_id": call.id, "content": json.dumps({"metric_id": "net_leverage", "value": 3})},
        ]
        answer_turn = client.complete(messages=messages, response_format=RESPONSE_FORMAT, **common)
        calls.append(answer_turn)
        value, problem = _json(answer_turn.content)
        problem = problem or _matches_schema(value, "done", 3)
    else:
        problem = f"tool turn did not call the tool: {problem}"
    checks.append(Check("tool call, then structured answer in a separate request", not problem, problem or "ok", calls))
    return checks


def render(results: dict[str, list[Check]], model_list: dict[str, dict | None], settings: LlmSettings,
           prices: dict, effort: str, when: str) -> str:
    lines = [
        "# Sail capability probe",
        "",
        f"Run {when} against {settings.base_url}, service tier `{settings.service_tier}`, reasoning effort "
        f"`{effort}` (the writer setting), max_completion_tokens {MAX_TOKENS}. Command: "
        "`uv run python -m sourcebound.pipeline.capability_probe`. Raw responses: data/runs/.",
        "",
        "| Model | Check | Result | Detail | Calls | Input / cached / output tokens | Cost (US$) | Seconds |",
        "|---|---|---|---|---|---|---|---|",
    ]
    total = 0.0
    for model, checks in results.items():
        for check in checks:
            tokens = [(c.usage.input_tokens, c.usage.cached_input_tokens, c.usage.output_tokens) for c in check.calls]
            cost = sum(call_cost(prices, model, c.usage) for c in check.calls)
            total += cost
            seconds = sum(c.seconds for c in check.calls)
            token_text = " + ".join(f"{i} / {ca} / {o}" for i, ca, o in tokens)
            lines.append(f"| {model} | {check.name} | {'pass' if check.passed else '**FAIL**'} | {check.detail} | "
                         f"{len(check.calls)} | {token_text} | {cost:.5f} | {seconds:.1f} |")
    lines += ["", f"Total probe cost at list price: US${total:.4f}.", "", "## GET /v1/models, as returned", ""]
    for model, entry in model_list.items():
        lines.append(f"- `{model}`: " + (f"`{json.dumps(entry, sort_keys=True)}`" if entry else "**not listed**"))
    lines += ["", "Context windows and output limits: " + (
        "not reported by GET /v1/models (fields listed above); the models page "
        "(https://docs.sailresearch.com/models.md, read 17 November 2026) lists a 1M-token context for all three."
    )]
    return "\n".join(lines) + "\n"


def main() -> None:
    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    client = SailClient(settings)
    config = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    effort = config["reasoning_effort"]["writer"]
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    listed = {m["id"]: m for m in client.list_models()}
    results, raw = {}, {}
    for model in config["writers"]:
        print(f"probing {model} ...", flush=True)
        results[model] = probe_model(client, model, effort)
        raw[model] = [{"check": c.name, "passed": c.passed, "detail": c.detail, "responses": [r.raw for r in c.calls]}
                      for c in results[model]]
        for check in results[model]:
            print(f"   {'pass' if check.passed else 'FAIL'}  {check.name}: {check.detail}")
    out = PROJECT_ROOT / "docs" / "sail-capability-probe.md"
    out.write_text(render(results, {m: listed.get(m) for m in config["writers"]}, settings, prices, effort, when))
    runs = PROJECT_ROOT / "data" / "runs"
    runs.mkdir(parents=True, exist_ok=True)
    (runs / f"capability-probe-{when[:10]}.json").write_text(json.dumps(raw, indent=1, default=str))
    print(f"written {out.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
