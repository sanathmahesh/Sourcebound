"""Pick about eight passages for a memo section: fixed queries, a section filter, merge, de-duplicate.

- Each query runs with the section filter. A passage's position is its best rank across the queries (ties go
  to the higher BM25 score).
- 10-Qs repeat earlier text, so near-duplicates (90% of words shared) are collapsed into the most recently
  filed copy.
- If the filter leaves fewer than four passages, the search is widened to all sections, and that is noted.
"""

from __future__ import annotations

from sourcebound.memo.sections import SectionSpec
from sourcebound.retrieval.bm25 import tokenize
from sourcebound.retrieval.chunking import Chunk
from sourcebound.retrieval.index import CompanyIndex, Hit, search

PASSAGES_PER_SECTION = 8
MIN_FILTERED = 4
DUPLICATE_OVERLAP = 0.9


def near_duplicate(a: Chunk, b: Chunk) -> bool:
    words_a, words_b = set(tokenize(a.text)), set(tokenize(b.text))
    if not words_a or not words_b:
        return a.text == b.text
    return len(words_a & words_b) / len(words_a | words_b) >= DUPLICATE_OVERLAP


def merge_hits(hit_lists: list[list[Hit]], limit: int = PASSAGES_PER_SECTION) -> list[Chunk]:
    best: dict[str, tuple[int, float, Chunk]] = {}
    for hits in hit_lists:
        for hit in hits:
            current = best.get(hit.chunk.id)
            if current is None or (hit.rank, -hit.score) < (current[0], -current[1]):
                best[hit.chunk.id] = (hit.rank, hit.score, hit.chunk)
    kept: list[Chunk] = []
    for _, _, chunk in sorted(best.values(), key=lambda item: (item[0], -item[1], item[2].id)):
        twin = next((n for n, k in enumerate(kept) if near_duplicate(k, chunk)), None)
        if twin is None:
            kept.append(chunk)
        elif chunk.filed > kept[twin].filed:
            kept[twin] = chunk
        if len(kept) >= limit and twin is None:
            break
    return kept[:limit]


def retrieve_for_section(index: CompanyIndex, spec: SectionSpec) -> tuple[list[Chunk], list[str]]:
    sections = set(spec.sections) if spec.sections else None
    passages = merge_hits([search(index, q, k=PASSAGES_PER_SECTION, sections=sections) for q in spec.queries])
    notes = []
    if len(passages) < MIN_FILTERED and sections is not None:
        notes.append(f"only {len(passages)} passages in {sorted(sections)}; search widened to all sections")
        widened = [search(index, q, k=PASSAGES_PER_SECTION) for q in spec.queries]
        passages = merge_hits([[Hit(n + 1, 0.0, c) for n, c in enumerate(passages)]] + widened)
    return passages, notes
