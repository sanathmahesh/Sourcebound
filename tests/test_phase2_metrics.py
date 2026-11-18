"""Liquidity coverage, the maturity ladder metrics, trends and the phase-2 warnings (synthetic numbers)."""

import pytest

from sourcebound.engine import checks
from sourcebound.engine.ladder import near_term_maturity_cover, share_due_24m
from sourcebound.engine.ratios import NO_DEBT, NO_LIQUID_RESOURCES, NO_USES, liquidity_coverage
from sourcebound.engine.trends import direction


# ----- liquidity coverage: (cash + revolver + max(cfo, 0)) / (debt due in 12 months + capex + dividends)


def test_liquidity_coverage():
    r = liquidity_coverage(cash=50, undrawn_revolver=30, cfo=120, debt_due_12m=40, capex=60, dividends=0)
    assert (r.value, r.status) == (2.0, "ok")


def test_liquidity_floors_negative_cash_from_operations_at_zero():
    r = liquidity_coverage(cash=50, undrawn_revolver=30, cfo=-500, debt_due_12m=40, capex=40, dividends=0)
    assert r.value == 1.0  # (50 + 30 + 0) / 80


def test_liquidity_with_no_uses_is_not_meaningful():
    r = liquidity_coverage(cash=50, undrawn_revolver=0, cfo=10, debt_due_12m=0, capex=0, dividends=0)
    assert (r.status, r.reason) == ("not_meaningful", NO_USES)


def test_liquidity_missing_input_is_not_available():
    assert liquidity_coverage(None, 0, 10, 0, 5, 0).status == "not_available"
    assert liquidity_coverage(10, 0, None, 0, 5, 0).status == "not_available"
    assert liquidity_coverage(10, 0, 10, 0, None, 0).status == "not_available"


# ----- maturity ladder metrics -------------------------------------------------------------------------


def test_near_term_maturity_cover():
    r = near_term_maturity_cover(debt_due_24m=30, liquid_resources=120)
    assert (r.value, r.status) == (0.25, "ok")


def test_near_term_cover_with_no_liquid_resources():
    r = near_term_maturity_cover(debt_due_24m=30, liquid_resources=0)
    assert (r.status, r.reason) == ("not_meaningful", NO_LIQUID_RESOURCES)
    assert near_term_maturity_cover(debt_due_24m=0, liquid_resources=0).value == 0.0


def test_share_due_within_24_months_is_a_percentage():
    assert share_due_24m(debt_due_24m=25, total_debt=200).value == 12.5
    r = share_due_24m(debt_due_24m=0, total_debt=0)
    assert (r.status, r.reason) == ("not_meaningful", NO_DEBT)
    assert share_due_24m(debt_due_24m=None, total_debt=100).status == "not_available"


# ----- trends ------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "start,end,higher_is_better,unit,expected",
    [
        (2.0, 3.0, False, "x", "worsening"),  # leverage up
        (3.0, 2.0, False, "x", "improving"),  # leverage down
        (2.0, 2.15, False, "x", "stable"),  # within 10% of the start
        (10.0, 6.0, True, "x", "worsening"),  # coverage down
        (20.0, 23.5, True, "%", "improving"),  # FCF / debt up 3.5 points
        (20.0, 21.5, True, "%", "stable"),  # within 2 percentage points
        (0.0, 0.05, False, "x", "stable"),  # start at zero uses the 0.1x floor
    ],
)
def test_trend_direction(start, end, higher_is_better, unit, expected):
    assert direction(start, end, higher_is_better, unit) == expected


# ----- warnings ----------------------------------------------------------------------------------------


def test_revenue_jump_over_40_percent_raises_structural_change_warning():
    entries = checks.revenue_changes({"FY-2": 100.0, "FY-1": 150.0, "FY0": 155.0})
    assert len(entries) == 1
    assert entries[0].kind == "structural_change" and entries[0].period == "FY-1"
    assert entries[0].severity == "warning"
    assert checks.revenue_changes({"FY-2": 100.0, "FY-1": 139.0, "FY0": 100.0}) == []


def test_revenue_drop_over_40_percent_also_warns():
    assert len(checks.revenue_changes({"FY-2": 100.0, "FY-1": 55.0})) == 1


def test_ladder_reconciles_with_total_debt():
    # ladder 80 + short-term borrowings 10 + finance leases 10 = 100 = total debt
    assert checks.reconcile_ladder(80, 10, 10, 100, "FY0") == []


def test_ladder_far_from_total_debt_warns():
    [entry] = checks.reconcile_ladder(60, 10, 10, 100, "FY0")
    assert entry.kind == "reconciliation" and entry.severity == "warning" and entry.subject == "maturity_ladder"


def test_incomplete_ladder_cannot_be_reconciled():
    [entry] = checks.reconcile_ladder(None, 10, 10, 100, "FY0")
    assert entry.severity == "info" and "incomplete" in entry.message


def _scope_resolver():
    from sourcebound.engine.concepts import load_concepts
    from sourcebound.engine.resolver import FactIndex, Resolver
    from sourcebound.paths import CONFIG_DIR
    from tests.helpers import fact

    facts = [fact("LongTermDebt", 120, end="2025-12-31"), fact("LongTermDebtCurrent", 10, end="2025-12-31"),
             fact("LongTermDebtNoncurrent", 100, end="2025-12-31")]  # 120 is neither 110 nor 100
    return Resolver(load_concepts(CONFIG_DIR / "concepts.yaml"), FactIndex(facts), cik=1)


def test_long_term_debt_scope_mismatch_warns_only_when_the_tag_is_used():
    from sourcebound.engine.periods import Period, PeriodPart, Window
    from tests.helpers import d

    period = Period("FY0", d("2025-12-31"), (PeriodPart(+1, Window(d("2025-01-01"), d("2025-12-31")), "FY0"),))
    resolver = _scope_resolver()
    assert checks.long_term_debt_scope(resolver, period, used=True).severity == "warning"
    assert checks.long_term_debt_scope(resolver, period, used=False).severity == "info"
