"""Drafting with one repair attempt, claim verification, judge parsing and passage merging (fake client)."""

import json

from sourcebound.llm.schemas import JudgeVerdict, parse_json
from sourcebound.memo.draft import SectionContext, draft_section
from sourcebound.memo.render import TableEntry
from sourcebound.memo.retrieve import merge_hits
from sourcebound.memo.sections import SECTION_SPECS
from sourcebound.retrieval.chunking import Chunk
from sourcebound.retrieval.index import Hit
from sourcebound.verify.claims import verify_claim
from tests.fakes import FakeChatClient, result

PASSAGE = "In total, the Company had committed lines of credit in the U.S. of $15.0 billion, all undrawn."


def chunk(cid: str, text: str = PASSAGE, filed: str = "2026-03-13", section: str = "liquidity") -> Chunk:
    return Chunk(cid, "WMT", "acc", "10-K", filed, "2026-01-31", section, "7", "h", 0, len(text), "https://x", text)


CTX = SectionContext(
    spec=SECTION_SPECS[2],  # liquidity
    company="Walmart Inc.",
    rows=[TableEntry("liquidity_coverage:LTM", "Liquidity coverage, LTM", "1.07x")],
    table={"liquidity_coverage:LTM": TableEntry("liquidity_coverage:LTM", "Liquidity coverage, LTM", "1.07x")},
    periods={"LTM": "the twelve months to 31 July 2026"},
    passages=[chunk("WMT-1")],
)
GOOD = {"claims": [
    {"kind": "quantitative", "text": "Liquidity coverage was {{m:liquidity_coverage:LTM}} for {{p:LTM}}.", "citations": []},
    {"kind": "qualitative", "text": "Walmart has $15.0 billion of committed credit lines, all undrawn.",
     "citations": [{"chunk_id": "WMT-1", "quote": "committed lines of credit in the U.S. of $15.0 billion"}]},
]}


def test_good_draft_needs_no_repair():
    client = FakeChatClient([result(json.dumps(GOOD))])
    outcome = draft_section(client, model="w", reasoning_effort="medium", max_tokens=100, ctx=CTX)
    assert outcome.draft is not None and len(outcome.draft.claims) == 2
    assert outcome.repaired is False and outcome.problems == []
    request = client.requests[0]
    assert request["response_format"]["json_schema"]["strict"] is True and "tools" not in request
    prompt = request["messages"][-1]["content"]
    assert "{{m:liquidity_coverage:LTM}}" in prompt and "WMT-1" in prompt and PASSAGE in prompt


def test_one_repair_attempt_fixes_a_raw_number():
    bad = {"claims": [{"kind": "quantitative", "text": "Liquidity coverage was 1.07x.", "citations": []}]}
    client = FakeChatClient([result(json.dumps(bad)), result(json.dumps(GOOD))])
    outcome = draft_section(client, model="w", reasoning_effort="medium", max_tokens=100, ctx=CTX)
    assert outcome.repaired is True and outcome.problems == []
    assert "1.07" in client.requests[1]["messages"][-1]["content"]  # the repair request names the problem


def test_failed_repair_keeps_the_claims_and_reports_problems():
    bad = {"claims": [{"kind": "quantitative", "text": "Liquidity coverage was 1.07x.", "citations": []}]}
    client = FakeChatClient([result(json.dumps(bad)), result(json.dumps(bad))])
    outcome = draft_section(client, model="w", reasoning_effort="medium", max_tokens=100, ctx=CTX)
    assert outcome.draft is not None and outcome.repaired is True
    assert outcome.problems and "1.07" in outcome.problems[0]


def test_unreadable_json_twice_means_no_draft():
    client = FakeChatClient([result("not json"), result("still not json")])
    outcome = draft_section(client, model="w", reasoning_effort="medium", max_tokens=100, ctx=CTX)
    assert outcome.draft is None and "not valid" in outcome.error


def test_judge_output_parsing():
    verdict, error = parse_json('{"verdict": "supported", "reason": "Stated.", "evidence_quote": "all undrawn"}', JudgeVerdict)
    assert error == "" and verdict.verdict == "supported"
    assert parse_json('{"verdict": "probably", "reason": "", "evidence_quote": ""}', JudgeVerdict)[0] is None
    assert parse_json("```json\n{\"verdict\": \"unsupported\", \"reason\": \"No.\", \"evidence_quote\": \"\"}\n```",
                      JudgeVerdict)[0].verdict == "unsupported"


