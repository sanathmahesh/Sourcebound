"""Load and check the scorecard grid in config/grid.yaml.

The grid is data, not code, so the author can read and approve it, and it is frozen with a git tag before
the scores are compared with anything outside the project.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Factor:
    id: str  # equals the metric id it scores, e.g. "debt_to_ebitda"
    label: str
    weight: float
    higher_is_better: bool
    thresholds: tuple[float, ...]  # five cut points, from the strongest band to the weakest


@dataclass(frozen=True)
class Grid:
    version: str
    tie_rule: str  # "worse": a value exactly on a threshold gets the worse score
    factors: tuple[Factor, ...]
    grades: tuple[tuple[float, str], ...]  # (upper bound of the weighted score, grade), ascending
    worst_grade: str
    ig_like_max: float


def load_grid(path: Path) -> Grid:
    return parse_grid(yaml.safe_load(path.read_text()))


def parse_grid(raw: dict) -> Grid:
    factors = tuple(
        Factor(
            id=f["id"],
            label=f["label"],
            weight=float(f["weight"]),
            higher_is_better=bool(f["higher_is_better"]),
            thresholds=tuple(f["thresholds"]),
        )
        for f in raw["factors"]
    )
    grid = Grid(
        version=raw["version"],
        tie_rule=raw["tie_rule"],
        factors=factors,
        grades=tuple((float(cut), grade) for cut, grade in raw["grades"]),
        worst_grade=raw["worst_grade"],
        ig_like_max=float(raw["ig_like_max"]),
    )
    _check(grid)
    return grid


def _check(grid: Grid) -> None:
    if grid.tie_rule != "worse":
        raise ValueError("tie_rule must be 'worse' (the approved rule)")
    if abs(sum(f.weight for f in grid.factors) - 1.0) > 1e-9:
        raise ValueError(f"factor weights must sum to 1, got {sum(f.weight for f in grid.factors)}")
    for f in grid.factors:
        steps = list(zip(f.thresholds, f.thresholds[1:]))
        ordered = all(a > b for a, b in steps) if f.higher_is_better else all(a < b for a, b in steps)
        if len(f.thresholds) != 5 or not ordered:
            raise ValueError(f"{f.id}: thresholds must be five values running from the strongest band to the weakest")
    cuts = [cut for cut, _ in grid.grades]
    if cuts != sorted(cuts):
        raise ValueError("grade cutoffs must be ascending")
