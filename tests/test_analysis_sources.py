"""Which filings the analysis uses: the newest 10-K and 10-Q that actually have facts in the data."""

from sourcebound.engine.analysis import analyse_company
from sourcebound.engine.concepts import load_concepts
from sourcebound.paths import CONFIG_DIR

SPECS = load_concepts(CONFIG_DIR / "concepts.yaml")
K, Q1, Q2 = "0000000000-26-000001", "0000000000-26-000002", "0000000000-26-000003"


def fact(start, end, val, accn, form, filed):
    row = {"end": end, "val": val, "accn": accn, "form": form, "filed": filed}
    if start:
        row["start"] = start
    return row


def synthetic_inputs(include_q2_facts: bool):
    revenue = [
        fact("2025-01-01", "2025-12-31", 100, K, "10-K", "2026-02-15"),
        fact("2024-01-01", "2024-12-31", 90, K, "10-K", "2026-02-15"),
        fact("2023-01-01", "2023-12-31", 80, K, "10-K", "2026-02-15"),
        fact("2026-01-01", "2026-03-31", 30, Q1, "10-Q", "2026-05-01"),
        fact("2025-01-01", "2025-03-31", 25, Q1, "10-Q", "2026-05-01"),
    ]
    if include_q2_facts:
        revenue += [
            fact("2026-01-01", "2026-06-30", 60, Q2, "10-Q", "2026-08-01"),
            fact("2025-01-01", "2025-06-30", 50, Q2, "10-Q", "2026-08-01"),
        ]
    companyfacts = {"cik": 1, "entityName": "Test Co", "facts": {"us-gaap": {"Revenues": {"units": {"USD": revenue}}}}}
    submissions = {
        "name": "Test Co",
        "filings": {"recent": {
            "form": ["10-Q", "10-Q", "10-K"],
            "accessionNumber": [Q2, Q1, K],
            "filingDate": ["2026-08-01", "2026-05-01", "2026-02-15"],
            "reportDate": ["2026-06-30", "2026-03-31", "2025-12-31"],
            "primaryDocument": ["q2.htm", "q1.htm", "k.htm"],
        }},
    }
    return companyfacts, submissions


def test_newest_10q_used_when_its_facts_are_present():
    a = analyse_company("TEST", *synthetic_inputs(include_q2_facts=True), SPECS)
    assert a.latest_10q.accession == Q2
    assert not [e for e in a.log if e.kind == "stale_data"]


def test_10q_without_facts_is_skipped_and_flagged():
    a = analyse_company("TEST", *synthetic_inputs(include_q2_facts=False), SPECS)
    assert a.latest_10q.accession == Q1
    assert str(a.periods["LTM"].end) == "2026-03-31"
    [entry] = [e for e in a.log if e.kind == "stale_data"]
    assert Q2 in entry.message and entry.severity == "warning"
