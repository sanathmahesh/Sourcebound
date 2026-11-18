"""End-to-end engine tests on facts captured from real EDGAR responses (17 November 2026).

Every expected figure below was read directly from the captured JSON in tests/fixtures/edgar/, not from
the engine, and carries the accession number of the filing that reported it. Values are in USD.
These tests pin the behaviour of the chains in config/concepts.yaml as revised and approved on
17 November 2026 (decision D18): finance-lease liabilities count as debt, balance-sheet components are
preferred for total debt, Verizon's capex tag is in the chain, and total revenue ranks first.
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


def test_wmt_interest_includes_finance_lease_interest(wmt):
    fy0 = wmt.values["interest_expense"]["FY0"]
    # InterestExpenseDebt 2,318 + FinanceLeaseInterestExpense 383, both accn 0000104169-26-000055
    assert (fy0.value, fy0.fallback_rank) == ((2_318 + 383) * M, 3)
    ltm = wmt.values["interest_expense"]["LTM"]
    # Debt interest: 2,318 (0000104169-26-000055) + 711 - 1,170 (both 0000104169-26-000154)
    # Lease interest: 383 (0000104169-26-000055) + 251 - 236 (both 0000104169-26-000154)
    assert ltm.value == ((2_318 + 711 - 1_170) + (383 + 251 - 236)) * M
    assert {i.tag for i in ltm.inputs} == {"InterestExpenseDebt", "FinanceLeaseInterestExpense"}


def test_wmt_ltm_cfo(wmt):
    cfo = wmt.values["cfo"]["LTM"]
    # 41,565 (0000104169-26-000055) + 19,710 (0000104169-26-000154) - 18,352 (0000104169-26-000154)
    assert cfo.value == (41_565 + 19_710 - 18_352) * M


def test_wmt_total_debt_includes_short_term_borrowings_and_finance_leases(wmt):
    debt = wmt.values["total_debt"]["FY0"]
    # LongTermDebtNoncurrent 34,624 + LongTermDebtCurrent 3,542 + ShortTermBorrowings 6,596
    # + FinanceLeaseLiabilityCurrent 856 + FinanceLeaseLiabilityNoncurrent 5,905, all accn 0000104169-26-000154
    assert (debt.value, debt.fallback_rank) == ((34_624 + 3_542 + 6_596 + 856 + 5_905) * M, 1)
    ltm = wmt.values["total_debt"]["LTM"]
    # At 31 Jul 2026, all accn 0000104169-26-000154: 36,462 + 3,470 + 10,479 + 880 + 5,952
    assert (ltm.value, ltm.fallback_rank) == ((36_462 + 3_470 + 10_479 + 880 + 5_952) * M, 1)


def test_wmt_reconciliation_still_flags_the_narrow_combined_tag(wmt):
    """DebtLongtermAndShorttermCombinedAmount (now rank 5) is 38,166 at FY0 (accn 0000104169-26-000154):
    long-term debt only. The check keeps showing the gap to the reviewer."""
    warnings = [
        e
        for e in wmt.log
        if e.kind == "reconciliation" and e.severity == "warning" and e.concept == "total_debt" and e.period == "FY0"
    ]
    assert any("38,166" in e.message for e in warnings)


# ----- Verizon: December year-end ------------------------------------------------------------------


@pytest.fixture(scope="module")
def vz(specs):
    return analyse("VZ", specs)


def test_vz_fy0_debt(vz):
    debt = vz.values["total_debt"]["FY0"]
    # LongTermDebtAndCapitalLeaseObligations 139,532 (accn 0000732712-26-000052)
    # + DebtCurrent 18,618 (accn 0000732712-26-000007)
    assert (debt.value, debt.fallback_rank) == ((139_532 + 18_618) * M, 2)


def test_vz_ltm_debt(vz):
    debt = vz.values["total_debt"]["LTM"]
    # At 30 Sep 2026, accn 0000732712-26-000052: LongTermDebtAndCapitalLeaseObligations 142,344
    # + LongTermDebtCurrent 23,889 (Verizon's whole "debt maturing within one year" line)
    assert (debt.value, debt.fallback_rank) == ((142_344 + 23_889) * M, 2)
    assert vz.ratios["debt_to_ebitda"]["LTM"].status == "ok"


def test_vz_capex(vz):
    fy0 = vz.values["capex"]["FY0"]
    # PaymentsToAcquireOtherProductiveAssets 17,011, accn 0000732712-26-000007
    assert (fy0.value, fy0.fallback_rank) == (17_011 * M, 4)
    ltm = vz.values["capex"]["LTM"]
    # 17,011 (0000732712-26-000007) + 11,926 (0000732712-26-000052) - 12,263 (0000732712-26-000052)
    assert ltm.value == (17_011 + 11_926 - 12_263) * M
    assert vz.ratios["fcf_to_debt"]["FY0"].status == "ok"


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
    # LongTermDebtAndCapitalLeaseObligations 5,328 + DebtCurrent 870 (both latest in accn 0001628280-26-070703)
    assert (debt.value, debt.fallback_rank) == ((5_328 + 870) * M, 2)
    ebitda = (-133 + 445 + 1_045) * M  # operating income (derived) + D&A, accn 0001628280-26-006708
    assert gt.ratios["ebitda"]["FY0"].value == ebitda
    assert gt.ratios["debt_to_ebitda"]["FY0"].value == pytest.approx(6_198 * M / ebitda)
    assert gt.ratios["interest_coverage"]["FY0"].value == pytest.approx(ebitda / (445 * M))
    # cfo 796 - capex 826, accn 0001628280-26-006708
    assert gt.ratios["fcf_to_debt"]["FY0"].value == pytest.approx((796 - 826) / 6_198 * 100)
    # cash 801 (accn 0001628280-26-070703); no short-term investments tag, assumed zero
    assert gt.ratios["net_leverage"]["FY0"].value == pytest.approx((6_198 - 801) * M / ebitda)
    assert gt.values["short_term_investments"]["FY0"].status == "assumed_zero"


def test_gt_ltm_debt(gt):
    debt = gt.values["total_debt"]["LTM"]
    # At 30 Sep 2026, accn 0001628280-26-070703: LongTermDebtAndCapitalLeaseObligations 6,030 + DebtCurrent 1,339
    assert (debt.value, debt.fallback_rank) == ((6_030 + 1_339) * M, 2)


def test_gt_ltm_cfo_with_negative_year_to_date(gt):
    cfo = gt.values["cfo"]["LTM"]
    # 796 (0001628280-26-006708) + (-764) (0001628280-26-070703) - (-716) (0001628280-26-070703)
    assert cfo.value == (796 - 764 + 716) * M


# ----- phase 2: liquidity, ladder, trends (values read from the captured JSON) ---------------------------


def test_wmt_liquidity_coverage_fy0(wmt):
    # sources: cash 10,727 (0000104169-26-000154) + no short-term investments or revolver tagged (assumed zero)
    #          + cfo 41,565 (0000104169-26-000055)
    # uses: short-term debt 3,542 + 6,596 (0000104169-26-000154) + capex 26,642 + dividends 7,507
    #       (both 0000104169-26-000055; dividends via PaymentsOfDividendsCommonStock)
    liquidity = wmt.ratios["liquidity_coverage"]["FY0"]
    assert liquidity.value == pytest.approx((10_727 + 41_565) / (3_542 + 6_596 + 26_642 + 7_507))
    assert wmt.values["undrawn_revolver"]["FY0"].status == "assumed_zero"


def test_vz_ladder_and_near_term_cover(vz):
    ladder = vz.ladder
    # Maturity table, all accn 0000732712-26-000007
    assert [b.value / M for b in ladder.buckets] == [17_267, 9_569, 13_032, 8_115, 11_081, 96_753]
    assert ladder.total == 155_817 * M
    metrics = {m.metric_id: m for m in ladder.metrics}
    # Debt due in 24 months: DebtCurrent 18,618 + year 2 9,569 (both 0000732712-26-000007)
    assert metrics["debt_due_24m"].value == (18_618 + 9_569) * M
    # Over cash 19,048 (0000732712-26-000052) + undrawn revolver 13,657 (0000732712-26-000007)
    assert metrics["near_term_maturity_cover"].value == pytest.approx((18_618 + 9_569) / (19_048 + 13_657))
    # Ladder 155,817 + short-term borrowings 441 + finance leases 943 + 1,568 is within 5% of total debt 158,150
    assert not [e for e in vz.log if e.subject == "maturity_ladder" and e.severity == "warning"]


def test_gt_ladder_incomplete_without_after_year_five(gt):
    """Goodyear tags years 1-5 (accn 0001628280-26-006708) but not 'after year five', so the ladder total
    and its reconciliation are not available; the 24-month metrics still are."""
    assert gt.ladder.total is None
    assert gt.values["maturity_after_year_5"]["FY0"].status == "not_available"
    metrics = {m.metric_id: m for m in gt.ladder.metrics}
    # DebtCurrent 870 (0001628280-26-070703) + year 2 1,035; over cash 801, no revolver tagged
    assert metrics["near_term_maturity_cover"].value == pytest.approx((870 + 1_035) / 801)
    assert any(e.subject == "maturity_ladder" and "incomplete" in e.message for e in gt.log)


def test_trends_cover_all_five_ratios(gt):
    trend_ids = [t.metric_id for t in gt.trends]
    assert trend_ids == ["debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "liquidity_coverage"]
    assert all(set(t.values) == {"FY-2", "FY-1", "FY0", "LTM"} for t in gt.trends)


def test_gt_scorecard_latest_hand_computed(gt):
    """Bands from ratios computed by hand from the captured facts ($m):
    LTM debt 6,030 + 1,339 = 7,369; LTM EBITDA = (-388 pre-tax + 415 interest) + 963 D&A = 990
      debt / EBITDA 7.44x -> 6; net (7,369 - 812) / 990 = 6.62x -> 6; coverage 990 / 415 = 2.39x -> 5
      FCF / debt (748 - 658) / 7,369 = 1.2% -> 5; liquidity (812 + 748) / (1,339 + 658) = 0.78x -> 6
    FY0 near-term cover (870 + 1,035) / 801 = 2.38x -> 6
    Weighted: 0.2*6 + 0.1*6 + 0.25*5 + 0.2*5 + 0.15*6 + 0.1*6 = 5.55 -> SB-6."""
    from sourcebound.paths import CONFIG_DIR
    from sourcebound.scorecard.grid import load_grid
    from sourcebound.scorecard.scoring import score_company

    card = score_company(load_grid(CONFIG_DIR / "grid.yaml"), gt, basis="latest")
    assert {f.id: f.band for f in card.factors} == {
        "debt_to_ebitda": 6, "net_leverage": 6, "interest_coverage": 5,
        "fcf_to_debt": 5, "liquidity_coverage": 6, "near_term_maturity_cover": 6,
    }
    assert {f.id: f.period for f in card.factors}["near_term_maturity_cover"] == "FY0"
    assert card.weighted_score == pytest.approx(5.55)
    assert (card.grade, card.provisional, card.ig_like) == ("SB-6", False, False)
