"""Layer (b), deterministic part: is each citation's quote really in the passage it cites?

Quotes are compared after normalisation: lower case, straight quotes and hyphens, single spaces. A quote
must be at least three words, so "the" cannot "support" a claim. No model is involved.
"""

from __future__ import annotations

import re

MIN_QUOTE_WORDS = 3
_TRANSLATE = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
                            "\xa0": " "})


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text.translate(_TRANSLATE)).strip().lower()


def check_quote(quote: str, passage_text: str | None) -> str:
    """'ok', 'chunk_not_found', 'quote_too_short' or 'quote_not_found'."""
    if passage_text is None:
        return "chunk_not_found"
    cleaned = normalise(quote).strip(" \"'…").rstrip(".").strip()
    if len(cleaned.split()) < MIN_QUOTE_WORDS:
        return "quote_too_short"
    return "ok" if cleaned in normalise(passage_text) else "quote_not_found"
