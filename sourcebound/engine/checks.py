"""Consistency checks that raise warnings or notes. They never change a value.

- Debt reconciliation: total debt is resolved from one candidate; every other candidate the company
  reports for the same date is computed too, and a difference over 5% is a warning. This catches a
  rank-1 tag that covers less than its name suggests.
- LongTermDebt scope: us-gaap LongTermDebt should include the current portion, but companies differ.
  When LongTermDebt, LongTermDebtCurrent and LongTermDebtNoncurrent are all reported for a date, record
  which reading the numbers support.
- Mixed ranks: a concept resolved through different tags in different periods makes trends less
  comparable, so it is noted.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.engine.periods import Period, Window
from sourcebound.engine.resolver import LogEntry, Resolved, Resolver

RECONCILIATION_TOLERANCE = 0.05  # 5%: candidates further apart than this raise a warning
SCOPE_TOLERANCE = 0.005  # 0.5%: how close LongTermDebt must be to a sum to count as equal


@dataclass(frozen=True)
class Alternative:
    rank: int
    candidate: str
    value: float | None
    failure: str


def debt_alternatives(resolver: Resolver, period: Period) -> list[Alternative]:
    """Every total_debt candidate evaluated for this period, whether or not it was the one used.

    Uses a scratch resolver, so candidates that were not used add nothing to the company's log.
    """
    scratch = Resolver(resolver.specs, resolver.index, resolver.cik)
    spec = scratch.specs["total_debt"]
    result = []
    for candidate in spec.chain:
        attempt = scratch.try_candidate(spec, candidate, period)
        value = None if attempt.failure else attempt.value
        result.append(Alternative(candidate.rank, candidate.describe(), value, attempt.failure))
    return result


def reconcile_total_debt(chosen: Resolved, alternatives: list[Alternative]) -> list[LogEntry]:
    """Warn when another reported candidate differs from the chosen total debt by more than 5%."""
    if chosen.status != "ok" or not chosen.value:
        return []
    entries = []
    for alt in alternatives:
        if alt.value is None or alt.rank == chosen.fallback_rank:
            continue
        gap = (alt.value - chosen.value) / chosen.value
        if abs(gap) > RECONCILIATION_TOLERANCE:
            entries.append(
                LogEntry(
                    "reconciliation", "total_debt", chosen.period,
                    f"total debt uses rank {chosen.fallback_rank} {chosen.candidate} = ${chosen.value / 1e6:,.0f}m, "
                    f"but rank {alt.rank} {alt.candidate} = ${alt.value / 1e6:,.0f}m ({gap:+.1%}). "
                    "Check which matches the balance sheet.",
                    "warning",
                    "total_debt",
                )
            )
    return entries


def long_term_debt_scope(resolver: Resolver, period: Period, used: bool) -> LogEntry | None:
    """Does LongTermDebt include the current portion at this date? Only answerable if all three tags exist.

    A mismatch is a warning only when total debt actually uses LongTermDebt (used=True); otherwise a note.
    """
    at = Window(None, period.end)
    values = {}
    for tag in ("LongTermDebt", "LongTermDebtCurrent", "LongTermDebtNoncurrent"):
        matches = resolver.index.matching(tag, at)
        if not matches:
            return None
        values[tag] = matches[-1].value
    total, current, noncurrent = values["LongTermDebt"], values["LongTermDebtCurrent"], values["LongTermDebtNoncurrent"]
    if abs(total - (current + noncurrent)) <= SCOPE_TOLERANCE * total:
        reading, severity = "includes the current portion (LongTermDebt = current + noncurrent)", "info"
    elif abs(total - noncurrent) <= SCOPE_TOLERANCE * total:
        reading, severity = "excludes the current portion (LongTermDebt = noncurrent)", "info"
    else:
        reading, severity = "matches neither current + noncurrent nor noncurrent alone", "warning" if used else "info"
    message = (
        f"LongTermDebt ${total / 1e6:,.0f}m {reading}; LongTermDebtCurrent ${current / 1e6:,.0f}m, "
        f"LongTermDebtNoncurrent ${noncurrent / 1e6:,.0f}m"
    )
    return LogEntry("reconciliation", "total_debt", period.label, message, severity, "LongTermDebt")


def mixed_ranks(concept: str, by_period: dict[str, Resolved]) -> LogEntry | None:
    """Note when a concept is resolved through different candidates in different periods."""
    used = {label: r for label, r in by_period.items() if r.status == "ok"}
    if len({r.candidate for r in used.values()}) <= 1:
        return None
    detail = "; ".join(f"{label}: rank {r.fallback_rank} {r.candidate}" for label, r in used.items())
    return LogEntry("mixed_ranks", concept, "all", f"different candidates across periods ({detail})", subject=concept)


STRUCTURAL_CHANGE_THRESHOLD = 0.40  # revenue moving more than 40% in a year


def revenue_changes(revenue: dict[str, float | None]) -> list[LogEntry]:
    """Warn when revenue moves more than 40% between consecutive fiscal years (a merger, split or similar)."""
    entries = []
    years = [label for label in ("FY-2", "FY-1", "FY0") if label in revenue]
    for earlier, later in zip(years, years[1:]):
        before, after = revenue[earlier], revenue[later]
        if before is None or after is None or before <= 0:
            continue
        change = (after - before) / before
        if abs(change) > STRUCTURAL_CHANGE_THRESHOLD:
            entries.append(
                LogEntry(
                    "structural_change", "revenue", later,
                    f"revenue changed {change:+.0%} from {earlier} (${before / 1e6:,.0f}m) to {later} "
                    f"(${after / 1e6:,.0f}m): possible structural change (merger, disposal or similar); "
                    "trends across these years may not be comparable",
                    "warning", "revenue",
                )
            )
    return entries


def reconcile_ladder(
    ladder_total: float | None,
    short_term_borrowings: float | None,
    finance_leases: float | None,
    total_debt: float | None,
    period: str,
) -> list[LogEntry]:
    """Compare the maturity table (plus short-term borrowings and finance leases, which it usually leaves
    out) with total debt. More than 5% apart is a warning; an incomplete ladder is noted."""
    if ladder_total is None:
        return [LogEntry("reconciliation", "maturity_ladder", period,
                         "maturity ladder incomplete (a bucket is not reported), so it cannot be reconciled "
                         "with total debt", "info", "maturity_ladder")]
    if total_debt is None or not total_debt or short_term_borrowings is None or finance_leases is None:
        return []
    expected = ladder_total + short_term_borrowings + finance_leases
    gap = (expected - total_debt) / total_debt
    if abs(gap) <= RECONCILIATION_TOLERANCE:
        return []
    return [LogEntry(
        "reconciliation", "maturity_ladder", period,
        f"maturity ladder ${ladder_total / 1e6:,.0f}m + short-term borrowings ${short_term_borrowings / 1e6:,.0f}m "
        f"+ finance leases ${finance_leases / 1e6:,.0f}m = ${expected / 1e6:,.0f}m, against total debt "
        f"${total_debt / 1e6:,.0f}m ({gap:+.1%})",
        "warning", "maturity_ladder",
    )]
