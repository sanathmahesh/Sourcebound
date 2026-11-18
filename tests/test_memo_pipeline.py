"""End to end on Goodyear's published metrics and index, with a rule-based fake model. No network."""

import json
import re
import shutil

import pytest

from sourcebound.contracts import Memo, VerificationReport
from sourcebound.llm.provider import LlmSettings
from sourcebound.paths import PROJECT_ROOT
from sourcebound.pipeline.generate_memo import generate_memo
from tests.fakes import result


class RuleFake:
    """Writes one placeholder claim and one cited claim per section; the judge says 'supported'."""

    def __init__(self):
        self.requests = []

    def complete(self, **request):
        self.requests.append(request)
        name = request["response_format"]["json_schema"]["name"]
        message = request["messages"][-1]["content"]
        if name == "judge_verdict":
            return result(json.dumps({"verdict": "supported", "reason": "Stated in the evidence.", "evidence_quote": ""}))
        placeholder = re.search(r"\{\{m:[^}]+\}\}", message)
        claims = []
        if placeholder:
            claims.append({"kind": "quantitative", "text": f"The figure is {placeholder.group()}.", "citations": []})
        passage = re.search(r"^\[([^\]]+)\] \([^)]*\)\n(.+)$", message, re.MULTILINE)
        if passage:
            words = [w for w in passage.group(2).split() if not re.search(r"\d", w)][:6]
            quote = " ".join(words)
            if quote and quote in passage.group(2):
                claims.append({"kind": "qualitative", "text": "The filing discusses this.",
                               "citations": [{"chunk_id": passage.group(1), "quote": quote}]})
        return result(json.dumps({"claims": claims}))


@pytest.fixture(scope="module")
def outputs(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("memo")
    (tmp / "published/companies/GT").mkdir(parents=True)
    shutil.copy(PROJECT_ROOT / "data/published/companies/GT/metrics.json", tmp / "published/companies/GT/metrics.json")
    settings = LlmSettings("https://api.example.invalid/v1", "sk-test", "fake/writer", "fake/judge", "asap")
    client = RuleFake()
    memo, report = generate_memo("GT", client, settings=settings, published_dir=tmp / "published",
                                 runs_dir=tmp / "runs", reports_dir=tmp / "reports",
                                 prices={"models": {"fake/writer": {"input": 1, "cached_input": 0.1, "output": 2},
                                                    "fake/judge": {"input": 1, "cached_input": 0.1, "output": 2}}})
    return tmp, memo, report, client


def test_memo_and_report_validate_and_are_written(outputs):
    tmp, memo, report, _ = outputs
    assert Memo.model_validate_json((tmp / "published/companies/GT/memo.json").read_text()) == memo
    assert VerificationReport.model_validate_json((tmp / "published/companies/GT/verification.json").read_text()) == report
    assert (tmp / "reports/memos/GT.md").exists()


def test_six_sections_in_order(outputs):
    _, memo, _, _ = outputs
    assert [s.id for s in memo.sections] == ["business_profile", "financial_risk", "liquidity", "maturity_wall",
                                             "key_risks", "rating_rationale"]


def test_every_number_and_citation_is_traceable_inside_the_memo(outputs):
    _, memo, _, _ = outputs
    for section in memo.sections:
        for claim in section.claims:
            for segment in claim.segments:
                if segment.t == "metric":
                    assert segment.metric_id in memo.metrics
                if segment.t == "quoted":
                    assert segment.chunk_id in memo.passages
            for citation in claim.citations:
                assert citation.chunk_id in memo.passages


def test_rating_rationale_gets_the_scorecard_and_no_new_passages(outputs):
    _, _, _, client = outputs
    rationale = [r for r in client.requests
                 if r["response_format"]["json_schema"]["name"] == "section_draft"
                 and "Section: Rating rationale" in r["messages"][-1]["content"]][0]
    text = rationale["messages"][-1]["content"]
    assert "{{m:sb_grade:latest}}" in text and "{{m:band_debt_to_ebitda:latest}}" in text
    assert "Findings from earlier sections" in text


def test_checklist_carries_data_items_and_run_totals_are_counted(outputs):
    _, memo, report, client = outputs
    assert any(item.category == "fallback" for item in memo.checklist)  # from the engine (GT derived EBIT)
    total_calls = memo.run.drafting.calls + memo.run.verification.calls
    assert total_calls == len(client.requests)
    assert report.summary.claims == sum(len(s.claims) for s in memo.sections)
    assert report.summary.supported == report.summary.claims  # the fake judge supports everything


def test_raw_requests_and_responses_are_saved(outputs):
    tmp, memo, _, client = outputs
    lines = (tmp / "runs" / memo.run.raw_outputs).read_text().splitlines()
    assert len(lines) == len(client.requests)
    first = json.loads(lines[0])
    assert {"stage", "request", "response", "usage", "cost_usd"} <= set(first)
    assert "sk-test" not in "".join(lines)


def test_rationale_writer_is_told_whether_the_grade_is_provisional(outputs):
    _, memo, _, client = outputs
    rationale = [r for r in client.requests if r["response_format"]["json_schema"]["name"] == "section_draft"
                 and "Section: Rating rationale" in r["messages"][-1]["content"]][0]
    expected = "is provisional" if memo.grade_provisional else "is not provisional"
    assert expected in rationale["messages"][-1]["content"]


def test_rationale_claims_are_judged_against_the_scorecard(outputs):
    _, _, _, client = outputs
    judged = [r["messages"][-1]["content"] for r in client.requests
              if r["response_format"]["json_schema"]["name"] == "judge_verdict" and "Scorecard" in r["messages"][-1]["content"]]
    assert judged, "no rationale claim was judged with the scorecard as evidence"
