"""Score a company on the grid.

1. Each factor gets a band from 1 (strongest) to 6 (weakest) from its ratio's value.
2. Statuses without a usable value map to fixed bands: EBITDA at or below zero scores 6 on leverage and
   coverage; net cash scores 1; no uses of cash scores 1 on liquidity; debt due with no cash or revolver
   scores 6. A company with no debt scores 1 on every debt-related factor.
3. A factor with no value at all ("not available") is left out, the remaining weights are scaled up to
   sum to 1 ("renormalised"), and the grade is marked provisional.
4. Weighted score = sum of weight x band over the factors scored, divided by the sum of their weights.
5. The weighted score maps to SB-1 ... SB-6; 3.5 or below counts as "IG-like".
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.engine.ratios import (
    EBITDA_NOT_POSITIVE,
    NO_DEBT,
    NO_LIQUID_RESOURCES,
    NO_USES,
    Ratio,
)
from sourcebound.scorecard.grid import Factor, Grid

DEBT_RELATED = {"debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "near_term_maturity_cover"}
NOT_MEANINGFUL_BANDS = {EBITDA_NOT_POSITIVE: 6, NO_DEBT: 1, NO_USES: 1, NO_LIQUID_RESOURCES: 6}


@dataclass
class FactorScore:
    id: str
    label: str
    period: str  # which period's ratio was scored
    value: float | None
    status: str
    band: int | None  # None when the factor could not be scored
    weight: float
    effective_weight: float | None  # weight after renormalisation; None when not scored
    note: str


@dataclass
class Scorecard:
    basis: str  # "latest" (LTM ratios, FY0 maturity ladder) or "FY0"
    grid_version: str
    factors: list[FactorScore]
    weighted_score: float | None
    grade: str | None
    provisional: bool
    ig_like: bool | None


def band_for(factor: Factor, value: float) -> int:
    """1 + the number of thresholds the value has reached on the weak side. A tie counts as reached."""
    if factor.higher_is_better:
        return 1 + sum(1 for t in factor.thresholds if value <= t)
    return 1 + sum(1 for t in factor.thresholds if value >= t)


def factor_band(factor: Factor, ratio: Ratio | None, zero_debt: bool) -> tuple[int | None, str]:
    """The band for one factor, and a note explaining any special case."""
    if ratio is None or ratio.status == "not_available":
        return None, "not available: left out and weights renormalised"
    if zero_debt and factor.id in DEBT_RELATED:
        return 1, "no debt: scores 1"
    if ratio.status == "net_cash":
        return 1, "net cash: scores 1"
    if ratio.status == "not_meaningful":
        band = NOT_MEANINGFUL_BANDS.get(ratio.reason)
        if band is None:
            return None, f"not meaningful ({ratio.reason}) and no fixed score: left out"
        return band, f"not meaningful ({ratio.reason}): scores {band}"
    return band_for(factor, ratio.value), ""


def grade_for(grid: Grid, weighted: float) -> tuple[str, bool]:
    """The SB grade for a weighted score, and whether it counts as IG-like."""
    grade = next((g for cut, g in grid.grades if weighted <= cut), grid.worst_grade)
    return grade, weighted <= grid.ig_like_max


def score(grid: Grid, metrics: dict[str, Ratio], zero_debt: bool, basis: str) -> Scorecard:
    """Score the metrics given for each factor (keyed by factor id)."""
    scored = []
    for factor in grid.factors:
        ratio = metrics.get(factor.id)
        band, note = factor_band(factor, ratio, zero_debt)
        scored.append(
            FactorScore(
                id=factor.id,
                label=factor.label,
                period=ratio.period if ratio else "",
                value=ratio.value if ratio else None,
                status=ratio.status if ratio else "not_available",
                band=band,
                weight=factor.weight,
                effective_weight=None,
                note=note,
            )
        )
    available = [f for f in scored if f.band is not None]
    total_weight = sum(f.weight for f in available)
    for f in available:
        f.effective_weight = f.weight / total_weight
    if not available:
        return Scorecard(basis, grid.version, scored, None, None, True, None)
    weighted = sum(f.weight * f.band for f in available) / total_weight
    grade, ig_like = grade_for(grid, weighted)
    return Scorecard(basis, grid.version, scored, weighted, grade, len(available) < len(scored), ig_like)


def score_company(grid: Grid, analysis, basis: str) -> Scorecard:
    """Score one analysed company.

    basis "latest": LTM ratios, with near-term maturity cover from FY0 (the maturity table is annual).
    basis "FY0": every factor from FY0.
    """
    ratio_period = "LTM" if basis == "latest" else "FY0"
    metrics = {}
    for factor in grid.factors:
        period = "FY0" if factor.id == "near_term_maturity_cover" else ratio_period
        metrics[factor.id] = analysis.ratios.get(factor.id, {}).get(period)
    debt = analysis.values["total_debt"].get(ratio_period)
    zero_debt = debt is not None and debt.status == "ok" and debt.value == 0
    return score(grid, metrics, zero_debt, basis)
