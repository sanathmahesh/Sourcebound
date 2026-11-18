"""Company search index: deterministic build, round trip, section filters, corpus choice."""

import subprocess
import sys

from sourcebound.edgar.sections import Span
from sourcebound.retrieval.chunking import FilingMeta, chunk_filing
from sourcebound.retrieval.index import build_company_index, index_from_json, index_to_json, search
from tests.helpers import filing

META_K = FilingMeta("TEST", "0000000000-26-000001", "10-K", "2026-02-15", "2025-12-31", "https://example.invalid/k.htm")
META_Q = FilingMeta("TEST", "0000000000-26-000002", "10-Q", "2026-05-01", "2026-03-31", "https://example.invalid/q.htm")
K_TEXT = "ITEM 7.\nOur revolving credit facility of $5 billion matures in 2029.\nLiquidity\nWe have ample cash."
Q_TEXT = "Item 2.\nWe repaid the term loan.\nItem 1A. Risk Factors\nRising interest rates could raise our borrowing costs."


def build():
    k_chunks = chunk_filing(K_TEXT, [Span("mdna", "7", "ITEM 7.", 0, len(K_TEXT))], META_K)
    q_spans = [Span("mdna", "I-2", "Item 2.", 0, 33), Span("risk_factors", "II-1A", "Item 1A. Risk Factors", 33, len(Q_TEXT))]
    q_chunks = chunk_filing(Q_TEXT, q_spans, META_Q)
    return build_company_index("TEST", [META_K, META_Q], k_chunks + q_chunks)


def test_build_is_deterministic():
    assert index_to_json(build()) == index_to_json(build())


def test_round_trip_gives_the_same_results():
    index = build()
    again = index_from_json(index_to_json(index))
    assert [(h.chunk.id, h.score) for h in search(again, "credit facility")] == [
        (h.chunk.id, h.score) for h in search(index, "credit facility")
    ]


def test_search_returns_chunks_with_their_source():
    [hit, *_] = search(build(), "credit facility")
    assert hit.chunk.form == "10-K" and hit.chunk.section == "mdna"
    assert "revolving credit facility" in hit.chunk.text
    assert hit.chunk.url == "https://example.invalid/k.htm"


def test_section_and_form_filters():
    index = build()
    assert {h.chunk.section for h in search(index, "interest rates borrowing", sections={"risk_factors"})} == {"risk_factors"}
    assert search(index, "credit facility", forms={"10-Q"}) == []


def test_loading_the_index_imports_neither_the_edgar_client_nor_pandas():
    code = (
        "import sys, sourcebound.retrieval.index;"
        "print('sourcebound.edgar.client' in sys.modules, 'pandas' in sys.modules)"
    )
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True).stdout.strip()
    assert out == "False False"


def test_corpus_is_latest_10k_and_later_10qs():
    from sourcebound.pipeline.build_index import corpus_filings

    filings = [
        filing("10-Q", "q3", "2026-11-01", "2026-09-30"),
        filing("10-Q", "q2", "2026-08-01", "2026-06-30"),
        filing("10-Q/A", "qa", "2026-08-15", "2026-06-30"),
        filing("10-K", "k", "2026-02-15", "2025-12-31"),
        filing("10-Q", "old", "2025-11-01", "2025-09-30"),
    ]
    k = filings[3]
    assert [f.accession for f in corpus_filings(filings, k)] == ["k", "q2", "q3"]
