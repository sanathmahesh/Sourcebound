"""Answer one follow-up question about one company: a bounded lookup loop, then a checked, structured answer.

Steps (PLAN.md 4.13 and decision D34):
1. Up to three rounds in which the model may call two read-only tools: get_metric (a value from the company's
   published metrics.json) and search_filing (BM25 over the company's own filing passages). These requests
   carry tools and no response format.
2. One request with the answer schema and no tools: status (ok | out_of_scope) and claims in the memo's shape.
   The capability probe showed that two of the three models invent numbers when tools and a schema share a
   request, so the two are always kept apart, even when the model stops looking things up early.
3. Every claim goes through the memo's checks: number trace, quote check, then the judge. Only claims the judge
   marks supported are kept; the rest are listed in "removed" with the reason. A live answer is not reviewed
   by a person before it is shown, so the bar is higher than in the memo, where partly supported claims are
   shown with a marker and put on the reviewer checklist.

The tools can only read the company named in the request: the ticker is fixed by the caller, not the model.
This module imports neither pandas nor the EDGAR client (the live function loads it).
"""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

from sourcebound import contracts as c
from sourcebound.llm.prompts import ASK_FINAL, ASK_SYSTEM
from sourcebound.llm.schemas import ASK_FORMAT, AskAnswer, parse_json
from sourcebound.memo.metric_table import build_table, scorecard_context
from sourcebound.memo.render import TableEntry, passage_from_chunk, period_phrases
from sourcebound.retrieval.chunking import Chunk
from sourcebound.retrieval.index import CompanyIndex, load_index, search
from sourcebound.verify.claims import verify_claim

SEARCH_SECTIONS = ["any", "business", "risk_factors", "mdna", "liquidity", "market_risk", "debt_note",
                   "financial_statements", "other_item"]
PASSAGES_PER_SEARCH = 5
CALLS_PER_ROUND = 3

TOOLS = [
    {"type": "function", "function": {
        "name": "get_metric",
        "description": "A figure computed by code from the company's XBRL data, with the placeholder to write it as.",
        "parameters": {
            "type": "object",
            "properties": {
                "metric_id": {"type": "string", "description": "a metric id from the list given, e.g. net_leverage"},
                "period": {"type": "string", "description": "FY-2, FY-1, FY0, LTM, or latest for scorecard items"},
            },
            "required": ["metric_id", "period"],
            "additionalProperties": False,
        }}},
    {"type": "function", "function": {
        "name": "search_filing",
        "description": "Search the company's own recent 10-K and 10-Q text. Returns up to 5 passages.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "a few keywords, e.g. revolving credit facility"},
                "section": {"type": "string", "enum": SEARCH_SECTIONS},
            },
            "required": ["query", "section"],
            "additionalProperties": False,
        }}},
]


class AskError(Exception):
    """A failure the API reports with an HTTP status and a plain message."""

    def __init__(self, status: int, message: str) -> None:
        super().__init__(message)
        self.status, self.message = status, message


@dataclass(frozen=True)
class AskSettings:
    writer_model: str
    judge_model: str
    reasoning_effort: str
    judge_reasoning_effort: str
    max_completion_tokens: int
    judge_max_completion_tokens: int
    max_rounds: int
    max_claims: int


@dataclass
class CompanyData:
    """One company's published metrics and search index, loaded once per warm function instance."""

    metrics: c.CompanyMetrics
    index: CompanyIndex
    table: dict[str, TableEntry]
    all_metrics: dict[str, c.Metric]
    periods: dict[str, str]
    judge_evidence: list[tuple[str, str]]


def load_company(ticker: str, published_dir: Path, index_dir: Path) -> CompanyData:
    cm = c.CompanyMetrics.model_validate_json((published_dir / "companies" / ticker / "metrics.json").read_text())
    table, all_metrics = build_table(cm)
    _, evidence = scorecard_context(cm)
    return CompanyData(cm, load_index(ticker, index_dir), table, all_metrics, period_phrases(cm.periods), evidence)


@dataclass
class AskContext:
    """What verify_claim needs: the passages the model saw, the placeholder table and the period phrases."""

    table: dict[str, TableEntry]
    periods: dict[str, str]
    judge_evidence: list[tuple[str, str]]
    seen: dict[str, Chunk] = field(default_factory=dict)

    def shown(self) -> dict[str, Chunk]:
        return self.seen


