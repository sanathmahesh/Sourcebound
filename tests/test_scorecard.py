"""The stylized scorecard: bands, weights, renormalisation, grades, and isolation from agency ratings."""

import builtins
from pathlib import Path

import pytest
from hypothesis import given
from hypothesis import strategies as st

from sourcebound.engine.ratios import (
    EBITDA_NOT_POSITIVE,
    INTEREST_NOT_POSITIVE,
    NO_DEBT,
    NO_LIQUID_RESOURCES,
    NO_USES,
    Ratio,
)
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.scorecard.grid import load_grid, parse_grid
from sourcebound.scorecard.scoring import band_for, grade_for, score

GRID = load_grid(CONFIG_DIR / "grid.yaml")
FACTORS = {f.id: f for f in GRID.factors}


def metric(metric_id: str, value, status: str = "ok", reason: str = "", period: str = "LTM") -> Ratio:
    return Ratio(metric_id, metric_id, period, value, "x", status, "", reason, [])


# ----- the grid itself ---------------------------------------------------------------------------------


def test_weights_sum_to_one():
    assert sum(f.weight for f in GRID.factors) == pytest.approx(1.0)


def test_grid_matches_the_plan():
    assert [(f.id, f.weight) for f in GRID.factors] == [
        ("debt_to_ebitda", 0.20),
        ("net_leverage", 0.10),
        ("interest_coverage", 0.25),
        ("fcf_to_debt", 0.20),
        ("liquidity_coverage", 0.15),
        ("near_term_maturity_cover", 0.10),
    ]
    assert FACTORS["debt_to_ebitda"].thresholds == (1.0, 2.0, 3.0, 4.5, 6.5)
    assert FACTORS["net_leverage"].thresholds == (0.5, 1.5, 2.5, 4.0, 6.0)
    assert FACTORS["interest_coverage"].thresholds == (15, 10, 6, 3.5, 2)
    assert FACTORS["fcf_to_debt"].thresholds == (40, 25, 15, 8, 0)
    assert FACTORS["liquidity_coverage"].thresholds == (2.5, 2.0, 1.5, 1.2, 1.0)
    assert FACTORS["near_term_maturity_cover"].thresholds == (0.25, 0.5, 0.75, 1.0, 1.5)
    assert GRID.tie_rule == "worse"


def test_grid_rejects_weights_not_summing_to_one():
    raw = {
        "version": "t", "tie_rule": "worse", "ig_like_max": 3.5,
        "grades": [[1.5, "SB-1"], [2.5, "SB-2"], [3.5, "SB-3"], [4.5, "SB-4"], [5.5, "SB-5"]], "worst_grade": "SB-6",
        "factors": [{"id": "a", "label": "A", "weight": 0.5, "higher_is_better": False, "thresholds": [1, 2, 3, 4, 5]}],
    }
    with pytest.raises(ValueError, match="weights"):
        parse_grid(raw)


def test_grid_rejects_thresholds_in_the_wrong_order():
    raw = {
        "version": "t", "tie_rule": "worse", "ig_like_max": 3.5,
        "grades": [[1.5, "SB-1"], [2.5, "SB-2"], [3.5, "SB-3"], [4.5, "SB-4"], [5.5, "SB-5"]], "worst_grade": "SB-6",
        "factors": [{"id": "a", "label": "A", "weight": 1.0, "higher_is_better": True, "thresholds": [1, 2, 3, 4, 5]}],
    }
    with pytest.raises(ValueError, match="thresholds"):
        parse_grid(raw)


# ----- every band boundary -----------------------------------------------------------------------------

EPS = 1e-9


@pytest.mark.parametrize("factor_id", list(FACTORS))
def test_every_band_boundary(factor_id):
    """Just on the better side of threshold i scores i+1; exactly on it (tie rule: worse) or past it, i+2."""
    factor = FACTORS[factor_id]
    step = EPS if factor.higher_is_better else -EPS  # a small move towards the better side
    for i, t in enumerate(factor.thresholds):
        assert band_for(factor, t + step) == i + 1, (factor_id, t)
        assert band_for(factor, t) == i + 2, (factor_id, t)
        assert band_for(factor, t - step) == i + 2, (factor_id, t)


@pytest.mark.parametrize(
    "factor_id,value,expected",
    [
        ("debt_to_ebitda", 0.5, 1), ("debt_to_ebitda", 1.5, 2), ("debt_to_ebitda", 3.7, 4), ("debt_to_ebitda", 9, 6),
        ("net_leverage", 0.3, 1), ("net_leverage", 3.0, 4), ("net_leverage", 7, 6),
        ("interest_coverage", 20, 1), ("interest_coverage", 12, 2), ("interest_coverage", 4, 4), ("interest_coverage", 1.5, 6),
        ("fcf_to_debt", 45, 1), ("fcf_to_debt", 30, 2), ("fcf_to_debt", 5, 5), ("fcf_to_debt", -5, 6),
        ("liquidity_coverage", 3, 1), ("liquidity_coverage", 1.3, 4), ("liquidity_coverage", 0.8, 6),
        ("near_term_maturity_cover", 0.1, 1), ("near_term_maturity_cover", 0.9, 4), ("near_term_maturity_cover", 2, 6),
    ],
)
def test_band_examples_from_the_plan(factor_id, value, expected):
    assert band_for(FACTORS[factor_id], value) == expected


