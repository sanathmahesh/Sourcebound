"""Rebuild a memo's claims exactly as drafted, from the saved requests and responses (no model calls).

Used to judge the same claims with another judge model, and to corrupt known-good claims for the
seeded-error test. A section's final draft is the repair if it parsed, otherwise the first draft (the same
rule as the pipeline).
"""

from __future__ import annotations

import json
from pathlib import Path

from sourcebound.contracts import CompanyMetrics, Memo
from sourcebound.llm.schemas import DraftClaim, SectionDraft, parse_json
from sourcebound.memo.draft import SectionContext
from sourcebound.memo.metric_table import build_table, scorecard_context
from sourcebound.memo.render import period_phrases
from sourcebound.memo.sections import SECTION_SPECS
from sourcebound.paths import PROJECT_ROOT
from sourcebound.retrieval.index import load_index

RUNS_DIR = PROJECT_ROOT / "data" / "runs"
PUBLISHED = PROJECT_ROOT / "data" / "published" / "companies"


def final_drafts(raw_file: Path) -> dict[str, SectionDraft]:
    """section id -> the draft the pipeline used."""
    attempts: dict[str, list[SectionDraft | None]] = {}
    for line in raw_file.read_text().splitlines():
        record = json.loads(line)
        if not record["stage"].startswith("draft:"):
            continue
        content = record["response"]["choices"][0]["message"].get("content")
        draft, _ = parse_json(content, SectionDraft)
        attempts.setdefault(record["stage"].split(":", 1)[1], []).append(draft)
    chosen = {}
    for section, drafts in attempts.items():
        usable = drafts[-1] if drafts[-1] is not None else drafts[0]
        if usable is not None:
            chosen[section] = usable
    return chosen


class MemoReplay:
    """The drafted claims of one memo, with the context needed to verify them again."""

    def __init__(self, memo: Memo, runs_dir: Path = RUNS_DIR) -> None:
        self.memo = memo
        self.cm = CompanyMetrics.model_validate_json((PUBLISHED / memo.ticker / "metrics.json").read_text())
        self.table, _ = build_table(self.cm)
        self.periods = period_phrases(self.cm.periods)
        self.index = load_index(memo.ticker)
        self.chunks = {c.id: c for c in self.index.chunks}
        self.drafts = final_drafts(runs_dir / memo.run.raw_outputs)

    def claim(self, claim_id: str) -> DraftClaim:
        section, n = claim_id.rsplit("-", 1)
        return self.drafts[section].claims[int(n) - 1]

    def context(self, section_id: str) -> SectionContext:
        section = next(s for s in self.memo.sections if s.id == section_id)
        spec = next(s for s in SECTION_SPECS if s.id == section_id)
        passages = [self.chunks[cid] for cid in section.passages_shown if cid in self.chunks]
        evidence = scorecard_context(self.cm)[1] if section_id == "rating_rationale" else []
        return SectionContext(spec, self.cm.name, [], self.table, self.periods, passages, judge_evidence=evidence)
