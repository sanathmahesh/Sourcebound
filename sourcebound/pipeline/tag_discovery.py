"""Tag-discovery report: which candidate tags each company actually reports, period by period.

Run:  uv run python -m sourcebound.pipeline.tag_discovery WMT VZ GT

Writes reports/tag-discovery.md with, per company:
1. the candidate each concept resolves to in each period (all concepts in config/concepts.yaml);
2. every candidate tag: how many facts the company has reported under it, the latest period end, and
   whether it covers each of our periods;
3. related tags the company reports for FY0 that are in no chain, as material for proposed chain changes.
The report proposes nothing by itself; chain changes need the author's approval.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone

from sourcebound.edgar.client import EdgarError
from sourcebound.engine.analysis import CompanyAnalysis
from sourcebound.engine.concepts import ConceptSpec, load_concepts
from sourcebound.engine.periods import PERIOD_ORDER, Period, Window
from sourcebound.engine.resolver import Resolver
from sourcebound.paths import CONFIG_DIR, REPORTS_DIR
from sourcebound.pipeline.load import load_and_analyse, make_client
from sourcebound.pipeline.ratio_report import money

# Name fragments that suggest a tag belongs to a concept group. Used only to list related tags.
RELATED_KEYWORDS = {
    "revenue": ["Revenue", "SalesRevenue"],
    "operating income": ["OperatingIncome", "IncomeLossFromContinuingOperationsBeforeIncomeTaxes"],
    "depreciation and amortisation": ["Depreciation", "Amortization"],
    "interest": ["InterestExpense", "InterestPaid", "InterestCost", "InterestIncomeExpense"],
    "debt": ["Debt", "Borrowing", "CommercialPaper", "NotesPayable", "FinanceLeaseLiability"],
    "cash and investments": ["CashAndCashEquivalents", "ShortTermInvestments", "MarketableSecurities"],
    "cash from operations": ["NetCashProvidedByUsedInOperatingActivities"],
    "capital expenditure": ["PaymentsToAcquire", "CapitalExpenditure"],
    "dividends": ["Dividend"],
    "revolver": ["LineOfCredit"],
    "maturities": ["Maturities"],
}


@dataclass
class TagRow:
    concept: str
    rank: int
    candidate: str
    tag: str
    fact_count: int
    latest_end: date | None
    periods: dict[str, bool]  # period label -> does the tag cover this period


@dataclass
class RelatedTag:
    group: str
    tag: str
    value: float
    window: str


def _covers(a: CompanyAnalysis, spec: ConceptSpec, tag: str, period: Period) -> bool:
    if spec.kind == "instant":
        return bool(a.index.matching(tag, Window(None, period.end)))
    return all(a.index.matching(tag, part.window) for part in period.parts)


def discover_tags(a: CompanyAnalysis) -> list[TagRow]:
    rows = []
    for spec in a.specs.values():
        for candidate in spec.chain:
            for component in candidate.components:
                if component.tag is None:
                    continue
                facts = a.index.all_facts(component.tag)
                rows.append(
                    TagRow(
                        concept=spec.name,
                        rank=candidate.rank,
                        candidate=candidate.describe(),
                        tag=component.tag,
                        fact_count=len(facts),
                        latest_end=max((f.end for f in facts), default=None),
                        periods={label: _covers(a, spec, component.tag, p) for label, p in a.periods.items()},
                    )
                )
    return rows


def related_tags(a: CompanyAnalysis) -> list[RelatedTag]:
    """Tags in no chain, with a value for FY0, whose names suggest one of the concept groups."""
    in_chains = {c.tag for s in a.specs.values() for cand in s.chain for c in cand.components if c.tag}
    fy0 = a.periods.get("FY0")
    if fy0 is None:
        return []
    windows = [fy0.parts[0].window, Window(None, fy0.end)]
    found = []
    for tag in sorted(a.index.tags() - in_chains):
        group = next((g for g, words in RELATED_KEYWORDS.items() if any(w in tag for w in words)), None)
        if group is None:
            continue
        for window in windows:
            matches = a.index.matching(tag, window)
            if matches:
                found.append(RelatedTag(group, tag, matches[-1].value, str(window)))
                break
    return sorted(found, key=lambda r: (list(RELATED_KEYWORDS).index(r.group), r.tag))


def _resolution_table(a: CompanyAnalysis) -> list[str]:
    """Which candidate each concept resolves to, per period. Uses a separate resolver (no log kept)."""
    resolver = Resolver(a.specs, a.index, a.cik)
    labels = [l for l in PERIOD_ORDER if l in a.periods]
    lines = ["| Concept | " + " | ".join(labels) + " |", "|---" * (len(labels) + 1) + "|"]
    for name in a.specs:
        cells = []
        for label in labels:
            r = resolver.resolve(name, a.periods[label])
            if r.status == "ok":
                cells.append(f"rank {r.fallback_rank}: {r.candidate} = {money(r.value)}")
            else:
                cells.append(r.status.replace("_", " "))
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    return lines


def _tag_table(rows: list[TagRow], labels: list[str]) -> list[str]:
    lines = [
        "| Concept | Rank | Tag | Facts | Latest period end | " + " | ".join(labels) + " |",
        "|---" * (5 + len(labels)) + "|",
    ]
    for r in rows:
        marks = " | ".join("yes" if r.periods.get(l) else "—" for l in labels)
        latest = r.latest_end or "never reported"
        lines.append(f"| {r.concept} | {r.rank} | {r.tag} | {r.fact_count} | {latest} | {marks} |")
    return lines


def render_tag_discovery(
    analyses: list[CompanyAnalysis],
    related: dict[str, list[RelatedTag]],
    unusable: dict[str, str] | None = None,
) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Tag-discovery report",
        "",
        f"Generated {generated} from EDGAR company facts. Values in US$ millions. A tag 'covers' a period when",
        "the company reported it for exactly that period (for LTM: all three windows).",
        "",
    ]
    if unusable:
        lines += ["## Companies that could not be analysed", ""]
        lines += [f"- **{ticker}**: {reason}" for ticker, reason in unusable.items()]
        lines.append("")
    for a in analyses:
        labels = [l for l in PERIOD_ORDER if l in a.periods]
        lines += [
            f"## {a.ticker}",
            "",
            f"{a.name}, CIK {a.cik}. Latest 10-K {a.latest_10k.accession} (period ended {a.latest_10k.report_date}).",
            f"Facts downloaded {a.data_fetched_at or 'unknown'}.",
            "",
            "### Resolution by period",
            "",
            *_resolution_table(a),
            "",
            "### Candidate tags",
            "",
            *_tag_table(discover_tags(a), labels),
            "",
        ]
        extra = related.get(a.ticker, [])
        lines += [f"### Related tags reported for FY0 but in no chain ({len(extra)})", ""]
        if extra:
            lines += ["| Group | Tag | FY0 value ($m) | Period |", "|---|---|---|---|"]
            lines += [f"| {r.group} | {r.tag} | {money(r.value)} | {r.window} |" for r in extra]
        else:
            lines.append("None found (or not computed).")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(tickers: list[str]) -> None:
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    client = make_client()
    analyses, unusable = [], {}
    for ticker in tickers:
        try:
            analyses.append(load_and_analyse(client, ticker, specs))
        except (ValueError, EdgarError) as exc:  # reported, never worked around
            unusable[ticker] = str(exc)
            print(f"{ticker}: could not be analysed: {exc}")
    related = {a.ticker: related_tags(a) for a in analyses}
    text = render_tag_discovery(analyses, related, unusable)
    path = REPORTS_DIR / "tag-discovery.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"Tag-discovery report for {', '.join(tickers)} written to {path.relative_to(REPORTS_DIR.parent)}")


if __name__ == "__main__":
    main([t.upper() for t in sys.argv[1:]] or ["WMT", "VZ", "GT"])
