"""Watchlist flags (PLAN.md 4.10): latest LTM against the prior fiscal year-end, at every threshold."""

import pytest

from sourcebound.watchlist.flags import (
    coverage_down,
    grade_change,
    leverage_up,
    liquidity_shortfall,
    near_term_maturities,
)


@pytest.mark.parametrize(
    "fy0,ltm,band_fy0,band_ltm,flagged",
    [
        (2.0, 2.5, 3, 3, True),  # up exactly 0.5x
        (2.0, 2.49, 3, 3, False),
        (2.0, 2.3, 3, 4, True),  # a worse band even though up less than 0.5x
        (3.0, 2.0, 4, 3, False),  # improved
        (2.0, None, 3, 6, True),  # EBITDA turned negative: no value but band 6
    ],
)
def test_leverage_up(fy0, ltm, band_fy0, band_ltm, flagged):
    assert (leverage_up(fy0, ltm, band_fy0, band_ltm) is not None) is flagged


@pytest.mark.parametrize(
    "fy0,ltm,band_fy0,band_ltm,flagged",
    [
        (10.0, 8.0, 2, 2, True),  # down exactly 20%
        (10.0, 8.01, 2, 2, False),
        (10.0, 9.5, 2, 3, True),  # worse band
        (10.0, 12.0, 2, 2, False),
    ],
)
def test_coverage_down(fy0, ltm, band_fy0, band_ltm, flagged):
    assert (coverage_down(fy0, ltm, band_fy0, band_ltm) is not None) is flagged


@pytest.mark.parametrize("value,severity", [(1.25, None), (1.2, None), (1.19, "warning"), (1.0, "warning"),
                                            (0.99, "alert"), (None, None)])
def test_liquidity_shortfall(value, severity):
    flag = liquidity_shortfall(value)
    assert (flag.severity if flag else None) == severity


@pytest.mark.parametrize("due,resources,severity", [(50, 100, None), (51, 100, "warning"), (100, 100, "warning"),
                                                     (101, 100, "alert"), (10, 0, "alert"), (0, 0, None)])
def test_near_term_maturities(due, resources, severity):
    flag = near_term_maturities(due, resources)
    assert (flag.severity if flag else None) == severity


@pytest.mark.parametrize("fy0,latest,flagged", [("SB-3", "SB-4", True), ("SB-4", "SB-3", False), ("SB-3", "SB-3", False),
                                                (None, "SB-4", False)])
def test_grade_change(fy0, latest, flagged):
    assert (grade_change(fy0, latest) is not None) is flagged


def test_flag_records_rule_and_values():
    flag = leverage_up(2.0, 2.6, 3, 4)
    assert (flag.type, flag.metric_id, flag.from_value, flag.to_value) == ("leverage_up", "debt_to_ebitda", "2.00x", "2.60x")
    assert "0.5x" in flag.rule
