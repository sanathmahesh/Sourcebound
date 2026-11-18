"""BM25: tokeniser, a hand-computed toy example, filters, determinism."""

import math

import pytest

from sourcebound.retrieval.bm25 import build_bm25, search_bm25, tokenize


def test_tokenizer_lowercases_keeps_alphanumerics_and_drops_stopwords():
    assert tokenize("The Revolving Credit Facility of $3.5 billion matures in 2029!") == [
        "revolving", "credit", "facility", "3", "5", "billion", "matures", "2029",
    ]


def test_tokenizer_splits_on_punctuation_and_apostrophes():
    assert tokenize("Walmart's debt-to-EBITDA") == ["walmart", "s", "debt", "ebitda"]


TOY = ["revolving credit facility", "credit rating", "credit credit risk"]


def test_scores_equal_the_hand_computed_example():
    """By hand, with k1 = 1.5, b = 0.75, N = 3, average length 8/3:
    idf(t) = ln((N - df + 0.5) / (df + 0.5) + 1): credit (df 3) = ln(1 + 0.5/3.5) = 0.133531...
                                                   facility (df 1) = ln(1 + 2.5/1.5) = 0.980829...
    term score = idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * len / avglen)).
    Query "credit facility": d0 = 1.055016, d1 = 0.150458, d2 = 0.183391 (see the phase-3 notes)."""
    index = build_bm25(TOY)
    assert index.avg_length == pytest.approx(8 / 3)
    results = dict(search_bm25(index, "credit facility", k=3))
    assert results[0] == pytest.approx(1.055015995868638, abs=1e-9)
    assert results[1] == pytest.approx(0.15045790718256064, abs=1e-9)
    assert results[2] == pytest.approx(0.1833907538190868, abs=1e-9)
    assert [doc for doc, _ in search_bm25(index, "credit facility", k=3)] == [0, 2, 1]


def test_idf_is_never_negative():
    index = build_bm25(["debt"] * 10)
    assert search_bm25(index, "debt", k=1)[0][1] > 0
    assert math.isfinite(search_bm25(index, "debt", k=1)[0][1])


def test_only_matching_documents_are_returned_and_k_limits():
    index = build_bm25(TOY)
    assert [doc for doc, _ in search_bm25(index, "rating", k=5)] == [1]
    assert len(search_bm25(index, "credit", k=2)) == 2
    assert search_bm25(index, "nonexistent words", k=5) == []


def test_allowed_documents_filter():
    index = build_bm25(TOY)
    assert [doc for doc, _ in search_bm25(index, "credit", k=5, allowed={1, 2})] == [2, 1]


def test_ties_break_by_document_order():
    index = build_bm25(["same text", "same text", "same text"])
    assert [doc for doc, _ in search_bm25(index, "same", k=3)] == [0, 1, 2]
