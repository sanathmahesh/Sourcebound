"""The published data contract: Pydantic models for the JSON files the site reads.

This module is the single source of truth for the shapes in PLAN.md 4.13. Phase 2 defines the parts the
metrics export needs (data/published/companies/<TICKER>/metrics.json); later phases add the memo,
verification, watchlist, evals and about files. JSON Schema and TypeScript types are generated from these
models in phase 7.

Metrics are keyed "<metric_id>:<period>", e.g. "net_leverage:LTM", matching the memo placeholders
{{m:net_leverage:LTM}}. Every metric carries the XBRL facts behind it.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

SCHEMA_VERSION = "1"
DISCLAIMER = (
    "Educational project. Not investment advice. SB grades are a student's stylized scorecard, "
    "not credit ratings."
)

Status = Literal["ok", "not_available", "not_meaningful", "net_cash"]
Severity = Literal["info", "warning"]


class Strict(BaseModel):
    # Published files are written with every field, defaults included, so the exported schema marks them all
    # required (serialization mode); TypeScript then needs no "maybe missing" checks.
    model_config = ConfigDict(extra="forbid", json_schema_serialization_defaults_required=True)


class MetricInput(Strict):
    """One XBRL fact behind a metric."""

    label: str  # plain-English concept label
    concept: str
    tag: str
    fallback_rank: int
    value: float  # exactly as filed
    unit: str
    period: str  # e.g. "2025-01-01 to 2025-12-31" or "at 2025-12-31"
    role: str  # which window of the period, e.g. "prior-year year-to-date"
    sign: int  # +1 added, -1 subtracted
    form: str
    accession: str
    filed: date
    url: str


class Metric(Strict):
    metric_id: str
    period: str
    label: str
    value: float | None
    unit: str  # "USD", "x" or "%"
    status: Status
    formula: str
    notes: list[str]
    inputs: list[MetricInput]


class Source(Strict):
    form: str
    accession: str
    period_end: date
    filed: date
    url: str


class PeriodInfo(Strict):
    label: str
    balance_sheet_date: date
    flow_windows: list[str]
    note: str


class TrendRow(Strict):
    metric_id: str
    label: str
    unit: str
    values: dict[str, float | None]
    statuses: dict[str, Status]
    direction: Literal["improving", "worsening", "stable", "not available"]


class LadderBucket(Strict):
    id: str
    label: str
    value: float | None
    status: Status
    metric_key: str


class MaturityLadder(Strict):
    as_of: date
    buckets: list[LadderBucket]
    total: float | None
    metric_keys: list[str]  # debt due in 24 months, share due in 24 months, near-term maturity cover


class ScorecardFactor(Strict):
    id: str
    label: str
    period: str
    value: float | None
    status: Status
    band: int | None = Field(ge=1, le=6)
    weight: float
    effective_weight: float | None
    note: str


class Scorecard(Strict):
    basis: Literal["latest", "FY0"]
    grid_version: str
    factors: list[ScorecardFactor]
    weighted_score: float | None
    grade: str | None
    provisional: bool
    ig_like: bool | None
    disclaimer: str = DISCLAIMER


class ChecklistItem(Strict):
    id: str
    category: Literal[
        "not_available", "fallback", "assumed_zero", "override", "reconciliation", "structural_change",
        "provisional_grade", "stale_data", "unsupported_claim", "partially_supported_claim", "draft_problem",
    ]
    severity: Severity
    message: str
    ref: str  # the concept or metric the item is about


class LogItem(Strict):
    kind: str
    concept: str
    period: str
    message: str
    severity: Severity
    subject: str


class CompanyMetrics(Strict):
    """data/published/companies/<TICKER>/metrics.json: the latest metrics, possibly newer than the memo."""

    schema_version: str = SCHEMA_VERSION
    ticker: str
    name: str
    cik: int
    sector: str
    generated_at: datetime
    data_fetched_at: str | None
    sources: list[Source]
    periods: list[PeriodInfo]
    period_problems: list[str]
    metrics: dict[str, Metric]
    trends: list[TrendRow]
    maturity_ladder: MaturityLadder | None
    scorecard: Scorecard
    scorecard_fy0: Scorecard
    checklist: list[ChecklistItem]
    log: list[LogItem]
    disclaimer: str = DISCLAIMER


# ----- memo.json and verification.json (phase 4) ------------------------------------------------------


class Segment(Strict):
    """A piece of a rendered claim: plain text, an engine metric, or a figure quoted from a passage."""

    t: Literal["text", "metric", "quoted"]
    v: str
    metric_id: str | None = None  # "<metric_id>:<period>" for t = metric
    chunk_id: str | None = None  # the passage a quoted figure comes from


class MemoCitation(Strict):
    chunk_id: str
    quote: str
    check: Literal["ok", "chunk_not_found", "quote_too_short", "quote_not_found"]


Verdict = Literal["supported", "partially_supported", "unsupported"]


class MemoClaim(Strict):
    id: str
    kind: Literal["quantitative", "qualitative"]
    verdict: Verdict
    judge_reason: str
    evidence_quote: str
    checked_by: Literal["judge", "deterministic"]  # deterministic = failed a number or quote check, no model call
    segments: list[Segment]
    citations: list[MemoCitation]
    flags: list[str]  # e.g. "number check failed: ...", "kept after failed repair"


class MemoSection(Strict):
    id: str
    title: str
    claims: list[MemoClaim]
    passages_shown: list[str]  # chunk ids given to the writer
    notes: list[str]


class Passage(Strict):
    text: str
    section: str
    form: str
    filed: str
    period_end: str
    accession: str
    url: str
    start: int
    end: int


class CallTotals(Strict):
    calls: int
    input_tokens: int
    cached_input_tokens: int
    output_tokens: int
    cost_usd: float
    seconds: float


class RunInfo(Strict):
    run_id: str
    started_at: datetime
    writer_model: str
    judge_model: str
    service_tier: str
    reasoning_effort: dict[str, str]
    prices_read_on: str
    drafting: CallTotals
    verification: CallTotals
    raw_outputs: str  # path to the saved requests and responses


class Memo(Strict):
    """data/published/companies/<TICKER>/memo.json: a dated snapshot with its own metrics and passages."""

    schema_version: str = SCHEMA_VERSION
    ticker: str
    name: str
    memo_date: date
    model: str
    judge_model: str
    grade: str | None
    grade_provisional: bool
    sources: list[Source]
    sections: list[MemoSection]
    metrics: dict[str, Metric]
    passages: dict[str, Passage]
    trends: list[TrendRow]
    maturity_ladder: MaturityLadder | None
    scorecard: Scorecard
    checklist: list[ChecklistItem]
    run: RunInfo
    disclaimer: str = DISCLAIMER


class NumberTrace(Strict):
    claim_id: str
    kind: Literal["metric", "quoted"]
    value: str
    metric_id: str | None = None
    chunk_id: str | None = None


class ClaimCheck(Strict):
    claim_id: str
    section: str
    kind: str
    verdict: Verdict
    checked_by: str
    reason: str
    citation_checks: list[str]
    flags: list[str]


class VerificationSummary(Strict):
    claims: int
    supported: int
    partially_supported: int
    unsupported: int
    checked_by_judge: int
    checked_deterministically: int
    metric_figures: int
    quoted_figures: int
    raw_numbers_rejected: int  # typed digits the validator rejected in first drafts, before any repair
    repairs: int
    sections_without_draft: int


class VerificationReport(Strict):
    """data/published/companies/<TICKER>/verification.json"""

    schema_version: str = SCHEMA_VERSION
    ticker: str
    memo_date: date
    writer_model: str
    judge_model: str
    summary: VerificationSummary
    numbers: list[NumberTrace]
    claims: list[ClaimCheck]
    fallback_log: list[LogItem]
    warnings: list[LogItem]


# ----- state.json, watchlist.json, index.json, evals.json (phase 6) ----------------------------------


class FilingRef(Strict):
    form: str
    accession: str
    period_end: date
    filed: date


class CompanyState(Strict):
    latest_10k: FilingRef | None
    latest_10q: FilingRef | None
    memo_status: Literal["current", "stale", "missing"]
    memo_date: date | None


class WatchState(Strict):
    """data/published/state.json: what the daily job last saw for each company."""

    schema_version: str = SCHEMA_VERSION
    checked_at: datetime
    last_heartbeat: datetime
    companies: dict[str, CompanyState]


class WatchFlag(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True, json_schema_serialization_defaults_required=True)

    type: str
    severity: Literal["warning", "alert"]
    rule: str
    metric_id: str
    from_: str = Field(alias="from")
    to: str


class WatchItem(Strict):
    ticker: str
    name: str
    latest_filing: FilingRef | None
    data_to: date | None  # balance-sheet date of the latest metrics (LTM)
    memo_status: Literal["current", "stale", "missing"]
    memo_date: date | None
    flags: list[WatchFlag]


class Watchlist(Strict):
    """data/published/watchlist.json"""

    schema_version: str = SCHEMA_VERSION
    checked_at: datetime
    items: list[WatchItem]


class HeadlineRatio(Strict):
    metric_id: str
    label: str
    period: str
    value: float | None
    unit: str
    status: Status
    display: str


class VerificationCounts(Strict):
    claims: int
    supported: int
    partially_supported: int
    unsupported: int


class IndexEntry(Strict):
    ticker: str
    name: str
    sector: str
    grade: str | None
    score: float | None
    provisional: bool
    ig_like: bool | None
    headline: list[HeadlineRatio]
    latest_filing: FilingRef | None
    data_to: date | None
    memo_status: Literal["current", "stale", "missing"]
    memo_date: date | None
    memo_model: str | None
    verification: VerificationCounts | None
    open_flags: int
    flag_types: list[str]


class SiteIndex(Strict):
    """data/published/index.json: one entry per company, for the portfolio page."""

    schema_version: str = SCHEMA_VERSION
    generated_at: datetime
    companies: list[IndexEntry]
    disclaimer: str = DISCLAIMER


class EvalsFile(Strict):
    """data/published/evals.json: the evaluation results (evals/results/results.json), for the site."""

    schema_version: str = SCHEMA_VERSION
    generated_at: datetime
    source: str
    results: dict


# ----- the live follow-up endpoint, POST /api/ask (phase 7) --------------------------------------------

Question = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]


class AskRequest(Strict):
    """The request body. The ticker fixes which company's files the tools may read."""

    ticker: Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, min_length=1, max_length=10)]
    question: Question


class ToolTrace(Strict):
    """One tool call the model made, for the "what was looked up" list."""

    round: int
    tool: str
    arguments: dict
    result: str  # a one-line summary of what the tool returned


class RemovedClaim(Strict):
    """A claim that failed verification and was taken out of the answer."""

    text: str  # rendered: placeholders replaced by engine values
    verdict: Verdict
    reason: str


class AskResponse(Strict):
    """The answer. Claims have the memo's shape; only claims the judge marked supported are kept."""

    schema_version: str = SCHEMA_VERSION
    ticker: str
    question: str
    status: Literal["ok", "out_of_scope"]
    claims: list[MemoClaim]
    removed: list[RemovedClaim]
    metrics: dict[str, Metric]  # the metrics the kept claims show, with their lineage
    passages: dict[str, Passage]  # the passages the kept claims cite
    trace: list[ToolTrace]
    model: str
    judge_model: str
    seconds: float
    data_to: date | None  # the latest balance-sheet date in the metrics used
    disclaimer: str = DISCLAIMER
