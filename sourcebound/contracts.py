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
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

SCHEMA_VERSION = "1"
DISCLAIMER = (
    "Educational project. Not investment advice. SB grades are a student's stylized scorecard, "
    "not credit ratings."
)

Status = Literal["ok", "not_available", "not_meaningful", "net_cash"]
Severity = Literal["info", "warning"]


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


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
        "provisional_grade", "stale_data",
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
