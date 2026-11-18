"""Deterioration flags (PLAN.md 4.10): the latest LTM against the prior fiscal year-end (FY0).

- leverage_up: Debt / EBITDA up by 0.5x or more, or into a worse scorecard band
- coverage_down: EBITDA / interest down by 20% or more, or into a worse band
- liquidity_shortfall: liquidity coverage below 1.2 (warning) or below 1.0 (alert)
- near_term_maturities: debt due within 12 months above 50% of cash + short-term investments + undrawn
  revolver (warning) or above 100% (alert)
- grade_change: a worse SB grade
Computed from the published metrics only; no model is involved.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.contracts import CompanyMetrics


@dataclass(frozen=True)
class Flag:
    type: str
    severity: str  # "warning" or "alert"
    rule: str
    metric_id: str
    from_value: str
    to_value: str


def _x(value: float | None, band: int | None) -> str:
    return f"{value:.2f}x" if value is not None else (f"band {band}" if band is not None else "not available")


def leverage_up(fy0: float | None, ltm: float | None, band_fy0: int | None, band_ltm: int | None) -> Flag | None:
    up = fy0 is not None and ltm is not None and ltm - fy0 >= 0.5 - 1e-9
    worse = band_fy0 is not None and band_ltm is not None and band_ltm > band_fy0
    if not (up or worse):
        return None
    return Flag("leverage_up", "warning", "Debt / EBITDA up by 0.5x or more, or into a worse band", "debt_to_ebitda",
                _x(fy0, band_fy0), _x(ltm, band_ltm))


def coverage_down(fy0: float | None, ltm: float | None, band_fy0: int | None, band_ltm: int | None) -> Flag | None:
    down = fy0 is not None and ltm is not None and fy0 > 0 and ltm <= fy0 * 0.8 + 1e-9
    worse = band_fy0 is not None and band_ltm is not None and band_ltm > band_fy0
    if not (down or worse):
        return None
    return Flag("coverage_down", "warning", "EBITDA / interest down by 20% or more, or into a worse band",
                "interest_coverage", _x(fy0, band_fy0), _x(ltm, band_ltm))


def liquidity_shortfall(ltm: float | None) -> Flag | None:
    if ltm is None or ltm >= 1.2:
        return None
    severity = "alert" if ltm < 1.0 else "warning"
    return Flag("liquidity_shortfall", severity, "liquidity coverage below 1.2 (warning) or 1.0 (alert)",
                "liquidity_coverage", "1.20x threshold", f"{ltm:.2f}x")


def near_term_maturities(due_12m: float | None, resources: float | None) -> Flag | None:
    if due_12m is None or resources is None or due_12m <= 0:
        return None
    share = due_12m / resources if resources > 0 else float("inf")
    if share <= 0.5:
        return None
    severity = "alert" if share > 1.0 else "warning"
    shown = "no cash or revolver" if resources <= 0 else f"{share:.0%}"
    return Flag("near_term_maturities", severity,
                "debt due within 12 months above 50% (warning) or 100% (alert) of cash, short-term investments "
                "and undrawn revolver", "short_term_debt", "50% threshold", shown)


def grade_change(fy0: str | None, latest: str | None) -> Flag | None:
    if fy0 is None or latest is None or int(latest.split("-")[1]) <= int(fy0.split("-")[1]):
        return None
    return Flag("grade_change", "warning", "a worse SB grade", "sb_grade", fy0, latest)


def _value(cm: CompanyMetrics, key: str) -> float | None:
    metric = cm.metrics.get(key)
    return metric.value if metric is not None and metric.status in ("ok", "net_cash") else None


def _band(card, factor: str) -> int | None:
    return next((f.band for f in card.factors if f.id == factor), None)


def compute_flags(cm: CompanyMetrics) -> list[Flag]:
    resources = [_value(cm, f"{c}:LTM") for c in ("cash", "short_term_investments", "undrawn_revolver")]
    candidates = [
        leverage_up(_value(cm, "debt_to_ebitda:FY0"), _value(cm, "debt_to_ebitda:LTM"),
                    _band(cm.scorecard_fy0, "debt_to_ebitda"), _band(cm.scorecard, "debt_to_ebitda")),
        coverage_down(_value(cm, "interest_coverage:FY0"), _value(cm, "interest_coverage:LTM"),
                      _band(cm.scorecard_fy0, "interest_coverage"), _band(cm.scorecard, "interest_coverage")),
        liquidity_shortfall(_value(cm, "liquidity_coverage:LTM")),
        near_term_maturities(_value(cm, "short_term_debt:LTM"), None if None in resources else sum(resources)),
        grade_change(cm.scorecard_fy0.grade, cm.scorecard.grade),
    ]
    return [flag for flag in candidates if flag is not None]
