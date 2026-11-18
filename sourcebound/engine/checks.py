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
    """Every total_debt candidate evaluated for this period, whether or not it was the one used."""
    spec = resolver.specs["total_debt"]
    result = []
    for candidate in spec.chain:
        attempt = resolver.try_candidate(spec, candidate, period)
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
                )
            )
    return entries


def long_term_debt_scope(resolver: Resolver, period: Period) -> LogEntry | None:
    """Does LongTermDebt include the current portion at this date? Only answerable if all three tags exist."""
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
        reading, severity = "matches neither current + noncurrent nor noncurrent alone", "warning"
    message = (
        f"LongTermDebt ${total / 1e6:,.0f}m {reading}; LongTermDebtCurrent ${current / 1e6:,.0f}m, "
        f"LongTermDebtNoncurrent ${noncurrent / 1e6:,.0f}m"
    )
    return LogEntry("reconciliation", "total_debt", period.label, message, severity)


def mixed_ranks(concept: str, by_period: dict[str, Resolved]) -> LogEntry | None:
    """Note when a concept is resolved through different candidates in different periods."""
    used = {label: r for label, r in by_period.items() if r.status == "ok"}
    if len({r.candidate for r in used.values()}) <= 1:
        return None
    detail = "; ".join(f"{label}: rank {r.fallback_rank} {r.candidate}" for label, r in used.items())
    return LogEntry("mixed_ranks", concept, "all", f"different candidates across periods ({detail})")
