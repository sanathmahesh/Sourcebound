"""The phase-1 ratio report and the tag-discovery report, rendered from captured fixtures."""

from datetime import date

import pytest

from sourcebound.engine.analysis import analyse_company
from sourcebound.engine.concepts import load_concepts
from sourcebound.paths import CONFIG_DIR
from sourcebound.pipeline.ratio_report import render_ratio_report
from sourcebound.pipeline.tag_discovery import discover_tags, render_tag_discovery
from tests.helpers import load_fixture


@pytest.fixture(scope="module")
def gt():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    return analyse_company("GT", load_fixture("companyfacts_GT.json"), load_fixture("submissions_GT.json"), specs)


def test_ratio_report_puts_facts_directly_beneath_each_ratio(gt):
    text = render_ratio_report(gt)
    block = text.split("### Debt / EBITDA — FY0")[1].split("### ")[0]
    lines = [line for line in block.splitlines() if line.strip()]
    assert lines[0].startswith("**Formula:** total_debt / EBITDA")
    table = "\n".join(lines[1:])
    for expected in ["LongTermDebt", "ShortTermBorrowings", "DepreciationDepletionAndAmortization", "0001628280-26-070703", "https://www.sec.gov/Archives/edgar/data/42582/"]:
        assert expected in table


def test_ratio_report_shows_all_three_ltm_facts(gt):
    text = render_ratio_report(gt)
    block = text.split("### EBITDA / interest — LTM")[1].split("### ")[0]
    assert "current year-to-date" in block and "prior-year year-to-date" in block
    assert "0001628280-26-070703" in block and "0001628280-26-006708" in block


def test_ratio_report_lists_every_ratio_and_period(gt):
    text = render_ratio_report(gt)
    for ratio in ["Debt / EBITDA", "Net leverage", "EBITDA / interest", "FCF / debt"]:
        for period in ["FY-2", "FY-1", "FY0", "LTM"]:
            assert f"### {ratio} — {period}" in text


def test_ratio_report_includes_log_sections(gt):
    text = render_ratio_report(gt)
    assert "## Fallback log" in text
    assert "derived" in text
    assert "restated" in text.lower()


def test_tag_discovery_marks_reported_and_missing_tags(gt):
    rows = discover_tags(gt)
    by_tag = {(r.concept, r.tag): r for r in rows}
    # GT reported InterestExpense until Q1 2025, then switched to InterestExpenseNonoperating.
    old_tag = by_tag[("interest_expense", "InterestExpense")]
    assert old_tag.latest_end == date(2025, 3, 31)
    assert old_tag.periods["FY-1"] is True and old_tag.periods["FY0"] is False
    assert by_tag[("operating_income", "OperatingIncomeLoss")].periods["FY0"] is False
    assert by_tag[("d_and_a", "DepreciationDepletionAndAmortization")].periods["FY0"] is True
    assert by_tag[("cash", "CashAndCashEquivalentsAtCarryingValue")].periods["LTM"] is True
    assert by_tag[("short_term_investments", "ShortTermInvestments")].fact_count == 0
    text = render_tag_discovery([gt], related={})
    assert "## GT" in text
