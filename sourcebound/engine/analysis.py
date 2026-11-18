"""Run the phase-1 engine for one company: periods, resolved concepts, ratios, checks and the log.

Pure: takes already-downloaded EDGAR JSON, so it runs the same on live data and on test fixtures.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.edgar.facts import parse_company_facts
from sourcebound.edgar.filings import Filing, latest_filing, parse_filings
from sourcebound.engine import checks
from sourcebound.engine.concepts import ConceptSpec
from sourcebound.engine.periods import PERIOD_ORDER, Period, find_periods
from sourcebound.engine.ratios import Ratio, compute_ratios
from sourcebound.engine.resolver import FactIndex, LogEntry, Resolved, Resolver

# The concepts the four core ratios need (plus short_term_debt, part of total debt and a golden-sheet row).
PHASE1_CONCEPTS = [
    "operating_income",
    "d_and_a",
    "interest_expense",
    "short_term_debt",
    "total_debt",
    "cash",
    "short_term_investments",
    "cfo",
    "capex",
]


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
    debt_alternatives: dict[str, list[checks.Alternative]]  # period label -> every total-debt candidate
    log: list[LogEntry]
    specs: dict[str, ConceptSpec]
    index: FactIndex
    data_fetched_at: str | None = None


def analyse_company(
    ticker: str,
    companyfacts: dict,
    submissions: dict,
    specs: dict[str, ConceptSpec],
    data_fetched_at: str | None = None,
) -> CompanyAnalysis:
    facts = parse_company_facts(companyfacts)
    filings = parse_filings(submissions)
    latest_10k = latest_filing(filings, "10-K")
    if latest_10k is None:
        raise ValueError(f"{ticker}: no 10-K in the submissions filing list")
    latest_10q = latest_filing(filings, "10-Q")
    found = find_periods(facts, latest_10k, latest_10q)
    periods = {label: found.periods[label] for label in PERIOD_ORDER if label in found.periods}

    cik = int(companyfacts["cik"])
    index = FactIndex(facts)
    resolver = Resolver(specs, index, cik)
    values: dict[str, dict[str, Resolved]] = {c: {} for c in PHASE1_CONCEPTS}
    for label, period in periods.items():
        for concept in PHASE1_CONCEPTS:
            values[concept][label] = resolver.resolve(concept, period)

    ratios: dict[str, dict[str, Ratio]] = {}
    for label in periods:
        for ratio in compute_ratios({c: values[c][label] for c in PHASE1_CONCEPTS}, label):
            ratios.setdefault(ratio.metric_id, {})[label] = ratio

    log = list(resolver.log)
    alternatives = {}
    for label, period in periods.items():
        alternatives[label] = checks.debt_alternatives(resolver, period)
        log += checks.reconcile_total_debt(values["total_debt"][label], alternatives[label])
        scope = checks.long_term_debt_scope(resolver, period)
        if scope:
            log.append(scope)
    for concept in PHASE1_CONCEPTS:
        entry = checks.mixed_ranks(concept, values[concept])
        if entry:
            log.append(entry)

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
        debt_alternatives=alternatives,
        log=log,
        specs=specs,
        index=index,
        data_fetched_at=data_fetched_at,
    )