def opening_message(data: CompanyData, question: str) -> str:
    ids: dict[str, list[str]] = {}
    for key in data.table:
        metric_id, period = key.rsplit(":", 1)
        ids.setdefault(metric_id, []).append(period)
    lines = [f"Company: {data.metrics.name} ({data.metrics.ticker})", f"Question: {question}", "",
             "Metrics available from get_metric (id: periods):"]
    lines += [f"- {mid}: {', '.join(periods)}  ({data.all_metrics[f'{mid}:{periods[0]}'].label})"
              for mid, periods in ids.items()]
    lines += ["", "Period placeholders:"] + [f"{{{{p:{label}}}}} = {phrase}" for label, phrase in data.periods.items()]
    return "\n".join(lines)


def get_metric(data: CompanyData, metric_id: str, period: str) -> tuple[dict, str]:
    """(tool output, one-line summary)."""
    key = f"{metric_id}:{period}"
    if key not in data.table:
        periods = [k.rsplit(":", 1)[1] for k in data.table if k.rsplit(":", 1)[0] == metric_id]
        hint = f"; periods available: {', '.join(periods)}" if periods else "; not a metric id from the list"
        return {"error": f"no metric {key}{hint}"}, f"no metric {key}"
    metric, entry = data.all_metrics[key], data.table[key]
    output = {"placeholder": f"{{{{m:{key}}}}}", "label": entry.label, "value": entry.display,
              "status": metric.status, "formula": metric.formula, "notes": metric.notes}
    return output, f"{key} = {entry.display}"


def search_filing(data: CompanyData, ctx: AskContext, query: str, section: str) -> tuple[list | dict, str]:
    if section not in SEARCH_SECTIONS:
        return {"error": f"section must be one of {', '.join(SEARCH_SECTIONS)}"}, f"bad section {section!r}"
    hits = search(data.index, query, k=PASSAGES_PER_SEARCH, sections=None if section == "any" else {section})
    for hit in hits:
        ctx.seen[hit.chunk.id] = hit.chunk
    output = [{"chunk_id": h.chunk.id, "section": h.chunk.section, "form": h.chunk.form,
               "period_end": h.chunk.period_end, "text": h.chunk.text} for h in hits]
    return output, f"{len(hits)} passages" + (f": {', '.join(h.chunk.id for h in hits)}" if hits else "")


def parse_arguments(arguments: str) -> dict | None:
    """The model's tool arguments as a dict, or None if they are not a JSON object."""
    try:
        args = json.loads(arguments or "{}")
    except ValueError:
        return None
    return args if isinstance(args, dict) else None


def run_tool(data: CompanyData, ctx: AskContext, name: str, arguments: str) -> tuple[object, str, dict]:
    """(tool output, summary, parsed arguments). Bad arguments become an error the model can read."""
    args = parse_arguments(arguments)
    if args is None:
        return {"error": "arguments were not a JSON object"}, "unreadable arguments", {}
    try:
        if name == "get_metric":
            output, summary = get_metric(data, str(args["metric_id"]), str(args["period"]))
        elif name == "search_filing":
            output, summary = search_filing(data, ctx, str(args["query"]), str(args["section"]))
        else:
            return {"error": f"unknown tool {name}"}, f"unknown tool {name}", args
    except KeyError as missing:
        return {"error": f"missing argument {missing}"}, f"missing argument {missing}", args
    return output, summary, args


