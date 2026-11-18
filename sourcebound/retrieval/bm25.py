"""BM25 keyword search, small enough to explain line by line.

BM25 scores a passage for a query by adding up, for each query word the passage contains:

    idf(word) * tf * (k1 + 1) / (tf + k1 * (1 - b + b * length / average_length))

- tf: how often the word appears in the passage. More is better, with diminishing returns (k1 = 1.5 sets
  how fast the benefit saturates).
- length / average_length: long passages get a small penalty, since they contain more words by chance
  (b = 0.75 sets how much).
- idf(word) = ln((N - df + 0.5) / (df + 0.5) + 1), where N is the number of passages and df the number
  containing the word. Rare words ("covenant") count for much more than common ones ("company"). The "+ 1"
  keeps it positive even for a word in every passage.

Words are lowercase runs of letters and digits; a short list of very common words is ignored.
The index is an "inverted index": for each word, the passages containing it and how often.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import log

K1 = 1.5
B = 0.75
TOKEN = re.compile(r"[a-z0-9]+")
STOPWORDS = frozenset(
    "a an and are as at be by for from has have in is it its of on or our that the this to was we were "
    "which will with".split()
)


def tokenize(text: str) -> list[str]:
    return [token for token in TOKEN.findall(text.lower()) if token not in STOPWORDS]


@dataclass
class Bm25Index:
    k1: float
    b: float
    doc_lengths: list[int]  # number of tokens in each passage
    avg_length: float
    postings: dict[str, list[tuple[int, int]]]  # word -> [(passage number, tf), ...]


def build_bm25(docs: list[str], k1: float = K1, b: float = B) -> Bm25Index:
    postings: dict[str, list[tuple[int, int]]] = defaultdict(list)
    lengths = []
    for doc_number, doc in enumerate(docs):
        tokens = tokenize(doc)
        lengths.append(len(tokens))
        for term, tf in sorted(Counter(tokens).items()):
            postings[term].append((doc_number, tf))
    average = sum(lengths) / len(lengths) if lengths else 0.0
    return Bm25Index(k1, b, lengths, average, dict(sorted(postings.items())))


def idf(n_docs: int, doc_freq: int) -> float:
    return log((n_docs - doc_freq + 0.5) / (doc_freq + 0.5) + 1)


def search_bm25(index: Bm25Index, query: str, k: int, allowed: set[int] | None = None) -> list[tuple[int, float]]:
    """The k best-scoring passages for the query, best first; ties go to the earlier passage.

    allowed restricts the passages considered (e.g. one section); word rarity is still measured over all.
    """
    n_docs = len(index.doc_lengths)
    scores: dict[int, float] = defaultdict(float)
    for term in dict.fromkeys(tokenize(query)):  # each query word once, in order
        postings = index.postings.get(term)
        if not postings:
            continue
        term_idf = idf(n_docs, len(postings))
        for doc_number, tf in postings:
            if allowed is not None and doc_number not in allowed:
                continue
            length_ratio = index.doc_lengths[doc_number] / index.avg_length if index.avg_length else 0.0
            scores[doc_number] += term_idf * tf * (index.k1 + 1) / (
                tf + index.k1 * (1 - index.b + index.b * length_ratio)
            )
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:k]
