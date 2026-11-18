"""Normalise the XBRL company-facts API into a flat list of facts.

XBRL tags each number in a filing with a concept from a standard taxonomy (here us-gaap). The company
facts API returns, per tag and unit, every value the company has reported, each with its period
(start and end dates, or only an end date for balance-sheet items), the filing it came from (accession
number, form, filing date) and the filing's fiscal-year fields fy/fp.

Two facts about this API shape the engine:
- It holds only standard-taxonomy facts without dimensions: company-specific extension tags and segment
  breakdowns are absent.
- fy and fp describe the filing a fact appeared in, not the fact's own period, so they are dropped here;
  the engine identifies periods from start and end dates only.
"""

from dataclasses import dataclass
from datetime import date

from sourcebound.edgar.filings import PERIODIC_FORMS
from sourcebound.edgar.tickers import cik10


@dataclass(frozen=True)
class Fact:
    tag: str  # us-gaap concept name, e.g. "LongTermDebtNoncurrent"
    unit: str  # "USD"
    value: float
    start: date | None  # None for an instant (balance-sheet) fact
    end: date
    accession: str
    form: str
    filed: date


def companyfacts_url(cik: int) -> str:
    return f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10(cik)}.json"


def parse_company_facts(data: dict, unit: str = "USD") -> list[Fact]:
    """Every us-gaap fact in the given unit that came from a 10-K or 10-Q (or amendment).

    Facts from other forms (8-K, S-4 and so on) are dropped: the engine works from periodic reports.
    """
    facts = []
    for tag, body in data.get("facts", {}).get("us-gaap", {}).items():
        for row in body.get("units", {}).get(unit, []):
            if row.get("form") not in PERIODIC_FORMS:
                continue
            facts.append(
                Fact(
                    tag=tag,
                    unit=unit,
                    value=row["val"],
                    start=date.fromisoformat(row["start"]) if row.get("start") else None,
                    end=date.fromisoformat(row["end"]),
                    accession=row["accn"],
                    form=row["form"],
                    filed=date.fromisoformat(row["filed"]),
                )
            )
    return facts
