"""Per-company overrides: each needs a reason and an approval date, and only config/overrides.yaml holds them."""

import pytest

from sourcebound.overrides import company_for, load_overrides, parse_overrides
from sourcebound.paths import CONFIG_DIR
from tests.helpers import load_fixture

TICKERS = load_fixture("company_tickers_subset.json")["rows"]


def test_production_overrides_load_and_carry_reasons():
    overrides = load_overrides(CONFIG_DIR / "overrides.yaml")
    xom = [o for o in overrides if o.ticker == "XOM"]
    assert len(xom) == 1
    assert xom[0].kind == "cik" and xom[0].cik == 34088
    assert "8-K12B" in xom[0].reason
    assert xom[0].approved_on == "2026-11-17"


@pytest.mark.parametrize(
    "bad",
    [
        {"ticker": "XOM", "kind": "cik", "cik": 1, "approved_on": "2026-11-17"},  # no reason
        {"ticker": "XOM", "kind": "cik", "cik": 1, "reason": "x"},  # no approval date
        {"ticker": "XOM", "kind": "rename", "reason": "x", "approved_on": "2026-11-17"},  # unknown kind
    ],
)
def test_incomplete_overrides_are_rejected(bad):
    with pytest.raises(ValueError):
        parse_overrides({"overrides": [bad]})


def test_company_lookup_without_override_uses_sec_ticker_file():
    company = company_for("VZ", TICKERS, [])
    assert company.cik == 732712  # from company_tickers.json, captured 17 Nov 2026


def test_cik_override_replaces_the_lookup():
    overrides = parse_overrides(
        {"overrides": [{"ticker": "VZ", "kind": "cik", "cik": 999, "reason": "test", "approved_on": "2026-11-17"}]}
    )
    company = company_for("VZ", TICKERS, overrides)
    assert company.cik == 999
