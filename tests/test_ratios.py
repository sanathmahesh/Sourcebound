"""Ratio maths, including zero and negative EBITDA, zero debt and missing inputs (synthetic numbers)."""

import pytest

from sourcebound.engine.ratios import (
    compute_ratios,
    debt_to_ebitda,
    ebitda,
    fcf_to_debt,
    interest_coverage,
    net_leverage,
)
from sourcebound.engine.resolver import Resolved


def test_ebitda():
    assert ebitda(80, 20) == 100
    assert ebitda(None, 20) is None
    assert ebitda(80, None) is None


def test_debt_to_ebitda():
    r = debt_to_ebitda(250, 100)
    assert (r.value, r.status) == (2.5, "ok")


@pytest.mark.parametrize("bad_ebitda", [0, -5])
def test_leverage_and_coverage_not_meaningful_when_ebitda_not_positive(bad_ebitda):
    assert debt_to_ebitda(250, bad_ebitda).status == "not_meaningful"
    assert net_leverage(250, 10, bad_ebitda).status == "not_meaningful"
    assert interest_coverage(bad_ebitda, 10).status == "not_meaningful"
    assert debt_to_ebitda(250, bad_ebitda).value is None


def test_zero_debt():
    assert (debt_to_ebitda(0, 100).value, debt_to_ebitda(0, 100).status) == (0.0, "ok")
    assert debt_to_ebitda(0, -5).value == 0.0  # zero-debt rule takes precedence over EBITDA <= 0
    r = fcf_to_debt(50, 20, 0)
    assert r.status == "not_meaningful"
    assert "no debt" in r.reason


def test_net_leverage_and_net_cash():
    r = net_leverage(250, 50, 100)
    assert (r.value, r.status) == (2.0, "ok")
    r = net_leverage(100, 150, 100)
    assert (r.value, r.status) == (-0.5, "net_cash")
    r = net_leverage(0, 30, 100)
    assert r.status == "net_cash"
    r = net_leverage(0, 0, 100)
    assert (r.value, r.status) == (0.0, "ok")


def test_interest_coverage():
    r = interest_coverage(100, 8)
    assert (r.value, r.status) == (12.5, "ok")
    assert interest_coverage(100, 0).status == "not_meaningful"


def test_fcf_to_debt_is_a_percentage_and_can_be_negative():
    r = fcf_to_debt(cfo=60, capex=20, total_debt=200)
    assert (r.value, r.status) == (20.0, "ok")
    r = fcf_to_debt(cfo=10, capex=30, total_debt=200)
    assert (r.value, r.status) == (-10.0, "ok")


@pytest.mark.parametrize(
    "call",
    [
        lambda: debt_to_ebitda(None, 100),
        lambda: debt_to_ebitda(100, None),
        lambda: net_leverage(100, None, 50),
        lambda: interest_coverage(100, None),
        lambda: fcf_to_debt(None, 10, 100),
        lambda: fcf_to_debt(50, None, 100),
        lambda: fcf_to_debt(50, 10, None),
    ],
)
def test_missing_input_is_not_available(call):
    r = call()
    assert (r.value, r.status) == (None, "not_available")
    assert "not available" in r.reason


def resolved(concept: str, value, status: str = "ok") -> Resolved:
    return Resolved(
        concept=concept,
        label=concept,
        period="FY0",
        status=status,
        value=value,
        fallback_rank=1 if status == "ok" else None,
        candidate=concept,
        flags=[],
        inputs=[],
        reason="" if status == "ok" else "no fact",
    )


def test_compute_ratios_builds_all_four_with_formulas():
    values = {
        "operating_income": resolved("operating_income", 80),
        "d_and_a": resolved("d_and_a", 20),
        "interest_expense": resolved("interest_expense", 10),
        "total_debt": resolved("total_debt", 300),
        "cash": resolved("cash", 40),
        "short_term_investments": resolved("short_term_investments", 0, status="assumed_zero"),
        "cfo": resolved("cfo", 90),
        "capex": resolved("capex", 30),
    }
    ratios = {r.metric_id: r for r in compute_ratios(values, "FY0")}
    assert set(ratios) == {"ebitda", "debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt"}
    assert ratios["ebitda"].value == 100
    assert ratios["debt_to_ebitda"].value == 3.0
    assert ratios["net_leverage"].value == pytest.approx(2.6)
    assert ratios["interest_coverage"].value == 10.0
    assert ratios["fcf_to_debt"].value == 20.0
    assert ratios["debt_to_ebitda"].formula == "total_debt / EBITDA"
    assert ratios["net_leverage"].formula == "(total_debt - cash - short_term_investments) / EBITDA"
    # Each ratio carries the resolved inputs it used, in order.
    assert [i.concept for i in ratios["fcf_to_debt"].inputs] == ["cfo", "capex", "total_debt"]


def test_compute_ratios_propagates_not_available():
    values = {
        "operating_income": resolved("operating_income", None, status="not_available"),
        "d_and_a": resolved("d_and_a", 20),
        "interest_expense": resolved("interest_expense", 10),
        "total_debt": resolved("total_debt", 300),
        "cash": resolved("cash", 40),
        "short_term_investments": resolved("short_term_investments", 0, status="assumed_zero"),
        "cfo": resolved("cfo", 90),
        "capex": resolved("capex", None, status="not_available"),
    }
    ratios = {r.metric_id: r for r in compute_ratios(values, "FY0")}
    assert ratios["ebitda"].status == "not_available"
    assert ratios["debt_to_ebitda"].status == "not_available"
    assert "operating_income" in ratios["debt_to_ebitda"].reason
    assert ratios["fcf_to_debt"].status == "not_available"
    assert "capex" in ratios["fcf_to_debt"].reason
