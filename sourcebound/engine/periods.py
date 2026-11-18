"""Which spans of time the ratios cover: FY-2, FY-1, FY0 and LTM.

- FY0 is the fiscal year reported by the latest 10-K; FY-1 and FY-2 are the two before it.
- LTM ("last twelve months") is as of the latest 10-Q when that 10-Q is newer than the 10-K:
      LTM = FY0 + current year-to-date - prior-year year-to-date
  e.g. for a December year-end with a September 10-Q: full 2025 + Jan-Sep 2026 - Jan-Sep 2025.
  When there is no newer 10-Q, LTM is simply FY0.

Periods are identified from the facts' own start and end dates, never from the API's fy/fp fields
(those describe the filing). Many retailers use 52/53-week fiscal years that end on a weekday rather than
a month end, so "annual" means 52 weeks, 53 weeks or a calendar year, not exactly 365 days.

A Period is a balance-sheet date plus a list of signed windows for flow items (income and cash flow):
one window for a fiscal year, three for LTM.
"""

from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta

from sourcebound.edgar.facts import Fact
from sourcebound.edgar.filings import Filing

# end - start in days: 363 (52 weeks), 364/365 (calendar year), 370 (53 weeks). A little slack either side.
ANNUAL_MIN_DAYS = 360
ANNUAL_MAX_DAYS = 372
# How far apart the two year-to-date windows may be in length (a 53-week year adds a week to one quarter).
YTD_LENGTH_TOLERANCE_DAYS = 7

PERIOD_ORDER = ["FY-2", "FY-1", "FY0", "LTM"]


@dataclass(frozen=True)
class Window:
    """A span one XBRL fact can describe. start is None for a balance-sheet (instant) fact."""

    start: date | None
    end: date

    @property
    def days(self) -> int:
        return (self.end - self.start).days if self.start else 0

    def __str__(self) -> str:
        return f"{self.start} to {self.end}" if self.start else f"at {self.end}"


@dataclass(frozen=True)
class PeriodPart:
    sign: int  # +1 or -1
    window: Window
    role: str  # e.g. "FY0", "current year-to-date"


@dataclass(frozen=True)
class Period:
    label: str  # "FY-2", "FY-1", "FY0" or "LTM"
    end: date  # balance-sheet date for instant items
    parts: tuple[PeriodPart, ...]  # signed windows summed for flow items
    note: str = ""


@dataclass
class PeriodSet:
    periods: dict[str, Period]
    problems: list[str]


def is_annual(window: Window) -> bool:
    return window.start is not None and ANNUAL_MIN_DAYS <= window.days <= ANNUAL_MAX_DAYS


def duration_windows(facts: list[Fact], accession: str | None = None) -> set[Window]:
    """The distinct (start, end) windows among duration facts, optionally from one filing only."""
    return {
        Window(f.start, f.end)
        for f in facts
        if f.start is not None and (accession is None or f.accession == accession)
    }


def find_periods(facts: list[Fact], latest_10k: Filing, latest_10q: Filing | None) -> PeriodSet:
    """Identify FY0, FY-1, FY-2 and LTM. Anything that cannot be identified is listed in problems."""
    problems: list[str] = []
    periods: dict[str, Period] = {}

    fy0 = _annual_window_ending(facts, latest_10k.report_date)
    if fy0 is None:
        problems.append(
            f"FY0: no annual facts end on the latest 10-K's report date {latest_10k.report_date} "
            f"(accession {latest_10k.accession})"
        )
        return PeriodSet(periods, problems)
    periods["FY0"] = Period("FY0", fy0.end, (PeriodPart(+1, fy0, "FY0"),))

    later = fy0
    for label in ("FY-1", "FY-2"):
        window = _annual_window_ending(facts, later.start - timedelta(days=1))
        if window is None:
            problems.append(f"{label}: no annual facts end on {later.start - timedelta(days=1)}")
            break
        periods[label] = Period(label, window.end, (PeriodPart(+1, window, label),))
        later = window

    if latest_10q is None or latest_10q.report_date <= fy0.end:
        periods["LTM"] = Period("LTM", fy0.end, periods["FY0"].parts, note="no 10-Q after the latest 10-K; LTM equals FY0")
    else:
        ltm, ltm_problems = _ltm_period(facts, fy0, latest_10q)
        if ltm is None:
            problems += [f"LTM not available: {p}" for p in ltm_problems]
        else:
            periods["LTM"] = ltm
    return PeriodSet(periods, problems)


def _annual_window_ending(facts: list[Fact], end: date) -> Window | None:
    """The annual window ending on this date that most facts use, or None if no fact has one."""
    counts = Counter(
        Window(f.start, f.end) for f in facts if f.start is not None and f.end == end and is_annual(Window(f.start, f.end))
    )
    if not counts:
        return None
    return max(counts, key=lambda w: (counts[w], w.start))


def _ltm_period(facts: list[Fact], fy0: Window, ten_q: Filing) -> tuple[Period | None, list[str]]:
    """Find the 10-Q's two year-to-date windows, check they line up with FY0, and build LTM."""
    windows = [w for w in duration_windows(facts, ten_q.accession) if not is_annual(w)]
    q_end = ten_q.report_date
    current = [w for w in windows if w.end == q_end]
    prior_lo, prior_hi = q_end - timedelta(days=371), q_end - timedelta(days=357)
    prior = [w for w in windows if prior_lo <= w.end <= prior_hi]
    if not current:
        return None, [f"10-Q {ten_q.accession} has no year-to-date facts ending {q_end}"]
    if not prior:
        return None, [f"10-Q {ten_q.accession} has no prior-year year-to-date facts ending near {q_end - timedelta(days=364)}"]
    # The year-to-date window is the longest one ending on the date (the 10-Q also reports the quarter alone).
    current_ytd = max(current, key=lambda w: w.days)
    prior_ytd = max(prior, key=lambda w: w.days)
    problems = check_ltm_windows(fy0, current_ytd, prior_ytd)
    if problems:
        return None, problems
    parts = (
        PeriodPart(+1, fy0, "FY0"),
        PeriodPart(+1, current_ytd, "current year-to-date"),
        PeriodPart(-1, prior_ytd, "prior-year year-to-date"),
    )
    note = f"LTM to {q_end} = FY0 + ({current_ytd}) - ({prior_ytd}), from 10-Q {ten_q.accession}"
    return Period("LTM", q_end, parts, note=note), []


def check_ltm_windows(fy0: Window, current_ytd: Window, prior_ytd: Window) -> list[str]:
    """Check that the three LTM windows line up. Returns a list of problems; empty means they do.

    - the current year-to-date starts the day after FY0 ends;
    - the prior-year year-to-date starts the day FY0 starts;
    - the two year-to-date windows are the same length, within a week.
    """
    problems = []
    if current_ytd.start != fy0.end + timedelta(days=1):
        problems.append(f"current year-to-date starts {current_ytd.start}, expected {fy0.end + timedelta(days=1)}")
    if prior_ytd.start != fy0.start:
        problems.append(f"prior-year year-to-date starts {prior_ytd.start}, expected {fy0.start}")
    if abs(current_ytd.days - prior_ytd.days) > YTD_LENGTH_TOLERANCE_DAYS:
        problems.append(
            f"year-to-date lengths differ: {current_ytd.days} days against {prior_ytd.days} days"
        )
    return problems
