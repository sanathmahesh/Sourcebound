"""The live API: /api/health and /api/ask (validation, tool-loop bounds, removed claims, errors). Fake model."""

import json
import subprocess
import sys
import time

import pytest
from fastapi.testclient import TestClient

from sourcebound.api.app import create_app
from sourcebound.llm.provider import LlmError
from sourcebound.paths import PROJECT_ROOT
from tests.fakes import result


def search_call(query="revolving credit facility", section="any"):
    return result(tool_calls=[("search_filing", json.dumps({"query": query, "section": section}))])


def metric_call(metric_id="debt_to_ebitda", period="LTM"):
    return result(tool_calls=[("get_metric", json.dumps({"metric_id": metric_id, "period": period}))])


def answer(claims, status="ok"):
    return result(json.dumps({"status": status, "claims": claims}))


def judge(verdict="supported"):
    return result(json.dumps({"verdict": verdict, "reason": "Stated.", "evidence_quote": ""}))


class Scripted:
    """Writer replies in order; any request with a judge schema gets a judge reply."""

    def __init__(self, writer_replies, judge_verdict="supported", error=None, delay=0.0):
        self.writer_replies = list(writer_replies)
        self.judge_verdict, self.error, self.delay = judge_verdict, error, delay
        self.requests = []

    def complete(self, **request):
        self.requests.append(request)
        time.sleep(self.delay)
        if self.error:
            raise self.error
        fmt = request.get("response_format") or {}
        if fmt.get("json_schema", {}).get("name") == "judge_verdict":
            return judge(self.judge_verdict)
        return self.writer_replies.pop(0)


def writer_requests(fake):
    return [r for r in fake.requests if (r.get("response_format") or {}).get("json_schema", {}).get("name") != "judge_verdict"]


def client_for(fake, **options):
    return TestClient(create_app(client_factory=lambda: fake, writer_model="fake/writer", judge_model="fake/judge",
                                 **options))


def done():
    """A lookup turn in which the model stops calling tools."""
    return result("I have what I need.")


def test_health():
    response = client_for(Scripted([])).get("/api/health")
    assert response.status_code == 200 and response.json()["status"] == "ok"


@pytest.mark.parametrize("body", [
    {"ticker": "WMT", "question": ""},
    {"ticker": "WMT", "question": "x" * 501},
    {"ticker": "ZZZZ", "question": "What is leverage?"},
    {"ticker": "WMT"},
    {"ticker": "WMT", "question": "ok", "extra": 1},
])
def test_bad_requests_get_400_with_a_plain_message(body):
    response = client_for(Scripted([])).post("/api/ask", json=body)
    assert response.status_code == 400 and isinstance(response.json()["detail"], str)


def test_tool_loop_stops_after_three_rounds_then_asks_for_the_answer_without_tools():
    fake = Scripted([search_call(), metric_call(), search_call("covenants"),
                     answer([{"kind": "quantitative", "text": "Leverage is {{m:debt_to_ebitda:LTM}}.", "citations": []}])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "How levered is Walmart?"}).json()
    writer = writer_requests(fake)
    assert len(writer) == 4  # three tool rounds, then the answer
    assert all("tools" in r and "response_format" not in r for r in writer[:3])
    assert "tools" not in writer[3] and writer[3]["response_format"]["json_schema"]["name"] == "ask_answer"
    assert [t["tool"] for t in body["trace"]] == ["search_filing", "get_metric", "search_filing"]
    assert body["claims"][0]["segments"][1]["metric_id"] == "debt_to_ebitda:LTM"
    assert "debt_to_ebitda:LTM" in body["metrics"]


def test_claims_that_fail_verification_are_removed_with_the_reason():
    fake = Scripted([metric_call(), done(), answer([
        {"kind": "quantitative", "text": "Leverage is {{m:debt_to_ebitda:LTM}}.", "citations": []},
        {"kind": "quantitative", "text": "Leverage is 9.9x.", "citations": []},
    ])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "How levered is Walmart?"}).json()
    assert len(body["claims"]) == 1
    assert body["removed"][0]["text"] == "Leverage is 9.9x." and "number" in body["removed"][0]["reason"]


