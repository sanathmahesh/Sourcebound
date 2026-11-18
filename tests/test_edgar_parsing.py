"""Ticker lookup, filing list and company-facts parsing, on captured EDGAR fixtures."""

from datetime import date

import pytest

from sourcebound.edgar.facts import parse_company_facts
from sourcebound.edgar.filings import filing_index_url, latest_filing, parse_filings
from sourcebound.edgar.tickers import cik10, find_company
from tests.helpers import load_fixture


def test_find_company_by_ticker():
    rows = load_fixture("company_tickers_subset.json")["rows"]
    company = find_company(rows, "wmt")
    assert company.ticker == "WMT"
    assert company.cik == 104169  # from company_tickers.json, captured 17 Nov 2026
    assert cik10(company.cik) == "0000104169"


def test_unknown_ticker_raises():
    rows = load_fixture("company_tickers_subset.json")["rows"]
    with pytest.raises(KeyError, match="ZZZZ"):
        find_company(rows, "ZZZZ")


def test_parse_filings_keeps_periodic_reports_newest_first():
    filings = parse_filings(load_fixture("submissions_VZ.json"))
    assert all(f.form in {"10-K", "10-Q", "10-K/A", "10-Q/A"} for f in filings)
    assert filings == sorted(filings, key=lambda f: (f.filed, f.accession), reverse=True)


def test_latest_filings_vz():
    filings = parse_filings(load_fixture("submissions_VZ.json"))
    ten_k = latest_filing(filings, "10-K")
    ten_q = latest_filing(filings, "10-Q")
    assert ten_k.accession == "0000732712-26-000007"
    assert ten_k.report_date == date(2025, 12, 31)
    assert ten_q.accession == "0000732712-26-000052"
    assert ten_q.report_date == date(2026, 9, 30)


def test_filing_index_url():
    url = filing_index_url(732712, "0000732712-26-000007")
    assert url == "https://www.sec.gov/Archives/edgar/data/732712/000073271226000007/0000732712-26-000007-index.htm"


def test_parse_company_facts_types_and_filters():
    facts = parse_company_facts(load_fixture("companyfacts_GT.json"))
    assert facts, "expected facts"
    assert all(f.unit == "USD" for f in facts)
    assert all(f.form in {"10-K", "10-Q", "10-K/A", "10-Q/A"} for f in facts)
    instants = [f for f in facts if f.tag == "CashAndCashEquivalentsAtCarryingValue"]
    assert all(f.start is None for f in instants)
    flows = [f for f in facts if f.tag == "NetCashProvidedByUsedInOperatingActivities"]
    assert all(f.start is not None and f.start < f.end for f in flows)


def test_parse_company_facts_keeps_values_exactly():
    facts = parse_company_facts(load_fixture("companyfacts_GT.json"))
    match = [
        f
        for f in facts
        if f.tag == "NetCashProvidedByUsedInOperatingActivities"
        and f.start == date(2025, 1, 1)
        and f.end == date(2025, 12, 31)
        and f.accession == "0001628280-26-006708"
    ]
    assert len(match) == 1
    assert match[0].value == 796_000_000  # GT FY2025 cash from operations, accn 0001628280-26-006708
    assert match[0].filed == date(2026, 2, 10)


def test_document_url():
    from sourcebound.edgar.filings import document_url

    filings = parse_filings(load_fixture("submissions_VZ.json"))
    ten_k = latest_filing(filings, "10-K")
    assert document_url(732712, ten_k) == (
        "https://www.sec.gov/Archives/edgar/data/732712/000073271226000007/vz-20251231.htm"
    )
