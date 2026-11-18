"""Layer (b), model part: the judge reads the rendered claim and its evidence and returns a verdict.

Evidence is the full text of each cited passage plus the engine values the claim's placeholders stand for
(so "leverage rose" can be checked against the numbers). Unreadable output gets one retry; after that the
claim is marked unsupported with a judge-error flag. GLM-5.3 is the provisional judge (phase 5 calibrates).
"""

from __future__ import annotations

from sourcebound.llm.prompts import JUDGE_SYSTEM
from sourcebound.llm.provider import LlmResult
from sourcebound.llm.schemas import JUDGE_FORMAT, JudgeVerdict, parse_json


def judge_message(claim: str, passages: list[tuple[str, str]], metrics: list[tuple[str, str]]) -> str:
    lines = [f"Claim: {claim}", "", "Evidence passages:"]
    lines += [f"[{cid}] {text}" for cid, text in passages] or ["(none)"]
    lines += ["", "Metric values and scorecard (computed by code from the company's XBRL data):"]
    lines += [f"- {label}: {value}" for label, value in metrics] or ["(none)"]
    return "\n".join(lines)


def run_judge(client, *, model: str, reasoning_effort: str, max_tokens: int, claim: str,
              passages: list[tuple[str, str]], metrics: list[tuple[str, str]]) -> tuple[JudgeVerdict | None, list[LlmResult]]:
    messages = [{"role": "system", "content": JUDGE_SYSTEM},
                {"role": "user", "content": judge_message(claim, passages, metrics)}]
    request = {"model": model, "response_format": JUDGE_FORMAT, "max_completion_tokens": max_tokens,
               "reasoning_effort": reasoning_effort}
    first = client.complete(messages=messages, **request)
    verdict, error = parse_json(first.content, JudgeVerdict)
    if verdict is not None:
        return verdict, [first]
    retry = client.complete(messages=messages + [
        {"role": "assistant", "content": first.content or ""},
        {"role": "user", "content": f"Your reply was {error}. Return only the JSON verdict."}], **request)
    verdict, _ = parse_json(retry.content, JudgeVerdict)
    return verdict, [first, retry]
