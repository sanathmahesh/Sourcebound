"""Fiscal-period identification and LTM window checks (synthetic facts)."""

import pytest

from sourcebound.engine.periods import Window, check_ltm_windows, find_periods, is_annual
from tests.helpers import d, fact, filing

K_ACCN = "0000000000-24-000010"
Q_ACCN = "0000000000-24-000020"


def annual_facts(windows: list[tuple[str, str]], accession: str = K_ACCN) -> list:
    """One synthetic revenue fact per annual window, all from the same 10-K."""
    return [fact("Revenues", 100.0, end=e, start=s, accession=accession) for s, e in windows]


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("2023-01-01", "2023-12-31", True),  # calendar year
        ("2024-01-01", "2024-12-31", True),  # leap calendar year
        ("2022-10-02", "2023-09-30", True),  # 52 weeks
        ("2021-09-26", "2022-10-01", True),  # 53 weeks
        ("2023-01-01", "2023-06-30", False),  # half year
        ("2022-01-01", "2023-01-31", False),  # 13 months
    ],
)
def test_is_annual(start, end, expected):
    assert is_annual(Window(d(start), d(end))) is expected


def test_december_year_end():
    facts = annual_facts([("2023-01-01", "2023-12-31"), ("2022-01-01", "2022-12-31"), ("2021-01-01", "2021-12-31")])
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    result = find_periods(facts, ten_k, None)
    assert result.problems == []
    fy0, fy1, fy2 = (result.periods[label] for label in ("FY0", "FY-1", "FY-2"))
    assert fy0.parts[0].window == Window(d("2023-01-01"), d("2023-12-31"))
    assert fy1.parts[0].window == Window(d("2022-01-01"), d("2022-12-31"))
    assert fy2.parts[0].window == Window(d("2021-01-01"), d("2021-12-31"))
    assert fy1.end == d("2022-12-31")


def test_january_year_end():
    facts = annual_facts([("2023-02-01", "2024-01-31"), ("2022-02-01", "2023-01-31"), ("2021-02-01", "2022-01-31")])
    ten_k = filing("10-K", K_ACCN, "2024-03-15", "2024-01-31")
    result = find_periods(facts, ten_k, None)
    assert result.periods["FY0"].parts[0].window == Window(d("2023-02-01"), d("2024-01-31"))
    assert result.periods["FY-2"].end == d("2022-01-31")


def test_52_53_week_years():
    facts = annual_facts([("2022-10-02", "2023-09-30"), ("2021-09-26", "2022-10-01"), ("2020-09-27", "2021-09-25")])
    ten_k = filing("10-K", K_ACCN, "2023-11-15", "2023-09-30")
    result = find_periods(facts, ten_k, None)
    assert result.problems == []
    assert result.periods["FY-1"].parts[0].window == Window(d("2021-09-26"), d("2022-10-01"))  # 53 weeks
    assert result.periods["FY-2"].end == d("2021-09-25")


def test_fiscal_years_use_dates_not_fy_fields():
    """A fact's own dates decide its period; the filing it came from does not."""
    facts = annual_facts([("2023-01-01", "2023-12-31")]) + [
        # The FY-1 window is only reported in an older 10-K.
        fact("Revenues", 90.0, start="2022-01-01", end="2022-12-31", accession="0000000000-23-000010", filed="2023-02-15"),
    ]
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    result = find_periods(facts, ten_k, None)
    assert result.periods["FY-1"].parts[0].window == Window(d("2022-01-01"), d("2022-12-31"))


def test_missing_prior_year_is_reported_not_guessed():
    facts = annual_facts([("2023-01-01", "2023-12-31")])
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    result = find_periods(facts, ten_k, None)
    assert "FY-1" not in result.periods
    assert any("FY-1" in p for p in result.problems)


def test_no_annual_window_at_report_date_is_a_problem():
    facts = annual_facts([("2022-01-01", "2022-12-31")])
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    result = find_periods(facts, ten_k, None)
    assert result.periods == {}
    assert result.problems


