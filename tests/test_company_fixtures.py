"""End-to-end engine tests on facts captured from real EDGAR responses (17 November 2026).

Every expected figure below was read directly from the captured JSON in tests/fixtures/edgar/, not from
the engine, and carries the accession number of the filing that reported it. Values are in USD.
These tests pin the behaviour of the chains in config/concepts.yaml as first written; where a test pins a
known weakness of a chain (marked CHAIN ISSUE), changing the chain needs the author's approval and an
update here.
"""

from datetime import date

import pytest

from sourcebound.engine.analysis import analyse_company
from sourcebound.engine.concepts import load_concepts
from sourcebound.engine.periods import Window
from sourcebound.paths import CONFIG_DIR
from tests.helpers import load_fixture

M = 1_000_000


@pytest.fixture(scope="module")
def specs():
    return load_concepts(CONFIG_DIR / "concepts.yaml")


def analyse(ticker: str, specs):
    return analyse_company(
        ticker,
        load_fixture(f"companyfacts_{ticker}.json"),
        load_fixture(f"submissions_{ticker}.json"),
        specs,
    )


def accessions(resolved) -> list[str]:
    return [i.accession for i in resolved.inputs]


# ----- Walmart: January year-end, latest 10-Q is Q2 -------------------------------------------------


@pytest.fixture(scope="module")
def wmt(specs):
    return analyse("WMT", specs)


def test_wmt_periods(wmt):
    assert wmt.latest_10k.accession == "0000104169-26-000055"
    assert wmt.latest_10q.accession == "0000104169-26-000154"
    assert wmt.period_problems == []
    assert wmt.periods["FY0"].parts[0].window == Window(date(2025, 2, 1), date(2026, 1, 31))
    assert wmt.periods["FY-1"].parts[0].window == Window(date(2024, 2, 1), date(2025, 1, 31))
    assert wmt.periods["FY-2"].parts[0].window == Window(date(2023, 2, 1), date(2024, 1, 31))
    ltm = wmt.periods["LTM"]
    assert ltm.end == date(2026, 7, 31)
    assert [p.window for p in ltm.parts[1:]] == [
        Window(date(2026, 2, 1), date(2026, 7, 31)),
        Window(date(2025, 2, 1), date(2025, 7, 31)),
    ]


def test_wmt_fy0_flows(wmt):
    op = wmt.values["operating_income"]["FY0"]
    assert (op.value, op.fallback_rank) == (29_825 * M, 1)  # accn 0000104169-26-000055
    assert accessions(op) == ["0000104169-26-000055"]
    da = wmt.values["d_and_a"]["FY0"]
    assert (da.value, da.candidate) == (14_203 * M, "DepreciationAmortizationAndAccretionNet")  # 0000104169-26-000055
    assert da.fallback_rank == 3


def test_wmt_ltm_interest_and_cfo(wmt):
    interest = wmt.values["interest_expense"]["LTM"]
    # 2,318 (FY0, 0000104169-26-000055) + 711 (YTD, 0000104169-26-000154) - 1,170 (prior YTD, 0000104169-26-000154)
    assert interest.value == (2_318 + 711 - 1_170) * M
    assert interest.candidate == "InterestExpenseDebt"
    assert accessions(interest) == ["0000104169-26-000055", "0000104169-26-000154", "0000104169-26-000154"]
    cfo = wmt.values["cfo"]["LTM"]
    # 41,565 (0000104169-26-000055) + 19,710 (0000104169-26-000154) - 18,352 (0000104169-26-000154)
    assert cfo.value == (41_565 + 19_710 - 18_352) * M


def test_wmt_total_debt_rank_one_excludes_short_term_borrowings(wmt):
    """CHAIN ISSUE: rank 1 DebtLongtermAndShorttermCombinedAmount equals Walmart's long-term debt including
    the current portion, but not its short-term borrowings. The reconciliation check must flag it."""
    debt = wmt.values["total_debt"]["FY0"]
    assert (debt.value, debt.fallback_rank) == (38_166 * M, 1)  # accn 0000104169-26-000154
    # Rank 2 would be 34,624 + 3,542 + 6,596 = 44,762 (accn 0000104169-26-000154), 14.7% higher.
    warnings = [
        e
        for e in wmt.log
        if e.kind == "reconciliation" and e.severity == "warning" and e.concept == "total_debt" and e.period == "FY0"
    ]
    assert any("44,762" in e.message for e in warnings)


# ----- Verizon: December year-end ------------------------------------------------------------------


@pytest.fixture(scope="module")
def vz(specs):
    return analyse("VZ", specs)


