"""The capability probe's checks, run against a fake client."""

import json

from sourcebound.pipeline.capability_probe import probe_model
from tests.fakes import FakeChatClient, result

GOOD = [
    result(json.dumps({"answer": "ready", "number": 7})),
    result(tool_calls=[("get_metric", json.dumps({"metric_id": "net_leverage", "period": "LTM"}))]),
    result(tool_calls=[("get_metric", json.dumps({"metric_id": "net_leverage", "period": "LTM"}))]),
    result(json.dumps({"answer": "done", "number": 3})),
    result(tool_calls=[("get_metric", json.dumps({"metric_id": "net_leverage", "period": "LTM"}))]),
    result(json.dumps({"answer": "done", "number": 3})),
]


def test_all_three_checks_pass_on_good_behaviour():
    checks = probe_model(FakeChatClient(GOOD), "m", reasoning_effort="low")
    assert [(c.name, c.passed) for c in checks] == [
        ("structured output (json_schema, strict)", True),
        ("strict function tool call", True),
        ("tool call then structured answer, in one request setup", True),
        ("tool call, then structured answer in a separate request", True),
    ]


def test_wrong_json_fails_structured_output():
    replies = [result('{"answer": "ready"}')] + GOOD[1:]
    checks = probe_model(FakeChatClient(replies), "m", reasoning_effort="low")
    assert checks[0].passed is False and "number" in checks[0].detail


def test_extra_tool_argument_fails_strict_check():
    replies = [GOOD[0], result(tool_calls=[("get_metric", json.dumps({"metric_id": "net_leverage", "period": "LTM", "x": 1}))])] + GOOD[2:]
    checks = probe_model(FakeChatClient(replies), "m", reasoning_effort="low")
    assert checks[1].passed is False


def test_answering_without_the_tool_fails_the_combined_check():
    replies = GOOD[:2] + [result(json.dumps({"answer": "done", "number": 3}))] + GOOD[4:]
    checks = probe_model(FakeChatClient(replies), "m", reasoning_effort="low")
    assert checks[2].passed is False and "tool" in checks[2].detail


def test_combined_check_sends_tool_result_and_schema():
    client = FakeChatClient(GOOD)
    probe_model(client, "m", reasoning_effort="low")
    second_turn = client.requests[3]
    assert second_turn["response_format"]["type"] == "json_schema"
    assert second_turn["messages"][-1]["role"] == "tool"
    assert all(r["reasoning_effort"] == "low" and r["model"] == "m" for r in client.requests)


def test_separate_requests_keep_tools_and_schema_apart():
    client = FakeChatClient(GOOD)
    checks = probe_model(client, "m", reasoning_effort="low")
    assert checks[3].passed
    tool_turn, answer_turn = client.requests[4], client.requests[5]
    assert "tools" in tool_turn and "response_format" not in tool_turn
    assert "response_format" in answer_turn and "tools" not in answer_turn
    assert answer_turn["messages"][-1]["role"] == "tool"
