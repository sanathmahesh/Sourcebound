"""Phase-5 metric functions on hand-built cases."""

import pytest

from sourcebound.evals.metrics import (
    judge_agreement,
    matches,
    share,
    spearman,
    spread,
)
from sourcebound.evals.ratings import ig_from_rating, rating_rank


def test_share_reports_its_sample_size():
    assert share(3, 4) == {"value": 0.75, "n": 4}
    assert share(0, 0) == {"value": None, "n": 0}


@pytest.mark.parametrize(
    "kind,engine,hand,expected",
    [
        ("amount", 6_596_000_000, "6,596", True),  # millions: equal after rounding to the filing's unit
        ("amount", 6_596_400_000, "6,596", True),
        ("amount", 6_597_000_000, "6,596", False),
        ("amount", -217_000_000, "(217)", True),  # parentheses mean negative
        ("amount", 0, "0", True),
        ("ratio_x", 1.214, "1.17", True),  # within 0.05x
        ("ratio_x", 1.214, "1.16", False),
        ("ratio_pct", 23.6, "22.7%", True),  # within 1 percentage point
        ("ratio_pct", 23.6, "22.5%", False),
    ],
)
def test_pass_rule(kind, engine, hand, expected):
    assert matches(kind, engine, hand, unit=1e6) is expected


def test_judge_agreement_and_false_pass_rate():
    human = ["supported", "unsupported", "unsupported", "partially_supported", "supported"]
    judge = ["supported", "supported", "unsupported", "supported", "supported"]
    result = judge_agreement(human, judge)
    assert result["agreement"] == {"value": 0.6, "n": 5}
    # judge said supported where I said unsupported: 1 of my 2 unsupported
    assert result["false_pass_rate"] == {"value": 0.5, "n": 2}


def test_spearman_with_ties_matches_a_hand_computation():
    # ranks x: 1, 2, 3, 4 ; y: 1, 3, 2, 4  -> rho = 1 - 6*2/(4*15) = 0.8
    assert spearman([1, 2, 3, 4], [10, 30, 20, 40]) == pytest.approx(0.8)
    assert spearman([1, 2, 3], [5, 5, 5]) is None  # no variation
    assert spearman([1, 1, 2, 3], [1, 2, 3, 4]) == pytest.approx(0.9486832980505138)  # average ranks for ties


def test_spread():
    assert spread([0.8, 0.9, 1.0]) == {"mean": pytest.approx(0.9), "min": 0.8, "max": 1.0, "n": 3}


@pytest.mark.parametrize(
    "rating,rank,ig",
    [("AAA", 1, True), ("AA-", 4, True), ("BBB-", 10, True), ("BB+", 11, False), ("Aa2", 3, True),
     ("Baa3", 10, True), ("Ba1", 11, False), ("Caa1", 17, False), ("CCC+", 17, False)],
)
def test_rating_scale(rating, rank, ig):
    assert rating_rank(rating) == rank
    assert ig_from_rating(rating) is ig


def test_unknown_rating_is_an_error():
    with pytest.raises(ValueError):
        rating_rank("A++")