def ltm_facts() -> list:
    facts = annual_facts([("2023-01-01", "2023-12-31"), ("2022-01-01", "2022-12-31"), ("2021-01-01", "2021-12-31")])
    facts += [
        fact("Revenues", 60.0, start="2024-01-01", end="2024-06-30", accession=Q_ACCN, form="10-Q", filed="2024-08-01"),
        fact("Revenues", 30.0, start="2024-04-01", end="2024-06-30", accession=Q_ACCN, form="10-Q", filed="2024-08-01"),
        fact("Revenues", 50.0, start="2023-01-01", end="2023-06-30", accession=Q_ACCN, form="10-Q", filed="2024-08-01"),
        fact("Revenues", 25.0, start="2023-04-01", end="2023-06-30", accession=Q_ACCN, form="10-Q", filed="2024-08-01"),
    ]
    return facts


def test_ltm_built_from_three_windows():
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    ten_q = filing("10-Q", Q_ACCN, "2024-08-01", "2024-06-30")
    result = find_periods(ltm_facts(), ten_k, ten_q)
    assert result.problems == []
    ltm = result.periods["LTM"]
    assert ltm.end == d("2024-06-30")
    assert [(p.sign, p.window) for p in ltm.parts] == [
        (+1, Window(d("2023-01-01"), d("2023-12-31"))),
        (+1, Window(d("2024-01-01"), d("2024-06-30"))),  # current year-to-date, not the quarter
        (-1, Window(d("2023-01-01"), d("2023-06-30"))),  # prior-year year-to-date
    ]


def test_ltm_equals_fy0_when_no_newer_10q():
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    old_q = filing("10-Q", Q_ACCN, "2023-11-01", "2023-09-30")
    result = find_periods(ltm_facts(), ten_k, old_q)
    ltm = result.periods["LTM"]
    assert ltm.parts == result.periods["FY0"].parts
    assert ltm.end == d("2023-12-31")
    assert "no 10-Q" in ltm.note


def test_ltm_not_available_when_10q_has_no_matching_ytd():
    facts = annual_facts([("2023-01-01", "2023-12-31"), ("2022-01-01", "2022-12-31"), ("2021-01-01", "2021-12-31")])
    # The 10-Q only reports a quarter that does not start the day after FY0 ends.
    facts.append(fact("Revenues", 30.0, start="2024-04-01", end="2024-06-30", accession=Q_ACCN, form="10-Q", filed="2024-08-01"))
    ten_k = filing("10-K", K_ACCN, "2024-02-15", "2023-12-31")
    ten_q = filing("10-Q", Q_ACCN, "2024-08-01", "2024-06-30")
    result = find_periods(facts, ten_k, ten_q)
    assert "LTM" not in result.periods
    assert any("LTM" in p for p in result.problems)


def test_check_ltm_windows_accepts_aligned_windows():
    fy0 = Window(d("2023-01-01"), d("2023-12-31"))
    current = Window(d("2024-01-01"), d("2024-06-30"))
    prior = Window(d("2023-01-01"), d("2023-07-01"))  # 52/53-week calendars can shift a few days
    assert check_ltm_windows(fy0, current, prior) == []


def test_check_ltm_windows_rejects_misalignment():
    fy0 = Window(d("2023-01-01"), d("2023-12-31"))
    assert check_ltm_windows(fy0, Window(d("2024-02-01"), d("2024-06-30")), Window(d("2023-01-01"), d("2023-06-30")))
    assert check_ltm_windows(fy0, Window(d("2024-01-01"), d("2024-06-30")), Window(d("2023-02-01"), d("2023-06-30")))
    # Year-to-date lengths more than a week apart (six months against nine months).
    assert check_ltm_windows(fy0, Window(d("2024-01-01"), d("2024-06-30")), Window(d("2023-01-01"), d("2023-09-30")))
