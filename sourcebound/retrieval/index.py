"""One search index per company, saved as a JSON file (data/index/<TICKER>.json).

The file holds the passages (with their source and offsets), the BM25 statistics and the inverted index,
so searching needs no network and no model. It is written deterministically (same input, same bytes).
This module imports neither the EDGAR client nor pandas: the live API loads it.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from sourcebound.paths import PROJECT_ROOT
from sourcebound.retrieval.bm25 import STOPWORDS, TOKEN, Bm25Index, build_bm25, search_bm25
from sourcebound.retrieval.chunking import Chunk, FilingMeta

INDEX_DIR = PROJECT_ROOT / "data" / "index"
SCHEMA_VERSION = "1"


@dataclass
class CompanyIndex:
    ticker: str
    filings: list[FilingMeta]
    chunks: list[Chunk]
    bm25: Bm25Index


@dataclass(frozen=True)
class Hit:
    rank: int
    score: float
    chunk: Chunk


def build_company_index(ticker: str, filings: list[FilingMeta], chunks: list[Chunk]) -> CompanyIndex:
    return CompanyIndex(ticker, filings, chunks, build_bm25([c.text for c in chunks]))


def search(
    index: CompanyIndex,
    query: str,
    k: int = 8,
    sections: set[str] | None = None,
    forms: set[str] | None = None,
) -> list[Hit]:
    """The k best passages for the query, optionally only from some sections or forms."""
    allowed = None
    if sections is not None or forms is not None:
        allowed = {
            n for n, c in enumerate(index.chunks)
            if (sections is None or c.section in sections) and (forms is None or c.form in forms)
        }
    results = search_bm25(index.bm25, query, k, allowed)
    return [Hit(rank, score, index.chunks[n]) for rank, (n, score) in enumerate(results, start=1)]


def index_to_json(index: CompanyIndex) -> str:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "ticker": index.ticker,
        "params": {"k1": index.bm25.k1, "b": index.bm25.b, "token_pattern": TOKEN.pattern,
                   "stopwords": sorted(STOPWORDS)},
        "filings": [asdict(f) for f in index.filings],
        "chunks": [asdict(c) for c in index.chunks],
        "doc_lengths": index.bm25.doc_lengths,
        "avg_length": index.bm25.avg_length,
        "postings": {term: [list(p) for p in plist] for term, plist in index.bm25.postings.items()},
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def index_from_json(text: str) -> CompanyIndex:
    data = json.loads(text)
    bm25 = Bm25Index(
        k1=data["params"]["k1"],
        b=data["params"]["b"],
        doc_lengths=data["doc_lengths"],
        avg_length=data["avg_length"],
        postings={term: [tuple(p) for p in plist] for term, plist in data["postings"].items()},
    )
    return CompanyIndex(
        ticker=data["ticker"],
        filings=[FilingMeta(**f) for f in data["filings"]],
        chunks=[Chunk(**c) for c in data["chunks"]],
        bm25=bm25,
    )


def load_index(ticker: str, directory: Path = INDEX_DIR) -> CompanyIndex:
    return index_from_json((directory / f"{ticker.upper()}.json").read_text())


def save_index(index: CompanyIndex, directory: Path = INDEX_DIR) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{index.ticker}.json"
    path.write_text(index_to_json(index))
    return path
