"""The timing log (evals/timings.csv): manual against tool-assisted effort, recorded only by the author.

Each row is one timed task. The summary is the median minutes and the count per task and condition, plus
the errors found later; with no rows, every figure is "not measured". Nothing here estimates a timing.
"""

from __future__ import annotations

import csv
import statistics
from dataclasses import dataclass
from pathlib import Path

TIMING_COLUMNS = ["date", "company", "condition", "task", "start", "end", "minutes", "errors found later", "notes"]
CONDITIONS = ("manual", "tool-assisted")


@dataclass(frozen=True)
class Timing:
    date: str
    company: str
    condition: str
    task: str
    minutes: float
    errors_found_later: int


@dataclass(frozen=True)
class TimingSummary:
    task: str
    condition: str
    n: int
    median_minutes: float
    errors_found_later: int


def read_timings(path: Path) -> list[Timing]:
    """Rows of the log; a malformed row is an error, never skipped or guessed."""
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != TIMING_COLUMNS:
            raise ValueError(f"{path}: columns must be {', '.join(TIMING_COLUMNS)}")
        timings = []
        for line, row in enumerate(reader, start=2):
            if row["condition"] not in CONDITIONS:
                raise ValueError(f"{path} line {line}: condition must be manual or tool-assisted")
            try:
                minutes = float(row["minutes"])
                errors = int(row["errors found later"] or 0)
            except ValueError:
                raise ValueError(f"{path} line {line}: minutes and errors found later must be numbers") from None
            timings.append(Timing(row["date"], row["company"], row["condition"], row["task"], minutes, errors))
    return timings


def summarise(timings: list[Timing]) -> list[TimingSummary]:
    groups: dict[tuple[str, str], list[Timing]] = {}
    for t in timings:
        groups.setdefault((t.task, t.condition), []).append(t)
    return [TimingSummary(task, condition, len(rows), statistics.median(r.minutes for r in rows),
                          sum(r.errors_found_later for r in rows))
            for (task, condition), rows in sorted(groups.items())]
