"""Per-company check report: every ratio with its formula and, directly beneath it, the XBRL facts it used;
then the maturity ladder, trends and scorecard.

Run:  uv run python -m sourcebound.pipeline.ratio_report WMT VZ GT

Prints a Markdown report per company and writes the same to reports/ratios/<TICKER>.md, so each number
can be checked by hand against the 10-K and 10-Q.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone

from sourcebound.edgar.filings import Filing, filing_index_url
from sourcebound.engine.analysis import CompanyAnalysis
from sourcebound.engine.concepts import load_concepts
from sourcebound.engine.periods import PERIOD_ORDER
from sourcebound.engine.ratios import Ratio
from sourcebound.engine.resolver import Resolved
from sourcebound.contracts import DISCLAIMER
from sourcebound.paths import CONFIG_DIR, REPORTS_DIR
from sourcebound.pipeline.load import load_and_analyse, make_client
from sourcebound.scorecard.grid import load_grid
from sourcebound.scorecard.scoring import score_company

RATIO_IDS = ["debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "liquidity_coverage"]
LADDER_METRIC_IDS = ["debt_due_24m", "share_due_24m", "near_term_maturity_cover"]
LOG_KINDS = [
    ("not_available", "Not available"),
    ("reconciliation", "Reconciliation"),
    ("fallback", "Fallbacks beyond rank 1"),
    ("assumed_zero", "Assumed zero: not reported"),
    ("restated", "Restated values (most recently filed value used)"),
    ("mixed_ranks", "Different candidates across periods"),
    ("structural_change", "Possible structural change"),
    ("stale_data", "Stale data"),
]


def money(value: float | None) -> str:
    """USD as millions with thousands separators; exact (no rounding) when not a whole million."""
    if value is None:
        return "—"
    millions = value / 1e6
    return f"{millions:,.0f}" if value % 1_000_000 == 0 else f"{millions:,.3f}"


def show_ratio(ratio: Ratio) -> str:
    if ratio.value is None:
        return ratio.status.replace("_", " ")
    if ratio.unit == "x":
        text = f"{ratio.value:.2f}x"
    elif ratio.unit == "%":
        text = f"{ratio.value:.1f}%"
    else:
        text = f"${money(ratio.value)}m"
    return f"{text} (net cash)" if ratio.status == "net_cash" else text


def _filing_line(label: str, filing: Filing | None, cik: int) -> str:
    if filing is None:
        return f"- {label}: none"
    return (
        f"- {label}: {filing.form} for the period ended {filing.report_date}, filed {filing.filed}, "
        f"accession {filing.accession} ([EDGAR]({filing_index_url(cik, filing.accession)}))"
    )


def _periods_table(a: CompanyAnalysis) -> list[str]:
    lines = ["| Period | Flow items (income statement, cash flow) | Balance-sheet date |", "|---|---|---|"]
    for label in PERIOD_ORDER:
        period = a.periods.get(label)
        if period is None:
            lines.append(f"| {label} | not available | not available |")
            continue
        flows = " ".join(
            f"{'+' if p.sign > 0 else '−'} {p.role} ({p.window})" if len(period.parts) > 1 else str(p.window)
            for p in period.parts
        )
        lines.append(f"| {label} | {flows} | {period.end} |")
    return lines


def _summary_table(a: CompanyAnalysis) -> list[str]:
    labels = [l for l in PERIOD_ORDER if l in a.periods]
    lines = ["| Metric | " + " | ".join(labels) + " |", "|---" * (len(labels) + 1) + "|"]
    for metric_id in ["ebitda", *RATIO_IDS]:
        by_period = a.ratios.get(metric_id, {})
        first = next(iter(by_period.values()))
        cells = [show_ratio(by_period[l]) for l in labels]
        lines.append(f"| {first.label} | " + " | ".join(cells) + " |")
    return lines


def _fact_rows(inp: Resolved) -> list[str]:
    if inp.status == "not_available":
        return [f"| {inp.concept} | — | — | **not available** | — | — | — | — | {inp.reason} |"]
    if inp.status == "assumed_zero":
        return [f"| {inp.concept} | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |"]
    rows = []
    for s in inp.inputs:
        value = money(s.value)  # exactly as filed; the role says whether it was subtracted
        period = f"{s.start} to {s.end}" if s.start else f"at {s.end}"
        role = f"{s.role}, subtracted" if s.sign < 0 else s.role
        rows.append(
            f"| {inp.concept} | {s.tag} | {s.fallback_rank} | {value} | {period} ({role}) | {s.form} | "
            f"{s.accession} | {s.filed} | [EDGAR]({s.url}) |"
        )
    return rows


def _ratio_block(ratio: Ratio) -> list[str]:
    lines = [f"### {ratio.label} — {ratio.period}", ""]
    lines.append(f"**Formula:** {ratio.formula}  ")
    parts = []
    for inp in ratio.inputs:
        shown = "n/a" if inp.value is None else money(inp.value)
        parts.append(f"{inp.concept} {shown}")
    lines.append(f"**Inputs ($m):** {' · '.join(parts)} → **{show_ratio(ratio)}**  ")
    if ratio.reason and ratio.status != "ok":
        lines.append(f"**Status:** {ratio.status.replace('_', ' ')}: {ratio.reason}  ")
    flags = [f"{inp.concept}: {flag}" for inp in ratio.inputs for flag in inp.flags]
    if flags:
        lines.append(f"**Flags:** {'; '.join(flags)}  ")
    lines += [
        "",
        "| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    seen: set[str] = set()
    for inp in ratio.inputs:
        if inp.concept not in seen:
            seen.add(inp.concept)
            lines += _fact_rows(inp)
    lines.append("")
    return lines


def _debt_alternatives(a: CompanyAnalysis) -> list[str]:
    lines = [
        "Every total-debt candidate the company reports, for comparison with the one used (✔).",
        "",
        "| Period | Rank | Candidate | Value ($m) |",
        "|---|---|---|---|",
    ]
    for label, alternatives in a.debt_alternatives.items():
        used = a.values["total_debt"][label].fallback_rank
        for alt in alternatives:
            value = money(alt.value) if alt.value is not None else f"not usable: {alt.failure}"
            mark = " ✔" if alt.rank == used else ""
            lines.append(f"| {label} | {alt.rank}{mark} | {alt.candidate} | {value} |")
    return lines


def _log_sections(a: CompanyAnalysis) -> list[str]:
    lines = ["## Fallback log", ""]
    for kind, title in LOG_KINDS:
        entries = [e for e in a.log if e.kind == kind]
        lines += [f"### {title} ({len(entries)})", ""]
        lines += [f"- **{e.concept} {e.period}**{' (warning)' if e.severity == 'warning' else ''}: {e.message}" for e in entries]
        lines.append("")
    return lines


def _ladder_section(a: CompanyAnalysis) -> list[str]:
    if a.ladder is None:
        return []
    lines = [
        "## Maturity ladder (FY0, from the latest 10-K)",
        "",
        "| Bucket | Tag | Value ($m) | Accession |",
        "|---|---|---|---|",
    ]
    for bucket in a.ladder.buckets:
        tag = bucket.inputs[0].tag if bucket.inputs else "—"
        accession = bucket.inputs[0].accession if bucket.inputs else "—"
        shown = money(bucket.value) if bucket.value is not None else f"not available"
        lines.append(f"| {bucket.label} | {tag} | {shown} | {accession} |")
    lines += [f"| **Total** | | {money(a.ladder.total) if a.ladder.total is not None else 'not available'} | |", ""]
    for metric in a.ladder.metrics:
        lines += _ratio_block(metric)
    return lines


def _trends_section(a: CompanyAnalysis) -> list[str]:
    lines = ["## Trends (direction from FY-2 to LTM)", "", "| Ratio | " + " | ".join(PERIOD_ORDER) + " | Direction |",
             "|---" * (len(PERIOD_ORDER) + 2) + "|"]
    for t in a.trends:
        cells = [show_ratio(a.ratios[t.metric_id][p]) if p in a.ratios[t.metric_id] else "—" for p in PERIOD_ORDER]
        lines.append(f"| {t.label} | " + " | ".join(cells) + f" | {t.direction} |")
    return lines + [""]


def _scorecard_section(cards: list) -> list[str]:
    lines = ["## Scorecard", "", f"**{DISCLAIMER}**", ""]
    for card in cards:
        weighted = f"{card.weighted_score:.2f}" if card.weighted_score is not None else "n/a"
        lines += [f"### Basis: {card.basis} — weighted {weighted}, grade {card.grade or 'n/a'}"
                  f"{' (provisional)' if card.provisional else ''}", "",
                  "| Factor | Period | Value | Band | Weight | Note |", "|---|---|---|---|---|---|"]
        for f in card.factors:
            value = "—" if f.value is None else f"{f.value:.2f}"
            lines.append(f"| {f.label} | {f.period} | {value} | {f.band or '—'} | {f.weight:.2f} | {f.note} |")
        lines.append("")
    return lines


def render_ratio_report(a: CompanyAnalysis, cards: list | None = None) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# {a.ticker}: {a.name}",
        "",
        "Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.",
        "",
        f"- CIK: {a.cik}",
        f"- Company facts downloaded from EDGAR: {a.data_fetched_at or 'unknown'}; report generated {generated}",
        _filing_line("Latest 10-K", a.latest_10k, a.cik),
        _filing_line("Latest 10-Q", a.latest_10q, a.cik),
        "",
        "## Periods",
        "",
        *_periods_table(a),
        "",
    ]
    for label, period in a.periods.items():
        if period.note:
            lines.append(f"- {label}: {period.note}")
    lines += [f"- **Problem:** {p}" for p in a.period_problems]
    warnings = [e for e in a.log if e.severity == "warning"]
    lines += ["", "## Summary", "", *_summary_table(a), "", f"## Warnings ({len(warnings)})", ""]
    lines += [f"- **{e.concept} {e.period}**: {e.message}" for e in warnings] or ["None."]
    lines += ["", "## Ratios with their source facts", ""]
    for metric_id in RATIO_IDS:
        for label in PERIOD_ORDER:
            if label in a.ratios.get(metric_id, {}):
                lines += _ratio_block(a.ratios[metric_id][label])
    lines += [*_ladder_section(a), *_trends_section(a), *_scorecard_section(cards or [])]
    lines += ["## Debt reconciliation", "", *_debt_alternatives(a), "", *_log_sections(a)]
    return "\n".join(lines).rstrip() + "\n"


def main(tickers: list[str]) -> None:
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    grid = load_grid(CONFIG_DIR / "grid.yaml")
    client = make_client()
    out_dir = REPORTS_DIR / "ratios"
    out_dir.mkdir(parents=True, exist_ok=True)
    for ticker in tickers:
        analysis = load_and_analyse(client, ticker, specs)
        cards = [score_company(grid, analysis, "latest"), score_company(grid, analysis, "FY0")]
        text = render_ratio_report(analysis, cards)
        print(text)
        path = out_dir / f"{analysis.ticker}.md"
        path.write_text(text)
        print(f"[written to {path.relative_to(REPORTS_DIR.parent)}]\n")


if __name__ == "__main__":
    from sourcebound.pipeline.export import load_companies

    main([t.upper() for t in sys.argv[1:]] or [c["ticker"] for c in load_companies()])
