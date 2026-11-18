"""Replaying saved drafts reproduces the published claims without any model call."""

from sourcebound.contracts import Memo
from sourcebound.evals.replay import MemoReplay
from sourcebound.memo.render import render_claim
from sourcebound.paths import PROJECT_ROOT


def test_replayed_claims_render_to_the_published_text():
    memo = Memo.model_validate_json((PROJECT_ROOT / "data/published/companies/GT/memo.json").read_text())
    replay = MemoReplay(memo)
    for section in memo.sections:
        ctx = replay.context(section.id)
        shown = ctx.shown()
        for claim in section.claims:
            draft = replay.claim(claim.id)
            cited = {c.chunk_id: shown[c.chunk_id].text for c in draft.citations if c.chunk_id in shown}
            rendered = render_claim(draft.text, cited, ctx.table, ctx.periods)
            assert rendered.text == "".join(s.v for s in claim.segments)
