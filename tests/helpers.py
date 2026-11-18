"""Builders for synthetic test data.

Synthetic facts use the fictional accession prefix 0000000000 and small round numbers. They test logic
only and are never presented as any company's data. Real-company values live only in tests that read the
captured fixtures in tests/fixtures/edgar/.
"""

import json
from datetime import date
from pathlib import Path

from sourcebound.edgar.facts import Fact
from sourcebound.edgar.filings import Filing

FIXTURES = Path(__file__).parent / "fixtures" / "edgar"


def d(text: str) -> date:
    return date.fromisoformat(text)


def fact(
    tag: str,
    value: float,
    end: str,
    start: str | None = None,
    accession: str = "0000000000-24-000001",
    filed: str = "2024-03-01",
    form: str = "10-K",
) -> Fact:
    return Fact(
        tag=tag,
        unit="USD",
        value=value,
        start=d(start) if start else None,
        end=d(end),
        accession=accession,
        form=form,
        filed=d(filed),
    )


def filing(form: str, accession: str, filed: str, report_date: str) -> Filing:
    return Filing(
        form=form,
        accession=accession,
        filed=d(filed),
        report_date=d(report_date),
        primary_document="doc.htm",
    )


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())