def judge_reply(verdict="supported"):
    return result(json.dumps({"verdict": verdict, "reason": "The passage says so.", "evidence_quote": "all undrawn"}))


def test_claim_passing_deterministic_checks_goes_to_the_judge():
    from sourcebound.llm.schemas import DraftClaim

    client = FakeChatClient([judge_reply()])
    claim = DraftClaim.model_validate(GOOD["claims"][1])
    memo_claim, calls = verify_claim("liquidity-2", claim, CTX, client, model="j", reasoning_effort="low", max_tokens=50)
    assert (memo_claim.verdict, memo_claim.checked_by) == ("supported", "judge")
    assert len(calls) == 1
    judged = client.requests[0]["messages"][-1]["content"]
    assert PASSAGE in judged and "$15.0 billion" in judged


def test_claim_with_a_missing_quote_is_unsupported_without_a_model_call():
    from sourcebound.llm.schemas import DraftClaim

    claim = DraftClaim.model_validate({"kind": "qualitative", "text": "The credit lines are fully drawn.",
                                       "citations": [{"chunk_id": "WMT-1", "quote": "the lines are fully drawn today"}]})
    client = FakeChatClient([])
    memo_claim, calls = verify_claim("liquidity-3", claim, CTX, client, model="j", reasoning_effort="low", max_tokens=50)
    assert (memo_claim.verdict, memo_claim.checked_by) == ("unsupported", "deterministic")
    assert "quote not found" in memo_claim.judge_reason and calls == []


def test_quantitative_claim_without_citation_is_judged_against_metric_values():
    from sourcebound.llm.schemas import DraftClaim

    client = FakeChatClient([judge_reply("partially_supported")])
    claim = DraftClaim.model_validate(GOOD["claims"][0])
    memo_claim, _ = verify_claim("liquidity-1", claim, CTX, client, model="j", reasoning_effort="low", max_tokens=50)
    assert memo_claim.verdict == "partially_supported"
    assert "Liquidity coverage, LTM (the twelve months to 31 July 2026): 1.07x" in client.requests[0]["messages"][-1]["content"]


def test_merge_ranks_by_best_rank_and_keeps_the_latest_duplicate():
    a, b = chunk("K-1", "Revolving credit facility text.", "2026-03-13"), chunk("Q-1", "Revolving credit facility text.", "2026-08-28")
    c = chunk("K-2", "Commercial paper programme text.")
    merged = merge_hits([[Hit(1, 9.0, a), Hit(2, 5.0, c)], [Hit(1, 8.0, b)]], limit=8)
    assert [x.id for x in merged] == ["Q-1", "K-2"]  # a and b are duplicates: keep the later filing


def test_judge_sees_the_period_dates_behind_each_figure():
    """Walmart run 1: true claims were marked 'partially supported' because 'FY-2' meant nothing to the judge."""
    from sourcebound.llm.schemas import DraftClaim

    client = FakeChatClient([judge_reply()])
    claim = DraftClaim.model_validate({"kind": "quantitative", "text": "Liquidity coverage was {{m:liquidity_coverage:LTM}}.",
                                       "citations": []})
    verify_claim("liquidity-1", claim, CTX, client, model="j", reasoning_effort="low", max_tokens=50)
    assert "- Liquidity coverage, LTM (the twelve months to 31 July 2026): 1.07x" in client.requests[0]["messages"][-1]["content"]


def test_section_wide_evidence_reaches_the_judge_without_placeholders():
    """Walmart run 1: a rationale claim wrongly called the grade provisional; the judge never saw the scorecard."""
    from dataclasses import replace

    from sourcebound.llm.schemas import DraftClaim

    ctx = replace(CTX, judge_evidence=[("SB grade (latest)", "SB-3, not provisional: all six factors scored")])
    client = FakeChatClient([judge_reply("unsupported")])
    claim = DraftClaim.model_validate({"kind": "qualitative", "text": "Walmart has $15.0 billion of committed credit lines.",
                                       "citations": [{"chunk_id": "WMT-1", "quote": "committed lines of credit in the U.S. of $15.0 billion"}]})
    verify_claim("rating_rationale-5", claim, ctx, client, model="j", reasoning_effort="low", max_tokens=50)
    assert "SB-3, not provisional" in client.requests[0]["messages"][-1]["content"]
