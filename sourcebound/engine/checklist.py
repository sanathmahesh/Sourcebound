"""The data part of the reviewer checklist (PLAN.md 4.9 c): what a human analyst must look at before
signing off a company's figures. Phase 4 adds the claim items for the memo.

Items come from the engine log and the scorecard: figures not available, fallbacks beyond rank 1,
components assumed zero, overrides, reconciliation warnings, possible structural changes, stale data (a
newer filing without facts), and provisional grades. Repeated log entries (the same fallback in four periods) become one item naming the periods.
"""

from __future__ import annotations

import re

from sourcebound.contracts import ChecklistItem
from sourcebound.engine.periods import PERIOD_ORDER

GROUPED_KINDS = {"not_available": "warning", "fallback": "info", "assumed_zero": "info"}


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")


def _label(analysis, concept: str) -> str:
    spec = analysis.specs.get(concept)
    return spec.label if spec else concept


def _grouped(analysis, kind: str, severity: str) -> list[ChecklistItem]:
    groups: dict[tuple[str, str], list] = {}
    for entry in analysis.log:
        if entry.kind == kind:
            groups.setdefault((entry.concept, entry.subject), []).append(entry)
    items = []
    for (concept, subject), entries in groups.items():
        periods = ", ".join(p for p in PERIOD_ORDER if any(e.period == p for e in entries))
        label = _label(analysis, concept)
        if kind == "fallback":
            message = f"{label}: {entries[0].message.split(' because ')[0]} in {periods}."
        elif kind == "not_available":
            message = f"{label} not available in {periods}: no candidate tag is reported (see the log)."
        elif subject == concept:
            message = f"{label} assumed zero (not reported) in {periods}."
        else:
            message = f"{label}: {subject} assumed zero (not reported) in {periods}."
        items.append(ChecklistItem(id=f"{kind}:{concept}:{_slug(subject)}", category=kind, severity=severity,
                                   message=message, ref=concept))
    return items


def data_checklist(analysis, scorecards: list) -> list[ChecklistItem]:
    items: list[ChecklistItem] = []
    for o in analysis.overrides:
        items.append(ChecklistItem(
            id=f"override:{o.ticker}:{o.kind}", category="override", severity="warning",
            message=f"Override approved {o.approved_on} ({o.kind} {o.cik}): {o.reason}", ref=o.ticker))
    for kind, severity in GROUPED_KINDS.items():
        items += _grouped(analysis, kind, severity)
    for n, entry in enumerate(analysis.log):
        if entry.kind == "reconciliation" and entry.severity == "warning":
            items.append(ChecklistItem(id=f"reconciliation:{entry.concept}:{entry.period}:{n}", category="reconciliation",
                                       severity="warning", message=entry.message, ref=entry.concept))
        elif entry.kind == "stale_data":
            items.append(ChecklistItem(id=f"stale_data:{entry.subject}", category="stale_data",
                                       severity="warning", message=entry.message, ref=entry.subject))
        elif entry.kind == "structural_change":
            items.append(ChecklistItem(id=f"structural_change:{entry.period}", category="structural_change",
                                       severity="warning", message=entry.message, ref=entry.concept))
    for card in scorecards:
        if card.provisional:
            missing = ", ".join(f.label for f in card.factors if f.band is None)
            items.append(ChecklistItem(
                id=f"provisional_grade:{card.basis}", category="provisional_grade", severity="warning",
                message=f"SB grade ({card.basis}) is provisional: {missing} could not be scored; "
                        "the remaining weights were renormalised.",
                ref="scorecard"))
    return items
