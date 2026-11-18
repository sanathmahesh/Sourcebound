"""The filing list from the EDGAR submissions API, and links to filings.

A 10-K is a company's annual report; a 10-Q is its quarterly report (filed for the first three quarters;
the fourth is covered by the 10-K). "/A" marks an amendment. Each filing has an accession number, its
unique ID, e.g. 0000732712-26-000007.
"""

from dataclasses import dataclass
from datetime import date

from sourcebound.edgar.tickers import cik10

PERIODIC_FORMS = {"10-K", "10-Q", "10-K/A", "10-Q/A"}


@dataclass(frozen=True)
class Filing:
    form: str
    accession: str
    filed: date
    report_date: date  # the period end the filing reports on
    primary_document: str


def submissions_url(cik: int) -> str:
    return f"https://data.sec.gov/submissions/CIK{cik10(cik)}.json"


def parse_filings(submissions: dict) -> list[Filing]:
    """The 10-K and 10-Q filings (and amendments) in filings.recent, newest first.

    filings.recent holds at least the last year or 1,000 filings, which always includes the latest 10-K.
    """
    recent = submissions["filings"]["recent"]
    filings = []
    for i, form in enumerate(recent["form"]):
        if form not in PERIODIC_FORMS or not recent["reportDate"][i]:
            continue
        filings.append(
            Filing(
                form=form,
                accession=recent["accessionNumber"][i],
                filed=date.fromisoformat(recent["filingDate"][i]),
                report_date=date.fromisoformat(recent["reportDate"][i]),
                primary_document=recent["primaryDocument"][i],
            )
        )
    return sorted(filings, key=lambda f: (f.filed, f.accession), reverse=True)


def latest_filing(filings: list[Filing], form: str) -> Filing | None:
    """The most recently filed filing of exactly this form (an original, not an amendment)."""
    matches = [f for f in filings if f.form == form]
    return max(matches, key=lambda f: (f.filed, f.accession)) if matches else None


def filing_index_url(cik: int, accession: str) -> str:
    """Link to a filing's index page on EDGAR, which lists every document in the filing."""
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{accession}-index.htm"
