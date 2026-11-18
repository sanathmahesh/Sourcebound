"""New-filing detection: the latest original 10-K and 10-Q in a company's EDGAR filing list."""

from __future__ import annotations

from sourcebound.contracts import FilingRef
from sourcebound.edgar.filings import latest_filing, parse_filings


def latest_filings(submissions: dict) -> tuple[FilingRef | None, FilingRef | None]:
    filings = parse_filings(submissions)

    def ref(form: str) -> FilingRef | None:
        f = latest_filing(filings, form)
        return FilingRef(form=f.form, accession=f.accession, period_end=f.report_date, filed=f.filed) if f else None

    return ref("10-K"), ref("10-Q")
