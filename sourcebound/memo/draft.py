"""Draft one memo section with the writer model: one structured call, at most one repair.

The draft is checked by code before anything is published: placeholders must exist, every typed digit must
come from a cited passage, citations must point to passages shown and their quotes must be in them, and
qualitative claims must cite something. If anything fails, the model gets one chance to fix it, with the
problems listed. Whatever still fails is kept, marked, and put on the reviewer checklist.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from sourcebound.llm.prompts import WRITER_SYSTEM
from sourcebound.llm.provider import LlmResult
from sourcebound.llm.schemas import DRAFT_FORMAT, SectionDraft, parse_json
from sourcebound.memo.render import TableEntry
from sourcebound.memo.sections import SectionSpec
from sourcebound.retrieval.chunking import Chunk
from sourcebound.verify.numbers import check_claim_numbers
from sourcebound.verify.quotes import check_quote

MAX_CLAIMS = 6


@dataclass
class SectionContext:
    spec: SectionSpec
    company: str
    rows: list[TableEntry]  # the metric rows shown for this section
    table: dict[str, TableEntry]  # every placeholder the company has (for checking)
    periods: dict[str, str]
    passages: list[Chunk]
    trends: list[str] = field(default_factory=list)
    earlier_findings: list[str] = field(default_factory=list)  # rating rationale only
    judge_evidence: list[tuple[str, str]] = field(default_factory=list)  # shown to the judge for every claim

    def shown(self) -> dict[str, Chunk]:
        return {c.id: c for c in self.passages}


@dataclass
class DraftOutcome:
    draft: SectionDraft | None
    calls: list[LlmResult]
    repaired: bool
    problems: list[str]  # remaining after the repair attempt
    error: str = ""
    initial_problems: list[str] = field(default_factory=list)  # found in the first draft, before any repair


def writer_message(ctx: SectionContext) -> str:
    lines = [f"Company: {ctx.company}", f"Section: {ctx.spec.title}", f"Task: {ctx.spec.instructions}", ""]
    lines.append("Metric table. Write each figure only as its placeholder, exactly as shown (the value is for your "
                 "understanding only):")
    lines += [f"{{{{m:{row.key}}}}} = {row.display}   ({row.label})" for row in ctx.rows] or ["(none)"]
    lines += ["", "Period placeholders:"]
    lines += [f"{{{{p:{label}}}}} = {phrase}" for label, phrase in ctx.periods.items()]
    if ctx.trends:
        lines += ["", "Trends from FY-2 to LTM (computed by code):"] + [f"- {t}" for t in ctx.trends]
    if ctx.earlier_findings:
        lines += ["", "Findings from earlier sections, verified as supported:"] + [f"- {f}" for f in ctx.earlier_findings]
    lines += ["", "Passages (cite by chunk_id):"]
    for chunk in ctx.passages:
        lines += [f"[{chunk.id}] ({chunk.section}, {chunk.form} for the period ended {chunk.period_end})", chunk.text, ""]
    if not ctx.passages:
        lines.append("(none)")
    return "\n".join(lines)


def draft_problems(draft: SectionDraft, ctx: SectionContext) -> list[str]:
    shown = ctx.shown()
    problems = []
    if len(draft.claims) > MAX_CLAIMS:
        problems.append(f"{len(draft.claims)} claims; at most {MAX_CLAIMS}")
    for n, claim in enumerate(draft.claims, start=1):
        prefix = f"claim {n}"
        if not claim.text.strip():
            problems.append(f"{prefix}: empty text")
        cited = {c.chunk_id: shown[c.chunk_id].text for c in claim.citations if c.chunk_id in shown}
        problems += [f"{prefix}: {p}" for p in check_claim_numbers(claim.text, cited, ctx.table, ctx.periods)]
        for citation in claim.citations:
            status = check_quote(citation.quote, cited.get(citation.chunk_id))
            if status == "chunk_not_found":
                problems.append(f"{prefix}: cites {citation.chunk_id}, which is not one of the passages given")
            elif status != "ok":
                problems.append(f"{prefix}: {status.replace('_', ' ')} in {citation.chunk_id}: {citation.quote!r}")
        if claim.kind == "qualitative" and not claim.citations:
            problems.append(f"{prefix}: a qualitative claim must cite a passage")
    return problems


def draft_section(client, *, model: str, reasoning_effort: str, max_tokens: int, ctx: SectionContext) -> DraftOutcome:
    messages = [{"role": "system", "content": WRITER_SYSTEM}, {"role": "user", "content": writer_message(ctx)}]
    request = {"model": model, "response_format": DRAFT_FORMAT, "max_completion_tokens": max_tokens,
               "reasoning_effort": reasoning_effort}
    first = client.complete(messages=messages, **request)
    draft, error = parse_json(first.content, SectionDraft)
    problems = draft_problems(draft, ctx) if draft else []
    if draft is not None and not problems:
        return DraftOutcome(draft, [first], False, [])
    initial = list(problems)

    if draft is None:
        feedback = f"Your reply was {error}. Return the whole section as JSON in the required format."
    else:
        feedback = ("Your draft breaks these rules:\n" + "\n".join(f"- {p}" for p in problems)
                    + "\nReturn the whole corrected section as JSON in the required format.")
    repair_messages = messages + [{"role": "assistant", "content": first.content or ""},
                                  {"role": "user", "content": feedback}]
    second = client.complete(messages=repair_messages, **request)
    repaired, repair_error = parse_json(second.content, SectionDraft)
    if repaired is not None:
        return DraftOutcome(repaired, [first, second], True, draft_problems(repaired, ctx), "", initial)
    if draft is not None:
        return DraftOutcome(draft, [first, second], True, problems, f"repair reply was {repair_error}", initial)
    return DraftOutcome(None, [first, second], True, [], f"draft and repair were {error} / {repair_error}", initial)
