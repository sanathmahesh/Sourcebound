"""The debt maturity ladder: how much debt falls due in each of the next five years and after.

A "maturity wall" is a large amount due in one year. The ladder comes from the maturity table in the latest
10-K (tags LongTermDebtMaturitiesRepaymentsOfPrincipal...), so it is as of FY0 only.

Debt due within 12 months is defined once for the whole engine: the balance sheet's short-term debt
(short-term borrowings plus the current portion of long-term debt). The ladder's year 1 is shown beside it.
So:
- debt due within 24 months = short-term debt + ladder year 2
- share due within 24 months = debt due within 24 months / total debt
- near-term maturity cover = debt due within 24 months / (cash + short-term investments + undrawn revolver)
  Below 1 means cash and committed credit lines could repay everything due in two years.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.engine.ratios import (
    NO_DEBT,
    NO_LIQUID_RESOURCES,
    NOT_AVAILABLE,
    NOT_MEANINGFUL,
    OK,
    Ratio,
    RatioValue,
)
from sourcebound.engine.resolver import Resolved

BUCKETS = [
    ("maturity_year_1", "Year 1"),
    ("maturity_year_2", "Year 2"),
    ("maturity_year_3", "Year 3"),
    ("maturity_year_4", "Year 4"),
    ("maturity_year_5", "Year 5"),
    ("maturity_after_year_5", "After year 5"),
]


@dataclass
class Ladder:
    period: str  # always FY0
    buckets: list[Resolved]
    total: float | None  # None unless every bucket is available
    metrics: list[Ratio]  # debt_due_24m, share_due_24m, near_term_maturity_cover


def near_term_maturity_cover(debt_due_24m: float | None, liquid_resources: float | None) -> RatioValue:
    if debt_due_24m is None or liquid_resources is None:
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    if liquid_resources <= 0:
        if debt_due_24m > 0:
            return RatioValue(None, NOT_MEANINGFUL, NO_LIQUID_RESOURCES)
        return RatioValue(0.0, OK)
    return RatioValue(debt_due_24m / liquid_resources, OK)


def share_due_24m(debt_due_24m: float | None, total_debt: float | None) -> RatioValue:
    """Percentage of total debt due within 24 months."""
    if debt_due_24m is None or total_debt is None:
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    if total_debt <= 0:
        return RatioValue(None, NOT_MEANINGFUL, NO_DEBT)
    return RatioValue(debt_due_24m / total_debt * 100, OK)


def build_ladder(values: dict[str, Resolved], period: str) -> Ladder:
    """The ladder and its three metrics from FY0's resolved concepts."""

    def v(concept: str) -> float | None:
        return values[concept].value

    def ratio(metric_id, label, unit, formula, concepts, result: RatioValue) -> Ratio:
        inputs = [values[c] for c in concepts]
        reason = result.reason
        if result.status == NOT_AVAILABLE:
            reason = "not available: no value for " + ", ".join(i.concept for i in inputs if i.status == "not_available")
        return Ratio(metric_id, label, period, result.value, unit, result.status, formula, reason, inputs)

    buckets = [values[concept] for concept, _ in BUCKETS]
    total = None if any(b.value is None for b in buckets) else sum(b.value for b in buckets)
    due = None if v("short_term_debt") is None or v("maturity_year_2") is None else v("short_term_debt") + v("maturity_year_2")
    liquid = None
    if not any(v(c) is None for c in ("cash", "short_term_investments", "undrawn_revolver")):
        liquid = v("cash") + v("short_term_investments") + v("undrawn_revolver")
    due_result = RatioValue(due, OK) if due is not None else RatioValue(None, NOT_AVAILABLE)
    metrics = [
        ratio("debt_due_24m", "Debt due within 24 months", "USD", "short_term_debt + maturity_year_2",
              ["short_term_debt", "maturity_year_2"], due_result),
        ratio("share_due_24m", "Share of debt due within 24 months", "%",
              "(short_term_debt + maturity_year_2) / total_debt",
              ["short_term_debt", "maturity_year_2", "total_debt"], share_due_24m(due, v("total_debt"))),
        ratio("near_term_maturity_cover", "Near-term maturity cover", "x",
              "(short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)",
              ["short_term_debt", "maturity_year_2", "cash", "short_term_investments", "undrawn_revolver"],
              near_term_maturity_cover(due, liquid)),
    ]
    return Ladder(period, buckets, total, metrics)