@pytest.mark.parametrize("factor_id", list(FACTORS))
@given(a=st.floats(-100, 100, allow_nan=False), b=st.floats(-100, 100, allow_nan=False))
def test_worse_ratio_never_earns_a_better_score(factor_id, a, b):
    factor = FACTORS[factor_id]
    worse, better = (min(a, b), max(a, b)) if factor.higher_is_better else (max(a, b), min(a, b))
    assert band_for(factor, worse) >= band_for(factor, better)


# ----- statuses, renormalisation, grades -------------------------------------------------------------


def full_metrics(**changes) -> dict[str, Ratio]:
    base = {
        "debt_to_ebitda": metric("debt_to_ebitda", 2.5),  # band 3
        "net_leverage": metric("net_leverage", 2.0),  # band 3
        "interest_coverage": metric("interest_coverage", 8),  # band 3
        "fcf_to_debt": metric("fcf_to_debt", 20),  # band 3
        "liquidity_coverage": metric("liquidity_coverage", 1.8),  # band 3
        "near_term_maturity_cover": metric("near_term_maturity_cover", 0.6, period="FY0"),  # band 3
    }
    base.update(changes)
    return base


def test_all_band_three_gives_sb3_and_ig_like():
    card = score(GRID, full_metrics(), zero_debt=False, basis="latest")
    assert card.weighted_score == pytest.approx(3.0)
    assert (card.grade, card.provisional, card.ig_like) == ("SB-3", False, True)


def test_missing_factor_renormalises_and_marks_provisional():
    metrics = full_metrics(interest_coverage=metric("interest_coverage", None, "not_available", "no value"),
                           debt_to_ebitda=metric("debt_to_ebitda", 9))  # band 6
    card = score(GRID, metrics, zero_debt=False, basis="latest")
    # (0.20*6 + 0.10*3 + 0.20*3 + 0.15*3 + 0.10*3) / 0.75
    assert card.weighted_score == pytest.approx((1.2 + 0.3 + 0.6 + 0.45 + 0.3) / 0.75)
    assert card.provisional
    factor = {f.id: f for f in card.factors}["interest_coverage"]
    assert factor.band is None and factor.effective_weight is None


def test_not_meaningful_statuses_map_to_fixed_bands():
    metrics = full_metrics(
        debt_to_ebitda=metric("debt_to_ebitda", None, "not_meaningful", EBITDA_NOT_POSITIVE),
        net_leverage=metric("net_leverage", None, "not_meaningful", EBITDA_NOT_POSITIVE),
        interest_coverage=metric("interest_coverage", None, "not_meaningful", EBITDA_NOT_POSITIVE),
        liquidity_coverage=metric("liquidity_coverage", None, "not_meaningful", NO_USES),
        near_term_maturity_cover=metric("near_term_maturity_cover", None, "not_meaningful", NO_LIQUID_RESOURCES),
    )
    bands = {f.id: f.band for f in score(GRID, metrics, zero_debt=False, basis="latest").factors}
    assert bands == {"debt_to_ebitda": 6, "net_leverage": 6, "interest_coverage": 6, "fcf_to_debt": 3,
                     "liquidity_coverage": 1, "near_term_maturity_cover": 6}


def test_net_cash_scores_one():
    card = score(GRID, full_metrics(net_leverage=metric("net_leverage", -0.4, "net_cash")), zero_debt=False, basis="latest")
    assert {f.id: f.band for f in card.factors}["net_leverage"] == 1


def test_zero_debt_scores_one_on_debt_related_factors():
    metrics = full_metrics(
        debt_to_ebitda=metric("debt_to_ebitda", 0.0, "ok", NO_DEBT),
        fcf_to_debt=metric("fcf_to_debt", None, "not_meaningful", NO_DEBT),
        interest_coverage=metric("interest_coverage", None, "not_meaningful", INTEREST_NOT_POSITIVE),
    )
    bands = {f.id: f.band for f in score(GRID, metrics, zero_debt=True, basis="latest").factors}
    assert bands["debt_to_ebitda"] == bands["fcf_to_debt"] == bands["interest_coverage"] == 1
    assert bands["liquidity_coverage"] == 3  # not debt-related


def test_no_interest_with_debt_outstanding_is_not_available():
    metrics = full_metrics(interest_coverage=metric("interest_coverage", None, "not_meaningful", INTEREST_NOT_POSITIVE))
    card = score(GRID, metrics, zero_debt=False, basis="latest")
    assert {f.id: f.band for f in card.factors}["interest_coverage"] is None
    assert card.provisional


@pytest.mark.parametrize(
    "weighted,grade,ig_like",
    [(1.0, "SB-1", True), (1.5, "SB-1", True), (1.51, "SB-2", True), (3.5, "SB-3", True),
     (3.51, "SB-4", False), (5.5, "SB-5", False), (5.51, "SB-6", False)],
)
def test_grade_cutoffs(weighted, grade, ig_like):
    assert grade_for(GRID, weighted) == (grade, ig_like)


# ----- the scorecard never reads agency ratings -------------------------------------------------------


def test_scorecard_source_never_mentions_the_agency_file():
    for path in (PROJECT_ROOT / "sourcebound" / "scorecard").glob("*.py"):
        assert "agency" not in path.read_text().lower(), path


def test_scoring_opens_no_agency_file(monkeypatch):
    real_open = builtins.open

    def guarded_open(file, *args, **kwargs):
        assert "agency" not in str(file).lower(), f"scorecard tried to open {file}"
        return real_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", guarded_open)
    monkeypatch.setattr(Path, "read_text", lambda self, *a, **k: guarded_open(self).read())
    grid = load_grid(CONFIG_DIR / "grid.yaml")
    score(grid, full_metrics(), zero_debt=False, basis="latest")
