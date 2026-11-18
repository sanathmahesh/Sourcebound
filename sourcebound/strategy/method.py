"""The method page, generated from config/grid.yaml and the engine's own formula strings.

Nothing is typed by hand: thresholds, weights and grade cut-offs are read from the grid, and each ratio's
definition is the formula the engine records with every published metric.
"""

from __future__ import annotations

from sourcebound.contracts import CompanyMetrics
from sourcebound.scorecard.grid import Factor, Grid
from sourcebound.scorecard.scoring import NOT_MEANINGFUL_BANDS

RATIOS = ["ebitda", "debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "liquidity_coverage",
          "near_term_maturity_cover"]


def _unit(factor: Factor) -> str:
    return "%" if factor.id == "fcf_to_debt" else "x"


def band_ranges(factor: Factor, tie_rule: str) -> list[str]:
    """Plain-English range for each band 1 (strongest) to 6. With tie rule "worse", a value exactly on a
    threshold belongs to the weaker band."""
    if tie_rule != "worse":
        raise ValueError(f"unsupported tie rule {tie_rule}")
    u, t = _unit(factor), [f"{v:g}" for v in factor.thresholds]
    if factor.higher_is_better:
        return [f"over {t[0]}{u}"] + [f"over {t[i + 1]}{u} to {t[i]}{u}" for i in range(4)] + [f"{t[4]}{u} or less"]
    return [f"under {t[0]}{u}"] + [f"{t[i]}{u} to under {t[i + 1]}{u}" for i in range(4)] + [f"{t[4]}{u} or more"]


def method_markdown(grid: Grid, example: CompanyMetrics) -> str:
    formulas = {m.metric_id: (m.label, m.formula) for m in example.metrics.values() if m.metric_id in RATIOS}
    lines = [
        "# Method", "",
        "Every figure is computed by code from the company's XBRL data in its 10-K and 10-Q filings, using the",
        "most recently filed value for each period. LTM (last twelve months) adds the latest year-to-date flows to",
        "the last fiscal year and subtracts the prior year's year-to-date flows. A figure that cannot be found is",
        "shown as \"not available\"; it is never estimated.", "",
        "## Ratios", "",
        "| Ratio | Definition |", "|---|---|",
    ]
    lines += [f"| {formulas[r][0]} | `{formulas[r][1]}` |" for r in RATIOS if r in formulas]
    lines += [
        "", f"## The SB scorecard ({grid.version})", "",
        "SB grades are a student's stylized scorecard, not credit ratings. Each factor is placed in a band from 1",
        "(strongest) to 6 (weakest); the grade comes from the weighted average band. "
        f"A value exactly on a threshold gets the weaker band (tie rule \"{grid.tie_rule}\").", "",
        "| Factor | Weight | " + " | ".join(f"Band {b}" for b in range(1, 7)) + " |",
        "|---|---|" + "---|" * 6,
    ]
    for f in grid.factors:
        lines.append(f"| {f.label} | {f.weight * 100:.0f}% | " + " | ".join(band_ranges(f, grid.tie_rule)) + " |")
    lines += ["", "Special cases: net cash scores band 1; a company with no debt scores band 1 on the debt factors; "
              "a ratio that cannot be computed meaningfully scores a fixed band when the reason is "
              + "; ".join(f"{reason} (band {band})" for reason, band in NOT_MEANINGFUL_BANDS.items())
              + ". Any other unscorable factor is left out."]
    lines += ["", "| Weighted score | Grade |", "|---|---|"]
    lower = None
    for upper, grade in grid.grades:
        lines.append(f"| {'up to' if lower is None else f'over {lower:g} to'} {upper:g} | {grade} |")
        lower = upper
    lines += [f"| over {lower:g} | {grid.worst_grade} |", "",
              f"A weighted score of {grid.ig_like_max:g} or less counts as \"IG-like\" (investment-grade-like) in the "
              "comparison with agency ratings. When a factor cannot be scored, the remaining weights are scaled up "
              "and the grade is marked provisional.", ""]
    return "\n".join(lines)
