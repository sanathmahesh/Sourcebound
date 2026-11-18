"""The results report recomputes everything from saved outputs, with no model calls."""

import pytest

from sourcebound.evals import report
from sourcebound.llm.provider import SailClient


def test_report_makes_no_model_calls_and_states_what_is_pending(monkeypatch, tmp_path):
    def forbidden(*args, **kwargs):
        raise AssertionError("the report must not call a model")

    monkeypatch.setattr(SailClient, "complete", forbidden)
    monkeypatch.setattr(SailClient, "__init__", forbidden)
    results = report.compute_results()
    assert {"writers", "engine_accuracy", "retrieval_recall", "judge_calibration", "seeded_errors",
            "labels", "scorecard_vs_agencies", "generated_at"} <= set(results)
    text = report.render(results)
    assert "# Evaluation results" in text and "pending" in text.lower() or "n =" in text


def test_retrieval_hit_uses_the_quote(monkeypatch):
    from sourcebound.retrieval.chunking import Chunk
    from sourcebound.retrieval.index import Hit

    chunk = Chunk("X-1", "X", "a", "10-K", "2026-01-01", "2025-12-31", "liquidity", "7", "h", 0, 10, "u",
                  "Our first lien revolving credit facility matures in 2030.")
    assert report.quote_in_hits("First-lien revolving credit facility", [Hit(1, 1.0, chunk)]) is False
    assert report.quote_in_hits("first lien revolving credit facility", [Hit(1, 1.0, chunk)]) is True
