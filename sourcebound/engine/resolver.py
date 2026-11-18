"""Resolve each concept to one value per period, with lineage and a log of every fallback.

For a concept and a period, the resolver walks the concept's chain in rank order and uses the first
candidate the company reports for that period. For each tag it needs, it finds the facts whose dates
match the period's windows exactly. When several filings report the same window (a 10-K reports last
year again as a comparative), the most recently filed value wins and its accession number is recorded;
if earlier filings reported a different value, that restatement is logged.

For LTM, one tag must supply all three windows (FY0, current year-to-date, prior-year year-to-date), so a
single LTM value never mixes tags.

Everything notable goes into Resolver.log: fallbacks beyond rank 1, values not available, optional parts
assumed zero, restatements. The log feeds the report now and the reviewer checklist later.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date

from sourcebound.edgar.facts import Fact
from sourcebound.edgar.filings import filing_index_url
from sourcebound.engine.concepts import Candidate, ConceptSpec
from sourcebound.engine.periods import Period, PeriodPart, Window


@dataclass(frozen=True)
class SourceFact:
    """One XBRL fact used in a value: everything a reviewer needs to find it in the filing."""

    concept: str
    tag: str
    fallback_rank: int
    value: float
    unit: str
    start: date | None
    end: date
    form: str
    accession: str
    filed: date
    url: str
    sign: int = 1  # -1 when subtracted (the prior-year year-to-date in LTM)
    role: str = ""  # which window of the period this fact fills


@dataclass
class Resolved:
    """A concept's value for one period."""

    concept: str
    label: str
    period: str
    status: str  # "ok" | "not_available" | "assumed_zero"
    value: float | None
    fallback_rank: int | None
    candidate: str  # the candidate used, e.g. "LongTermDebt + ShortTermBorrowings"
    flags: list[str]
    inputs: list[SourceFact]
    reason: str = ""  # why not available, when it is not


@dataclass(frozen=True)
class LogEntry:
    kind: str  # fallback | not_available | assumed_zero | restated | reconciliation | mixed_ranks
    concept: str
    period: str
    message: str
    severity: str = "info"  # "info" or "warning"


class FactIndex:
    """Facts grouped by tag, for fast lookup of the facts matching a window."""

    def __init__(self, facts: list[Fact]) -> None:
        self._by_tag: dict[str, list[Fact]] = defaultdict(list)
        for f in facts:
            self._by_tag[f.tag].append(f)

    def tags(self) -> set[str]:
        return set(self._by_tag)

    def all_facts(self, tag: str) -> list[Fact]:
        return list(self._by_tag.get(tag, []))

    def matching(self, tag: str, window: Window) -> list[Fact]:
        """Facts for this tag whose dates equal the window, oldest filing first."""
        found = [f for f in self._by_tag.get(tag, []) if f.start == window.start and f.end == window.end]
        return sorted(found, key=lambda f: (f.filed, f.accession))


@dataclass
class _Attempt:
    """The outcome of trying one candidate for one period."""

    value: float = 0.0
    inputs: list[SourceFact] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    notes: list[LogEntry] = field(default_factory=list)  # logged only if the candidate is used
    failure: str = ""  # non-empty when the candidate cannot be used