def lookup_rounds(client, settings: AskSettings, data: CompanyData, ctx: AskContext,
                  messages: list[dict]) -> list[c.ToolTrace]:
    """Up to max_rounds tool turns. Appends every turn to messages; returns the trace."""
    trace = []
    for round_no in range(1, settings.max_rounds + 1):
        reply = client.complete(model=settings.writer_model, messages=list(messages), tools=TOOLS, tool_choice="auto",
                                max_completion_tokens=settings.max_completion_tokens,
                                reasoning_effort=settings.reasoning_effort)
        if not reply.tool_calls:
            if reply.content:
                messages.append({"role": "assistant", "content": reply.content})
            break
        messages.append({"role": "assistant", "content": reply.content or "", "tool_calls": [
            {"id": call.id, "type": "function", "function": {"name": call.name, "arguments": call.arguments}}
            for call in reply.tool_calls]})
        for n, call in enumerate(reply.tool_calls):
            if n < CALLS_PER_ROUND:
                output, summary, args = run_tool(data, ctx, call.name, call.arguments)
            else:
                output, summary = {"error": f"skipped: at most {CALLS_PER_ROUND} lookups per round"}, "skipped"
                args = parse_arguments(call.arguments) or {}
            messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(output)})
            trace.append(c.ToolTrace(round=round_no, tool=call.name, arguments=args, result=summary))
    return trace


def final_answer(client, settings: AskSettings, messages: list[dict]) -> AskAnswer:
    """The schema-only turn, with one retry if the reply cannot be read."""
    request = {"model": settings.writer_model, "response_format": ASK_FORMAT,
               "max_completion_tokens": settings.max_completion_tokens, "reasoning_effort": settings.reasoning_effort}
    messages = messages + [{"role": "user", "content": ASK_FINAL}]
    first = client.complete(messages=messages, **request)
    answer, error = parse_json(first.content, AskAnswer)
    if answer is not None:
        return answer
    retry = client.complete(messages=messages + [
        {"role": "assistant", "content": first.content or ""},
        {"role": "user", "content": f"Your reply was {error}. Return only the JSON answer."}], **request)
    answer, _ = parse_json(retry.content, AskAnswer)
    if answer is None:
        raise AskError(503, "The model's answer could not be read. Please try again.")
    return answer


def answer_question(client, settings: AskSettings, data: CompanyData, question: str) -> c.AskResponse:
    started = time.monotonic()
    ctx = AskContext(data.table, data.periods, data.judge_evidence)
    messages = [{"role": "system", "content": ASK_SYSTEM}, {"role": "user", "content": opening_message(data, question)}]
    trace = lookup_rounds(client, settings, data, ctx, messages)
    answer = final_answer(client, settings, messages)

    drafted = answer.claims if answer.status == "ok" else []
    to_check, extra = drafted[:settings.max_claims], drafted[settings.max_claims:]

    def check(numbered):
        n, claim = numbered
        verified, _ = verify_claim(f"ask-{n}", claim, ctx, client, model=settings.judge_model,
                                   reasoning_effort=settings.judge_reasoning_effort,
                                   max_tokens=settings.judge_max_completion_tokens)
        return verified

    with ThreadPoolExecutor(max_workers=max(1, len(to_check))) as pool:
        checked = list(pool.map(check, enumerate(to_check, start=1)))
    kept = [claim for claim in checked if claim.verdict == "supported"]
    removed = [c.RemovedClaim(text="".join(s.v for s in claim.segments), verdict=claim.verdict,
                              reason=claim.judge_reason) for claim in checked if claim.verdict != "supported"]
    removed += [c.RemovedClaim(text=claim.text, verdict="unsupported",
                               reason=f"not checked: more than {settings.max_claims} claims") for claim in extra]
    if answer.status == "out_of_scope":
        removed += [c.RemovedClaim(text=claim.text, verdict="unsupported", reason="answer marked out of scope")
                    for claim in answer.claims]

    metric_keys = {s.metric_id for claim in kept for s in claim.segments if s.t == "metric"}
    chunk_ids = {x.chunk_id for claim in kept for x in claim.citations} | {
        s.chunk_id for claim in kept for s in claim.segments if s.t == "quoted"}
    dates = [p.balance_sheet_date for p in data.metrics.periods]
    return c.AskResponse(
        ticker=data.metrics.ticker, question=question, status=answer.status, claims=kept, removed=removed,
        metrics={k: data.all_metrics[k] for k in sorted(metric_keys) if k in data.all_metrics},
        passages={cid: passage_from_chunk(ctx.seen[cid]) for cid in sorted(chunk_ids) if cid in ctx.seen},
        trace=trace, model=settings.writer_model, judge_model=settings.judge_model,
        seconds=round(time.monotonic() - started, 2), data_to=max(dates) if dates else None)
