"""Layer (c): the reviewer checklist appended to the memo (PLAN.md 4.9 c).

The data items come from the engine (figures not available, fallbacks, assumed zeros, overrides,
reconciliation warnings, provisional grade, stale data). This adds the memo's own items: every unsupported
or partially supported claim (they stay visible in the memo, marked) and every section draft problem.
"""

from __future__ import annotations

from sourcebound.contracts import ChecklistItem, MemoSection


def memo_checklist(data_items: list[ChecklistItem], sections: list[MemoSection]) -> list[ChecklistItem]:
    items = list(data_items)
    for section in sections:
        for note in section.notes:
            items.append(ChecklistItem(id=f"draft_problem:{section.id}:{len(items)}", category="draft_problem",
                                       severity="warning", message=f"{section.title}: {note}", ref=section.id))
        for claim in section.claims:
            if claim.verdict == "supported":
                continue
            text = "".join(s.v for s in claim.segments)
            category = "unsupported_claim" if claim.verdict == "unsupported" else "partially_supported_claim"
            items.append(ChecklistItem(
                id=f"{category}:{claim.id}", category=category, severity="warning",
                message=f"{section.title}: {claim.verdict.replace('_', ' ')} ({claim.judge_reason}): “{text}”",
                ref=claim.id))
    return items
