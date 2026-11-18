"""Run the engine for one company: periods, resolved concepts, ratios, ladder, trends, checks and the log.

Pure: takes already-downloaded EDGAR JSON, so it runs the same on live data and on test fixtures.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from sourcebound.edgar.facts import parse_company_facts
from sourcebound.edgar.filings import Filing, latest_filing, parse_filings
from sourcebound.engine import checks
from sourcebound.engine.concepts import ConceptSpec
from sourcebound.engine.ladder import BUCKETS, Ladder, build_ladder
from sourcebound.engine.periods import PERIOD_ORDER, Period, find_periods
from sourcebound.engine.ratios import Ratio, compute_ratios
from sourcebound.engine.resolver import FactIndex, LogEntry, Resolved, Resolver
from sourcebound.engine.trends import Trend, build_trends
from sourcebound.overrides import Override

# Resolved for every period.
PERIOD_CONCEPTS = [
    "revenue",
    "operating_income",
    "d_and_a",
    "interest_expense",
    "short_term_debt",
    "total_debt",
    "cash",
    "short_term_investments",
    "cfo",
    "capex",
    "dividends",
    "undrawn_revolver",
]
# Resolved for FY0 only: the maturity table is in the annual 10-K.
LADDER_CONCEPTS = [concept for concept, _ in BUCKETS] + ["short_term_borrowings", "finance_lease_liabilities"]


@dataclass
class CompanyAnalysis:
    ticker: str
    name: str
    cik: int
    latest_10k: Filing
    latest_10q: Filing | None
    periods: dict[str, Period]
    period_problems: list[str]
    values: dict[str, dict[str, Resolved]]  # concept -> period label -> value
    ratios: dict[str, dict[str, Ratio]]  # metric id -> period label -> ratio
    ladder: Ladder | None  # FY0 only
    trends: list[Trend]
    debt_alternatives: dict[str, list[checks.Alternative]]  # period label -> every total-debt candidate
    log: list[LogEntry]
    specs: dict[str, ConceptSpec]
    index: FactIndex
    data_fetched_at: str | None = None
    overrides: list[Override] = field(default_factory=list)


def analyse_company(
    ticker: str,
    companyfacts: dict,
    submissions: dict,
    specs: dict[str, ConceptSpec],
    data_fetched_at: str | None = None,
    overrides: list[Override] | None = None,
) -> CompanyAnalysis:
    facts = parse_company_facts(companyfacts)
    filings = parse_filings(submissions)
    latest_10k, k_note = _latest_with_facts(filings, facts, "10-K")
    if latest_10k is None:
        raise ValueError(f"{ticker}: no 10-K with facts in the company-facts data")
    latest_10q, q_note = _latest_with_facts(filings, facts, "10-Q")
    found = find_periods(facts, latest_10k, latest_10q)
    periods = {label: found.periods[label] for label in PERIOD_ORDER if label in found.periods}

    cik = int(companyfacts["cik"])
    index = FactIndex(facts)
    resolver = Resolver(specs, index, cik)
    values: dict[str, dict[str, Resolved]] = {c: {} for c in PERIOD_CONCEPTS + LADDER_CONCEPTS}
    for label, period in periods.items():
        for concept in PERIOD_CONCEPTS:
            values[concept][label] = resolver.resolve(concept, period)
    if "FY0" in periods:
        for concept in LADDER_CONCEPTS:
            values[concept]["FY0"] = resolver.resolve(concept, periods["FY0"])

    ratios: dict[str, dict[str, Ratio]] = {}
    for label in periods:
        for ratio in compute_ratios({c: values[c][label] for c in PERIOD_CONCEPTS}, label):
            ratios.setdefault(ratio.metric_id, {})[label] = ratio

    ladder = None
    if "FY0" in periods:
        ladder = build_ladder({c: by_period["FY0"] for c, by_period in values.items() if "FY0" in by_period}, "FY0")
        for metric in ladder.metrics:
            ratios.setdefault(metric.metric_id, {})["FY0"] = metric

    log = [note for note in (k_note, q_note) if note] + list(resolver.log) + _checks(resolver, periods, values, ladder)
    return CompanyAnalysis(
        ticker=ticker.upper(),
        name=submissions.get("name", companyfacts.get("entityName", "")),
        cik=cik,
        latest_10k=latest_10k,
        latest_10q=latest_10q,
        periods=periods,
        period_problems=found.problems,
        values=values,
        ratios=ratios,
        ladder=ladder,
        trends=build_trends(ratios),
        debt_alternatives={label: checks.debt_alternatives(resolver, p) for label, p in periods.items()},
        log=log,
        specs=specs,
        index=index,
        data_fetched_at=data_fetched_at,
        overrides=list(overrides or []),
    )


def _latest_with_facts(filings: list[Filing], facts: list, form: str) -> tuple[Filing | None, LogEntry | None]:
    """The newest filing of this form whose facts are in the company-facts data.

    The filing list and the facts can disagree: facts can lag a new filing, or (ExxonMobil, 2026) a filing
    can be listed under a company whose facts sit under another registrant. A skipped newer filing is
    logged as stale data for the reviewer.
    """
    with_facts = {f.accession for f in facts}
    newest = latest_filing(filings, form)
    usable = latest_filing([f for f in filings if f.accession in with_facts], form)
    if newest is None or newest == usable:
        return usable, None
    used = f"{usable.accession} (period ended {usable.report_date})" if usable else "none"
    note = LogEntry(
        "stale_data", "filings", "LTM" if form == "10-Q" else "FY0",
        f"the newest {form}, {newest.accession} (period ended {newest.report_date}, filed {newest.filed}), has no "
        f"facts in this company's XBRL data; using {used} instead",
        "warning", form,
    )
    return usable, note


def _checks(resolver: Resolver, periods: dict[str, Period], values: dict, ladder: Ladder | None) -> list[LogEntry]:
    """Warnings and notes that compare values with each other. None of them changes a value."""
    log: list[LogEntry] = []
    for label, period in periods.items():
        log += checks.reconcile_total_debt(values["total_debt"][label], checks.debt_alternatives(resolver, period))
        uses_tag = any(i.tag == "LongTermDebt" for i in values["total_debt"][label].inputs)
        scope = checks.long_term_debt_scope(resolver, period, used=uses_tag)
        if scope:
            log.append(scope)
    for concept in PERIOD_CONCEPTS:
        entry = checks.mixed_ranks(concept, values[concept])
        if entry:
            log.append(entry)
    log += checks.revenue_changes({label: r.value for label, r in values["revenue"].items() if label != "LTM"})
    if ladder is not None:
        fy0 = {c: values[c]["FY0"].value for c in ("short_term_borrowings", "finance_lease_liabilities", "total_debt")}
        log += checks.reconcile_ladder(
            ladder.total, fy0["short_term_borrowings"], fy0["finance_lease_liabilities"], fy0["total_debt"], "FY0"
        )
    return log
