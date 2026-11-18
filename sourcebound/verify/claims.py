"""Verify one drafted claim: deterministic checks first, the judge only if they pass.

1. Numbers: render placeholders; every typed digit must come from a cited passage (verify/numbers.py).
2. Citations: each cited passage must be one the writer was shown, and its quote must be in it.
3. A qualitative claim must cite something.
Any failure gives verdict "unsupported" with the reason, and no model call. Otherwise the judge decides.
"""

from __future__ import annotations

from sourcebound.contracts import MemoCitation, MemoClaim
from sourcebound.llm.provider import LlmResult
from sourcebound.llm.schemas import DraftClaim
from sourcebound.memo.render import render_claim
from sourcebound.verify.judge import run_judge
from sourcebound.verify.quotes import check_quote

QUOTE_REASONS = {"chunk_not_found": "cited passage not found", "quote_too_short": "quote too short",
                 "quote_not_found": "quote not found"}


def verify_claim(claim_id: str, claim: DraftClaim, ctx, client, *, model: str, reasoning_effort: str,
                 max_tokens: int, flags: list[str] | None = None) -> tuple[MemoClaim, list[LlmResult]]:
    shown = ctx.shown()
    cited = {c.chunk_id: shown[c.chunk_id].text for c in claim.citations if c.chunk_id in shown}
    rendered = render_claim(claim.text, cited, ctx.table, ctx.periods)
    citations = [MemoCitation(chunk_id=c.chunk_id, quote=c.quote, check=check_quote(c.quote, cited.get(c.chunk_id)))
                 for c in claim.citations]
    flags = list(flags or [])

    def decided(verdict: str, reason: str, checked_by: str, evidence: str = "") -> MemoClaim:
        return MemoClaim(id=claim_id, kind=claim.kind, verdict=verdict, judge_reason=reason, evidence_quote=evidence,
                         checked_by=checked_by, segments=rendered.segments, citations=citations, flags=flags)

    if rendered.problems:
        return decided("unsupported", "unsupported: number check failed: " + "; ".join(rendered.problems),
                       "deterministic"), []
    failed = [c for c in citations if c.check != "ok"]
    if failed:
        reasons = sorted({QUOTE_REASONS[c.check] for c in failed})
        return decided("unsupported", "unsupported: " + "; ".join(reasons), "deterministic"), []
    if claim.kind == "qualitative" and not citations:
        return decided("unsupported", "unsupported: qualitative claim without a citation", "deterministic"), []

    metrics = [(_with_period(ctx.table[k].label, k, ctx.periods), ctx.table[k].display)
               for k in dict.fromkeys(rendered.metric_keys)] + list(ctx.judge_evidence)
    verdict, calls = run_judge(client, model=model, reasoning_effort=reasoning_effort, max_tokens=max_tokens,
                               claim=rendered.text, passages=list(cited.items()), metrics=metrics)
    if verdict is None:
        flags.append("judge_error: unreadable output twice")
        return decided("unsupported", "judge output unreadable", "judge"), calls
    return decided(verdict.verdict, verdict.reason, "judge", verdict.evidence_quote), calls


def _with_period(label: str, key: str, periods: dict[str, str]) -> str:
    """'Revenue, FY-2' -> 'Revenue, FY-2 (the fiscal year ended 31 January 2024)', so dates can be checked."""
    phrase = periods.get(key.rsplit(":", 1)[-1])
    return f"{label} ({phrase})" if phrase else label
