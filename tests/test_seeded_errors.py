"""Seeded errors: each corruption is built as intended, and the deterministic ones are caught by code."""

from sourcebound.contracts import Memo
from sourcebound.evals.replay import MemoReplay
from sourcebound.evals.seeded import corrupt, negate
from sourcebound.paths import PROJECT_ROOT
from sourcebound.verify.numbers import check_claim_numbers
from sourcebound.verify.quotes import check_quote

MEMO = Memo.model_validate_json((PROJECT_ROOT / "data/published/companies/GT/memo.json").read_text())
REPLAY = MemoReplay(MEMO)


def first_claim(with_placeholder: bool, with_citation: bool):
    for section in MEMO.sections:
        for claim in section.claims:
            draft = REPLAY.claim(claim.id)
            if ("{{m:" in draft.text) == with_placeholder and bool(draft.citations) == with_citation:
                return draft, REPLAY.context(section.id)
    raise AssertionError("no such claim")


def test_negation():
    assert negate("Liquidity is adequate.") == "It is not the case that liquidity is adequate."


def test_raw_number_corruption_is_caught_by_the_number_check():
    draft, ctx = first_claim(with_placeholder=True, with_citation=False)
    bad = dict(corrupt(draft, ctx, REPLAY.cm))["raw_number"]
    assert "{{m:" not in bad.text or bad.text.count("{{m:") < draft.text.count("{{m:")
    assert check_claim_numbers(bad.text, {}, ctx.table, ctx.periods)


def test_wrong_placeholder_stays_valid_so_only_the_judge_can_catch_it():
    draft, ctx = first_claim(with_placeholder=True, with_citation=False)
    bad = dict(corrupt(draft, ctx, REPLAY.cm))["wrong_placeholder"]
    assert bad.text != draft.text
    assert check_claim_numbers(bad.text, {}, ctx.table, ctx.periods) == []


def test_citation_swaps():
    draft, ctx = first_claim(with_placeholder=False, with_citation=True)
    corrupted = dict(corrupt(draft, ctx, REPLAY.cm))
    swapped = corrupted["citation_swap"].citations[0]
    shown = ctx.shown()
    assert swapped.chunk_id != draft.citations[0].chunk_id
    assert check_quote(swapped.quote, shown[swapped.chunk_id].text) != "ok"  # old quote, new passage
    matched = corrupted["citation_swap_with_quote"].citations[0]
    assert check_quote(matched.quote, shown[matched.chunk_id].text) == "ok"  # quote valid, passage irrelevant
