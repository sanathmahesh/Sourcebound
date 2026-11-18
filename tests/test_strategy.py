"""Strategy artifacts: figures come only from results.json, the timing log or config (PLAN.md phase 8 test)."""

import csv
import json

import pytest

from sourcebound.strategy import render as r
from sourcebound.strategy.timings import TIMING_COLUMNS, read_timings, summarise

RESULTS = {
    "generated_at": "2026-11-18 07:51 UTC",
    "writers": {"GLM-5.3": {"model": "zai-org/GLM-5.3", "memos_run1": 15, "claims_per_memo": 35.0666,
                            "judge_supported": {"value": 0.8593, "n": 526}, "cost_total_per_memo": 0.10674,
                            "model_seconds_per_memo": 250.588}},
    "judge_calibration": {"zai-org/GLM-5.3": {"agreement": {"value": None, "n": 0}}},
}


def test_placeholders_render_from_results_with_their_sample_size():
    text, spans = r.render("Supported: {{r:writers>GLM-5.3>judge_supported|rate}}; cost {{r:writers>GLM-5.3>cost_total_per_memo|usd3}}.",
                           RESULTS, [])
    assert text == "Supported: 85.9% (n = 526); cost $0.107."
    assert [text[a:b] for a, b in spans] == ["85.9% (n = 526)", "$0.107"]


def test_unmeasured_rates_render_as_pending():
    text, _ = r.render("{{r:judge_calibration>zai-org/GLM-5.3>agreement|rate}}", RESULTS, [])
    assert text == "pending (n = 0)"


def test_unknown_paths_and_formats_fail_loudly():
    with pytest.raises(KeyError):
        r.render("{{r:writers>Nope>cost|usd3}}", RESULTS, [])
    with pytest.raises(ValueError):
        r.render("{{r:writers>GLM-5.3>claims_per_memo|guess}}", RESULTS, [])


def test_typed_digits_outside_placeholders_are_found():
    text, spans = r.render("Cost {{r:writers>GLM-5.3>cost_total_per_memo|usd3}}, about 6 times less.", RESULTS, [])
    assert r.stray_numbers(text, spans) == ["6"]


def test_identifiers_and_dates_are_not_figures():
    text = "SR 26-2, OCC Bulletin 2026-13, FIL-15-2026, SR 11-7 and SR 23-4; a 10-K or 10-Q; D34; SB-1 to SB-6; 17 April 2026; phase 9."
    assert r.stray_numbers(text, []) == []


def write_log(path, rows):
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(TIMING_COLUMNS)
        writer.writerows(rows)


def test_empty_timing_log_means_pending(tmp_path):
    path = tmp_path / "timings.csv"
    write_log(path, [])
    assert summarise(read_timings(path)) == []
    text, _ = r.render("{{table:timings}}", RESULTS, read_timings(path))
    assert "No timings recorded yet" in text


def test_timing_summary_uses_medians_per_task_and_condition(tmp_path):
    # Synthetic rows to test the arithmetic; the real log is filled in only by the author.
    path = tmp_path / "timings.csv"
    write_log(path, [["2026-12-01", "WMT", "manual", "memo", "09:00", "10:30", "90", "2", ""],
                     ["2026-12-02", "VZ", "manual", "memo", "09:00", "11:00", "120", "1", ""],
                     ["2026-12-03", "GT", "manual", "memo", "09:00", "10:00", "60", "0", ""],
                     ["2026-12-01", "HCA", "tool-assisted", "memo", "13:00", "13:40", "40", "0", ""]])
    rows = summarise(read_timings(path))
    assert [(s.task, s.condition, s.n, s.median_minutes, s.errors_found_later) for s in rows] == [
        ("memo", "manual", 3, 90.0, 3), ("memo", "tool-assisted", 1, 40.0, 0)]


def test_timing_log_rejects_bad_rows(tmp_path):
    path = tmp_path / "timings.csv"
    write_log(path, [["2026-12-01", "WMT", "by hand", "memo", "09:00", "10:30", "90", "0", ""]])
    with pytest.raises(ValueError, match="condition"):
        read_timings(path)


def test_rendered_artifacts_are_current_and_carry_no_stray_numbers():
    results = json.loads(r.RESULTS_FILE.read_text())
    timings = read_timings(r.TIMINGS_FILE)
    for template in sorted(r.TEMPLATE_DIR.glob("*.md")):
        text, spans = r.render(template.read_text(), results, timings)
        assert (r.STRATEGY_DIR / template.name).read_text() == r.HEADER.format(name=template.name) + text, \
            f"{template.name} is stale: run uv run python -m sourcebound.pipeline.build_strategy"
        assert r.stray_numbers(text, spans) == [], template.name
    assert len(list(r.TEMPLATE_DIR.glob("*.md"))) == 5  # artifacts 1-5; the decision log is written by hand


def test_numbered_list_markers_are_structure_not_figures():
    assert r.stray_numbers("Steps:\n1. Open the filing.\n2. Time it. It took 3 minutes.", []) == ["3"]


def test_published_about_file_matches_the_documents_in_the_repo():
    from sourcebound import contracts as c
    from sourcebound.pipeline.build_strategy import METHOD_FILE, PUBLISHED_DIR, about_documents, method_text

    assert METHOD_FILE.read_text() == method_text(), "run: uv run python -m sourcebound.pipeline.build_strategy"
    about = c.AboutFile.model_validate_json((PUBLISHED_DIR / "about.json").read_text())
    assert about.documents == about_documents(), "run: uv run python -m sourcebound.pipeline.build_strategy"
    assert [d.id for d in about.documents if d.group == "strategy"][-1] == "06-decision-log"


def test_code_spans_are_names_not_figures():
    assert r.stray_numbers("See `test_bad_requests_get_400_with_a_plain_message` and 7 others.", []) == ["7"]


def test_results_file_is_current_and_carries_no_typed_figures():
    from sourcebound.paths import PROJECT_ROOT
    from sourcebound.pipeline.build_strategy import render_results

    text = render_results()  # raises if the template types a figure by hand
    assert (PROJECT_ROOT / "RESULTS.md").read_text() == text, "run: uv run python -m sourcebound.pipeline.build_strategy"
    for words in ("pending (n = 0)", "uv run python -m sourcebound.evals.report", "zai-org/GLM-5.3"):
        assert words in text


def test_about_page_carries_the_model_card_and_limitations():
    from sourcebound.pipeline.build_strategy import about_documents

    reference = [d.id for d in about_documents() if d.group == "reference"]
    assert reference == ["model_card", "limitations"]
