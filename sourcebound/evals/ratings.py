"""Agency rating scales, for comparing SB grades with ratings the author enters by hand.

Only eval code reads evals/agency_ratings.csv; the scorecard never does (a test enforces it).
S&P and Fitch: AAA, AA+, AA, ... D. Moody's: Aaa, Aa1, ... C. Both map to one numeric scale, 1 = strongest.
Investment grade (IG) is BBB- / Baa3 (rank 10) or better.
"""

from __future__ import annotations

import csv
from pathlib import Path

SP_FITCH = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-", "BB+", "BB", "BB-", "B+", "B", "B-",
            "CCC+", "CCC", "CCC-", "CC", "C", "D"]
MOODYS = ["Aaa", "Aa1", "Aa2", "Aa3", "A1", "A2", "A3", "Baa1", "Baa2", "Baa3", "Ba1", "Ba2", "Ba3", "B1", "B2", "B3",
          "Caa1", "Caa2", "Caa3", "Ca", "C"]
IG_WORST_RANK = 10


def rating_rank(rating: str) -> int:
    text = rating.strip()
    if text in MOODYS:
        return MOODYS.index(text) + 1
    if text.upper() in SP_FITCH:
        return SP_FITCH.index(text.upper()) + 1
    if text.upper() == "SD":
        return len(SP_FITCH)
    raise ValueError(f"unrecognised rating {rating!r}")


def ig_from_rating(rating: str) -> bool:
    return rating_rank(rating) <= IG_WORST_RANK


def load_agency_ratings(path: Path) -> dict[str, list[dict]]:
    """ticker -> rows (agency, rating, date, source). Empty if the author has entered none."""
    by_ticker: dict[str, list[dict]] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            if row.get("ticker") and row.get("rating"):
                by_ticker.setdefault(row["ticker"].strip().upper(), []).append(row)
    return by_ticker


def company_rank(rows: list[dict]) -> float:
    """One number per company: the average rank across the agencies entered."""
    ranks = [rating_rank(r["rating"]) for r in rows]
    return sum(ranks) / len(ranks)