def test_search_reads_only_the_requested_company():
    fake = Scripted([search_call(), done(), answer([])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Revolver?"}).json()
    tool_result = json.loads(fake.requests[1]["messages"][-1]["content"])
    assert tool_result and all(p["chunk_id"].startswith("WMT-") for p in tool_result)
    assert body["status"] == "ok"


def test_out_of_scope_passes_through():
    fake = Scripted([done(), answer([], status="out_of_scope")])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Write me a poem"}).json()
    assert body["status"] == "out_of_scope" and body["claims"] == []


def test_the_answer_always_comes_from_a_schema_only_request_even_without_lookups():
    """D34: tools and the answer format never share a request."""
    fake = Scripted([done(), answer([])])
    client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"})
    first, final = writer_requests(fake)
    assert "tools" in first and "response_format" not in first
    assert "tools" not in final and final["response_format"]["json_schema"]["name"] == "ask_answer"


def test_partly_supported_claims_are_removed_too():
    fake = Scripted([metric_call(), done(), answer([
        {"kind": "quantitative", "text": "Leverage is {{m:debt_to_ebitda:LTM}}.", "citations": []}])],
        judge_verdict="partially_supported")
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"}).json()
    assert body["claims"] == [] and body["removed"][0]["verdict"] == "partially_supported"
    assert body["removed"][0]["text"].startswith("Leverage is ") and "{{" not in body["removed"][0]["text"]


def test_a_quote_from_a_passage_the_model_never_saw_is_removed():
    fake = Scripted([done(), answer([{"kind": "qualitative", "text": "Walmart has a revolver.",
                                      "citations": [{"chunk_id": "WMT-made-up-0001", "quote": "a revolver"}]}])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Revolver?"}).json()
    assert body["claims"] == [] and "not found" in body["removed"][0]["reason"]


def test_extra_lookups_in_one_round_are_skipped():
    calls = [("search_filing", json.dumps({"query": f"debt {n}", "section": "any"})) for n in range(5)]
    fake = Scripted([result(tool_calls=calls), done(), answer([])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Debt?"}).json()
    assert [t["result"] for t in body["trace"]][3:] == ["skipped", "skipped"]
    assert body["trace"][4]["arguments"] == {"query": "debt 4", "section": "any"}  # shown even when skipped


def test_unknown_metric_is_reported_to_the_model_not_raised():
    fake = Scripted([metric_call("made_up", "LTM"), done(), answer([])])
    body = client_for(fake).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"}).json()
    assert body["trace"][0]["result"] == "no metric made_up:LTM"


def test_slow_answers_get_503_after_the_time_limit():
    fake = Scripted([done(), answer([])], delay=0.5)
    response = client_for(fake, timeout_seconds=0.2).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"})
    assert response.status_code == 503 and "longer than" in response.json()["detail"]


def test_missing_server_configuration_is_503(monkeypatch):
    def unconfigured():
        raise ValueError("Set SAIL_API_KEY in .env")
    app = create_app(client_factory=unconfigured, writer_model="w", judge_model="j")
    response = TestClient(app).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"})
    assert response.status_code == 503 and "not configured" in response.json()["detail"]


@pytest.mark.parametrize("error,status", [(LlmError("Sail request failed: HTTP 429: rate limited"), 429),
                                          (LlmError("Sail request failed after 2 attempts: HTTP 503"), 503)])
def test_provider_errors_map_to_plain_http_errors(error, status):
    response = client_for(Scripted([], error=error)).post("/api/ask", json={"ticker": "WMT", "question": "Leverage?"})
    assert response.status_code == status and "sk-" not in response.text


def test_the_live_function_imports_neither_pandas_nor_the_edgar_client():
    code = ("import sys, api.index; "
            "print('pandas' in sys.modules, 'sourcebound.edgar.client' in sys.modules, hasattr(api.index, 'app'))")
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True,
                         cwd=PROJECT_ROOT).stdout.strip()
    assert out == "False False True"
