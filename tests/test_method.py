"""The method page is generated from the grid and states each band's range correctly."""

from sourcebound.scorecard.grid import Factor
from sourcebound.strategy.method import band_ranges


def test_lower_is_better_ranges_put_ties_in_the_weaker_band():
    f = Factor("debt_to_ebitda", "Debt / EBITDA", 0.2, False, (1.0, 2.0, 3.0, 4.5, 6.5))
    assert band_ranges(f, "worse") == ["under 1x", "1x to under 2x", "2x to under 3x", "3x to under 4.5x",
                                       "4.5x to under 6.5x", "6.5x or more"]


def test_higher_is_better_ranges_put_ties_in_the_weaker_band():
    f = Factor("interest_coverage", "EBITDA / interest", 0.25, True, (15, 10, 6, 3.5, 2))
    assert band_ranges(f, "worse") == ["over 15x", "over 10x to 15x", "over 6x to 10x", "over 3.5x to 6x",
                                       "over 2x to 3.5x", "2x or less"]
