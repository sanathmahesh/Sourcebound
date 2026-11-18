"""Three-year trends: each ratio for FY-2, FY-1, FY0 and LTM, with a direction from FY-2 to LTM.

Direction is "improving", "worsening" or "stable", in the credit sense: lower leverage is better, higher
coverage, FCF / debt and liquidity are better. A change counts as stable when it is small:
- multiples (x): within 10% of the FY-2 value, and never less than 0.1x;
- percentages (%): within 2 percentage points.
If either end is not a number (not available, or not meaningful), the direction is "not available".
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.engine.periods import PERIOD_ORDER
from sourcebound.engine.ratios import Ratio

HIGHER_IS_BETTER = {
    "debt_to_ebitda": False,
    "net_leverage": False,
    "interest_coverage": True,
    "fcf_to_debt": True,
    "liquidity_coverage": True,
}
NUMERIC_STATUSES = {"ok", "net_cash"}


@dataclass
class Trend:
    metric_id: str
    label: str
    unit: str
    values: dict[str, float | None]
    statuses: dict[str, str]
    direction: str


def direction(start: float, end: float, higher_is_better: bool, unit: str) -> str:
    change = end - start
    tolerance = 2.0 if unit == "%" else max(0.10 * abs(start), 0.1)
    if abs(change) <= tolerance:
        return "stable"
    better = change > 0 if higher_is_better else change < 0
    return "improving" if better else "worsening"


def build_trends(ratios: dict[str, dict[str, Ratio]]) -> list[Trend]:
    trends = []
    for metric_id, higher_is_better in HIGHER_IS_BETTER.items():
        by_period = ratios.get(metric_id, {})
        if not by_period:
            continue
        first = next(iter(by_period.values()))
        values = {label: by_period[label].value for label in PERIOD_ORDER if label in by_period}
        statuses = {label: by_period[label].status for label in PERIOD_ORDER if label in by_period}
        start, end = by_period.get("FY-2"), by_period.get("LTM")
        if start and end and start.status in NUMERIC_STATUSES and end.status in NUMERIC_STATUSES \
                and start.value is not None and end.value is not None:
            label = direction(start.value, end.value, higher_is_better, first.unit)
        else:
            label = "not available"
        trends.append(Trend(metric_id, first.label, first.unit, values, statuses, label))
    return trends
