"""Cut a filing's text into passages ("chunks") for retrieval.

- Paragraphs (lines) are grouped, in order, into chunks of up to 1,500 characters; most end up 900-1,500.
- A paragraph longer than 1,500 characters is split at sentence ends (". "), or at a space if there is no
  sentence end.
- A chunk never crosses a section boundary, so every chunk has exactly one section label.
- Each chunk records its character offsets, and its text is exactly text[start:end]: a quote can always be
  checked against the source.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.edgar.sections import Span

MIN_CHARS = 900  # target lower bound (not enforced at a section's end)
MAX_CHARS = 1500


@dataclass(frozen=True)
class FilingMeta:
    ticker: str
    accession: str
    form: str
    filed: str
    period_end: str
    url: str


@dataclass(frozen=True)
class Chunk:
    id: str
    ticker: str
    accession: str
    form: str
    filed: str
    period_end: str
    section: str
    item: str
    heading: str
    start: int
    end: int
    url: str
    text: str


def _paragraphs(text: str, start: int, end: int) -> list[tuple[int, int]]:
    """(start, end) of each non-empty line inside [start, end), without surrounding spaces."""
    result = []
    position = start
    while position < end:
        line_end = text.find("\n", position, end)
        line_end = end if line_end == -1 else line_end
        line = text[position:line_end]
        stripped_start = position + (len(line) - len(line.lstrip()))
        stripped_end = position + len(line.rstrip())
        if stripped_end > stripped_start:
            result.append((stripped_start, stripped_end))
        position = line_end + 1
    return result


def _split_long(text: str, start: int, end: int) -> list[tuple[int, int]]:
    """Split one paragraph into pieces of at most MAX_CHARS, preferably after a full stop."""
    pieces = []
    position = start
    while end - position > MAX_CHARS:
        window = text[position:position + MAX_CHARS]
        cut = window.rfind(". ")
        if cut >= MAX_CHARS // 4:
            piece_end = position + cut + 1  # keep the full stop
        else:
            space = window.rfind(" ")
            piece_end = position + space if space > 0 else position + MAX_CHARS
        pieces.append((position, piece_end))
        position = piece_end
        while position < end and text[position].isspace():
            position += 1
    if end > position:
        pieces.append((position, end))
    return pieces


def _group(pieces: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge consecutive pieces while the merged chunk stays within MAX_CHARS."""
    chunks: list[list[int]] = []
    for start, end in pieces:
        if chunks and end - chunks[-1][0] <= MAX_CHARS:
            chunks[-1][1] = end
        else:
            chunks.append([start, end])
    return [(start, end) for start, end in chunks]


def chunk_filing(text: str, spans: list[Span], meta: FilingMeta) -> list[Chunk]:
    chunks = []
    for span in spans:
        pieces = [piece for s, e in _paragraphs(text, span.start, span.end) for piece in _split_long(text, s, e)]
        for start, end in _group(pieces):
            chunks.append(
                Chunk(
                    id=f"{meta.ticker}-{meta.accession.replace('-', '')}-{len(chunks):04d}",
                    ticker=meta.ticker,
                    accession=meta.accession,
                    form=meta.form,
                    filed=meta.filed,
                    period_end=meta.period_end,
                    section=span.label,
                    item=span.item,
                    heading=span.heading,
                    start=start,
                    end=end,
                    url=meta.url,
                    text=text[start:end],
                )
            )
    return chunks
