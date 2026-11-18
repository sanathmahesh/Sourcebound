"""Phase-2 summary reports, written by the export command.

- reports/coverage.md: company by concept, which fallback rank each period used, or assumed zero, or not
  available; and company by ratio, whether each period has a value.
- reports/scorecard.md: the scorecard table for all companies.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sourcebound.contracts import DISCLAIMER, CompanyMetrics
from sourcebound.engine.analysis import LADDER_CONCEPTS, PERIOD_CONCEPTS, CompanyAnalysis
from sourcebound.engine.periods import PERIOD_ORDER
from sourcebound.paths import REPORTS_DIR

RATIO_IDS = ["debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "liquidity_coverage"]
STATUS_MARK = {"ok": "ok", "not_available": "–", "not_meaningful": "nm", "net_cash": "nc"}


def _concept_cell(analysis: CompanyAnalysis, concept: str, periods: list[str]) -> str:
    marks = []
    for label in periods:
        r = analysis.values[concept].get(label)
        if r is None or r.status == "not_available":
            marks.append("–")
        elif r.status == "assumed_zero":
            marks.append("0")
        else:
            marks.append(str(r.fallback_rank))
    return "·".join(marks)


def render_coverage(exported: list[tuple[CompanyAnalysis, CompanyMetrics]]) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Coverage report",
        "",
        f"Generated {generated}. For each company and concept: the fallback rank used in FY-2·FY-1·FY0·LTM.",
        "`1` = first-choice tag, `2`+ = a fallback (logged), `0` = assumed zero because not reported (on the",
        "reviewer checklist), `–` = not available. Chains are in config/concepts.yaml.",
        "",
        "## Concepts, every period",
        "",
        "| Ticker | " + " | ".join(PERIOD_CONCEPTS) + " |",
        "|---" * (len(PERIOD_CONCEPTS) + 1) + "|",
    ]
    for a, _ in exported:
        cells = [_concept_cell(a, c, PERIOD_ORDER) for c in PERIOD_CONCEPTS]
        lines.append(f"| {a.ticker} | " + " | ".join(cells) + " |")
    lines += [
        "",
        "## Maturity ladder and related, FY0 only",
        "",
        "| Ticker | " + " | ".join(LADDER_CONCEPTS) + " |",
        "|---" * (len(LADDER_CONCEPTS) + 1) + "|",
    ]
    for a, _ in exported:
        lines.append(f"| {a.ticker} | " + " | ".join(_concept_cell(a, c, ["FY0"]) for c in LADDER_CONCEPTS) + " |")
    lines += [
        "",
        "## Ratios, FY-2·FY-1·FY0·LTM",
        "",
        "`ok` = value, `nm` = not meaningful (e.g. EBITDA at or below zero), `nc` = net cash, `–` = not available.",
        "",
        "| Ticker | " + " | ".join(RATIO_IDS) + " | near_term_maturity_cover (FY0) |",
        "|---" * (len(RATIO_IDS) + 2) + "|",
    ]
    for a, _ in exported:
        cells = []
        for metric_id in RATIO_IDS:
            by_period = a.ratios.get(metric_id, {})
            cells.append("·".join(STATUS_MARK[by_period[l].status] if l in by_period else "–" for l in PERIOD_ORDER))
        near = a.ratios.get("near_term_maturity_cover", {}).get("FY0")
        cells.append(STATUS_MARK[near.status] if near else "–")
        lines.append(f"| {a.ticker} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def _factor_cell(metrics: CompanyMetrics, factor_id: str) -> str:
    factor = next(f for f in metrics.scorecard.factors if f.id == factor_id)
    if factor.band is None:
        return "n/a"
    if factor.value is None:
        shown = factor.status.replace("_", " ")
    elif factor_id == "fcf_to_debt":
        shown = f"{factor.value:.1f}%"
    else:
        shown = f"{factor.value:.2f}x"
    if factor.status == "net_cash":
        shown = "net cash"
    return f"{shown} ({factor.band})"


def render_scorecard(exported: list[tuple[CompanyAnalysis, CompanyMetrics]]) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    factor_ids = [f.id for f in exported[0][1].scorecard.factors] if exported else []
    labels = [f.label for f in exported[0][1].scorecard.factors] if exported else []
    lines = [
        "# Scorecard",
        "",
        f"**{DISCLAIMER}**",
        "",
        f"Generated {generated}. Grid {exported[0][1].scorecard.grid_version if exported else ''} (config/grid.yaml):",
        "each cell shows the ratio and, in brackets, its band from 1 (strongest) to 6 (weakest). Basis: LTM ratios,",
        "with near-term maturity cover from the latest 10-K (FY0). A tie on a threshold takes the worse band.",
        "Provisional = a factor could not be scored and the other weights were renormalised.",
        "",
        "| Ticker | Sector | " + " | ".join(labels) + " | Weighted | SB grade | IG-like | Provisional | FY0 grade | Data to |",
        "|---" * (len(labels) + 8) + "|",
    ]
    rows = sorted(exported, key=lambda pair: (pair[1].scorecard.weighted_score is None, pair[1].scorecard.weighted_score or 0))
    for a, m in rows:
        card, fy0 = m.scorecard, m.scorecard_fy0
        weighted = f"{card.weighted_score:.2f}" if card.weighted_score is not None else "n/a"
        data_to = a.periods["LTM"].end if "LTM" in a.periods else "n/a"
        lines.append(
            f"| {a.ticker} | {m.sector} | " + " | ".join(_factor_cell(m, f) for f in factor_ids)
            + f" | {weighted} | {card.grade or 'n/a'} | {'yes' if card.ig_like else 'no'} | "
            + f"{'yes' if card.provisional else 'no'} | {fy0.grade or 'n/a'} | {data_to} |"
        )
    lines += ["", "Sorted from strongest to weakest weighted score."]
    return "\n".join(lines) + "\n"


def write_coverage_report(exported) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "coverage.md").write_text(render_coverage(exported))


def write_scorecard_report(exported) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "scorecard.md").write_text(render_scorecard(exported))