def test_vz_fy0_debt(vz):
    debt = vz.values["total_debt"]["FY0"]
    assert (debt.value, debt.fallback_rank) == (158_150 * M, 1)  # accn 0000732712-26-000007


def test_vz_ltm_debt_not_available_under_current_chain(vz):
    """CHAIN ISSUE: at 30 Sep 2026 Verizon tags LongTermDebtCurrent and LongTermDebtAndCapitalLeaseObligations,
    a pair no current candidate covers. Reported as not available, never estimated."""
    debt = vz.values["total_debt"]["LTM"]
    assert debt.status == "not_available"
    assert vz.ratios["debt_to_ebitda"]["LTM"].status == "not_available"


def test_vz_capex_not_available_under_current_chain(vz):
    """CHAIN ISSUE: Verizon tags capital expenditure as PaymentsToAcquireOtherProductiveAssets."""
    assert vz.values["capex"]["FY0"].status == "not_available"
    assert vz.ratios["fcf_to_debt"]["FY0"].status == "not_available"


def test_vz_interest_tag_changes_between_years(vz):
    fy2 = vz.values["interest_expense"]["FY-2"]
    assert (fy2.value, fy2.candidate) == (5_524 * M, "InterestExpense")  # accn 0000732712-24-000010
    fy0 = vz.values["interest_expense"]["FY0"]
    assert (fy0.value, fy0.candidate) == (6_694 * M, "InterestExpenseNonoperating")  # accn 0000732712-26-000007
    assert any(e.kind == "mixed_ranks" and e.concept == "interest_expense" for e in vz.log)


def test_vz_ltm_operating_income(vz):
    op = vz.values["operating_income"]["LTM"]
    # 29,259 (0000732712-26-000007) + 24,071 (0000732712-26-000052) - 24,255 (0000732712-26-000052)
    assert op.value == (29_259 + 24_071 - 24_255) * M


# ----- Goodyear: no operating-income line, a restatement --------------------------------------------


@pytest.fixture(scope="module")
def gt(specs):
    return analyse("GT", specs)


def test_gt_operating_income_is_derived(gt):
    op = gt.values["operating_income"]["FY0"]
    # pre-tax income -133 + interest expense 445, both accn 0001628280-26-006708
    assert (op.value, op.fallback_rank) == ((-133 + 445) * M, 2)
    assert any("derived" in f for f in op.flags)
    assert set(accessions(op)) == {"0001628280-26-006708"}


def test_gt_restatement_uses_latest_filing_and_is_logged(gt):
    op = gt.values["operating_income"]["FY-1"]
    # FY2024 pre-tax income: 155 in accn 0000950170-25-020763, restated to 130 in accn 0001628280-26-006708.
    # FY2024 interest expense: 522 under rank 1 InterestExpense, accn 0000950170-25-020763.
    assert op.value == (130 + 522) * M
    restated = [e for e in gt.log if e.kind == "restated" and e.period == "FY-1"]
    assert restated and "0000950170-25-020763" in restated[0].message


def test_gt_total_debt_and_ratios_fy0(gt):
    debt = gt.values["total_debt"]["FY0"]
    # LongTermDebt 5,431 + ShortTermBorrowings 506 (both latest in accn 0001628280-26-070703)
    assert (debt.value, debt.fallback_rank) == ((5_431 + 506) * M, 3)
    ebitda = (-133 + 445 + 1_045) * M  # operating income (derived) + D&A, accn 0001628280-26-006708
    assert gt.ratios["ebitda"]["FY0"].value == ebitda
    assert gt.ratios["debt_to_ebitda"]["FY0"].value == pytest.approx((5_431 + 506) * M / ebitda)
    assert gt.ratios["interest_coverage"]["FY0"].value == pytest.approx(ebitda / (445 * M))
    # cfo 796 - capex 826, accn 0001628280-26-006708
    assert gt.ratios["fcf_to_debt"]["FY0"].value == pytest.approx((796 - 826) / (5_431 + 506) * 100)
    # cash 801 (accn 0001628280-26-070703); no short-term investments tag, assumed zero
    assert gt.ratios["net_leverage"]["FY0"].value == pytest.approx((5_937 - 801) * M / ebitda)
    assert gt.values["short_term_investments"]["FY0"].status == "assumed_zero"


def test_gt_ltm_cfo_with_negative_year_to_date(gt):
    cfo = gt.values["cfo"]["LTM"]
    # 796 (0001628280-26-006708) + (-764) (0001628280-26-070703) - (-716) (0001628280-26-070703)
    assert cfo.value == (796 - 764 + 716) * M
