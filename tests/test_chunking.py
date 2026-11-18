"""Chunking: offsets reproduce the source text, sizes, and chunks never cross a section boundary."""

import gzip
from pathlib import Path

from sourcebound.edgar.sections import Span, detect_sections
from sourcebound.retrieval.chunking import MAX_CHARS, FilingMeta, chunk_filing

FILINGS = Path(__file__).parent / "fixtures" / "filings"
META = FilingMeta(ticker="TEST", accession="0000000000-26-000001", form="10-K", filed="2026-02-15",
                  period_end="2025-12-31", url="https://example.invalid/doc.htm")


def test_offsets_reproduce_the_source_text_and_sizes_are_bounded():
    text = "\n".join(f"Paragraph {i}. " + "Words about debt. " * (i % 7 + 1) for i in range(300))
    chunks = chunk_filing(text, [Span("unlabelled", "", "", 0, len(text))], META)
    assert chunks
    for chunk in chunks:
        assert text[chunk.start:chunk.end] == chunk.text
        assert len(chunk.text) <= MAX_CHARS


def test_a_long_paragraph_is_split_at_sentence_ends():
    text = "This sentence is about the credit facility and its covenants. " * 80  # one 5,000-char paragraph
    chunks = chunk_filing(text, [Span("unlabelled", "", "", 0, len(text))], META)
    assert len(chunks) >= 4
    for chunk in chunks:
        assert text[chunk.start:chunk.end] == chunk.text
        assert len(chunk.text) <= MAX_CHARS
        assert chunk.text.endswith(".")


def test_chunks_never_cross_sections_and_carry_labels():
    text = "A" * 50 + "\n" + "B" * 50 + "\n" + "C" * 50
    spans = [Span("business", "1", "h", 0, 51), Span("risk_factors", "1A", "h2", 51, len(text))]
    chunks = chunk_filing(text, spans, META)
    assert [(c.section, c.item, c.text) for c in chunks] == [
        ("business", "1", "A" * 50),
        ("risk_factors", "1A", "B" * 50 + "\n" + "C" * 50),
    ]


def test_ids_are_stable_and_unique():
    text = "\n".join("Paragraph text. " * 30 for _ in range(20))
    first = chunk_filing(text, [Span("unlabelled", "", "", 0, len(text))], META)
    second = chunk_filing(text, [Span("unlabelled", "", "", 0, len(text))], META)
    assert [c.id for c in first] == [c.id for c in second]
    assert len({c.id for c in first}) == len(first)
    assert first[0].id == "TEST-000000000026000001-0000"


def test_real_filing_offsets_reproduce_text():
    with gzip.open(FILINGS / "WMT-10-K-0000104169-26-000055.txt.gz", "rt", encoding="utf-8") as f:
        text = f.read()
    chunks = chunk_filing(text, detect_sections(text, "10-K"), META)
    assert all(text[c.start:c.end] == c.text for c in chunks)
    assert all(len(c.text) <= MAX_CHARS for c in chunks)
    sizes = sorted(len(c.text) for c in chunks)
    assert sizes[len(sizes) // 2] >= 900  # the median chunk is in the 900-1,500 range
    assert {"business", "risk_factors", "mdna", "liquidity", "debt_note"} <= {c.section for c in chunks}