class Resolver:
    def __init__(self, specs: dict[str, ConceptSpec], index: FactIndex, cik: int) -> None:
        self.specs = specs
        self.index = index
        self.cik = cik
        self.log: list[LogEntry] = []
        self._done: dict[tuple[str, str], Resolved] = {}

    def resolve(self, concept: str, period: Period) -> Resolved:
        """The concept's value for the period, trying each candidate in rank order."""
        key = (concept, period.label)
        if key not in self._done:
            self._done[key] = self._resolve(self.specs[concept], period)
        return self._done[key]

    def try_candidate(self, spec: ConceptSpec, candidate: Candidate, period: Period) -> _Attempt:
        """Evaluate one candidate without logging. Used by the resolver and by reconciliation checks."""
        attempt = _Attempt()
        reported = 0
        for component in candidate.components:
            if component.tag:
                part = self._tag_value(spec, candidate, component.tag, period)
            else:
                part = self._concept_value(component.concept, period)
            if part.failure:
                if component.optional:
                    attempt.notes.append(
                        LogEntry("assumed_zero", spec.name, period.label,
                                 f"{component.describe()} assumed zero: not reported (part of rank {candidate.rank} "
                                 f"{candidate.describe()})")
                    )
                    continue
                attempt.failure = f"{component.describe()} {part.failure}"
                return attempt
            reported += 1
            attempt.value += part.value
            attempt.inputs += part.inputs
            attempt.flags += part.flags
            attempt.notes += part.notes
        if reported == 0:
            attempt.failure = "no component reported"
        if candidate.flag:
            attempt.flags.insert(0, candidate.flag)
        return attempt

    # ----- internals ---------------------------------------------------------------------------

    def _resolve(self, spec: ConceptSpec, period: Period) -> Resolved:
        tried: list[str] = []
        for candidate in spec.chain:
            attempt = self.try_candidate(spec, candidate, period)
            if attempt.failure:
                tried.append(f"rank {candidate.rank} {candidate.describe()}: {attempt.failure}")
                continue
            if candidate.rank > 1:
                self.log.append(
                    LogEntry("fallback", spec.name, period.label,
                             f"used rank {candidate.rank} {candidate.describe()} because " + "; ".join(tried))
                )
            self.log += attempt.notes
            return Resolved(
                concept=spec.name,
                label=spec.label,
                period=period.label,
                status="ok",
                value=attempt.value,
                fallback_rank=candidate.rank,
                candidate=candidate.describe(),
                flags=list(dict.fromkeys(attempt.flags)),
                inputs=attempt.inputs,
            )

        reason = "; ".join(tried)
        if spec.required:
            self.log.append(LogEntry("not_available", spec.name, period.label, f"not available: {reason}", "warning"))
            return Resolved(spec.name, spec.label, period.label, "not_available", None, None, "", [], [], reason)
        self.log.append(LogEntry("assumed_zero", spec.name, period.label, f"assumed zero: not reported ({reason})"))
        return Resolved(spec.name, spec.label, period.label, "assumed_zero", 0, None, "", [], [], reason)

    def _concept_value(self, concept: str, period: Period) -> _Attempt:
        sub = self.resolve(concept, period)
        if sub.status == "not_available":
            return _Attempt(failure="not available")
        return _Attempt(value=sub.value, inputs=list(sub.inputs), flags=list(sub.flags))

    def _tag_value(self, spec: ConceptSpec, candidate: Candidate, tag: str, period: Period) -> _Attempt:
        """Sum the tag's facts over the period's windows (one window, or three signed ones for LTM)."""
        if spec.kind == "instant":
            parts = (PeriodPart(+1, Window(None, period.end), "balance sheet"),)
        else:
            parts = period.parts
        attempt = _Attempt()
        for part in parts:
            matches = self.index.matching(tag, part.window)
            if not matches:
                where = f"for {part.window}" if part.window.start else str(part.window)
                return _Attempt(failure=f"not reported {where}")
            chosen = matches[-1]  # most recently filed
            attempt.value += part.sign * chosen.value
            attempt.inputs.append(self._source(spec.name, candidate.rank, chosen, part))
            differing = [m for m in matches if m.value != chosen.value]
            if differing:
                first = matches[0]
                attempt.notes.append(
                    LogEntry("restated", spec.name, period.label,
                             f"{tag} {part.window}: restated from {first.value:,.0f} (accession {first.accession}, "
                             f"filed {first.filed}) to {chosen.value:,.0f} (accession {chosen.accession}, filed "
                             f"{chosen.filed}); using the most recently filed value")
                )
        return attempt

    def _source(self, concept: str, rank: int, fact: Fact, part: PeriodPart) -> SourceFact:
        return SourceFact(
            concept=concept,
            tag=fact.tag,
            fallback_rank=rank,
            value=fact.value,
            unit=fact.unit,
            start=fact.start,
            end=fact.end,
            form=fact.form,
            accession=fact.accession,
            filed=fact.filed,
            url=filing_index_url(self.cik, fact.accession),
            sign=part.sign,
            role=part.role,
        )
