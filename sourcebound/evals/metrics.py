"""Eval metric functions (PLAN.md 4.11). Pure functions; every share is reported with its sample size."""

from __future__ import annotations

import re
from statistics import mean

RATIO_X_TOLERANCE = 0.05  # x
RATIO_PCT_TOLERANCE = 1.0  # percentage points


def share(hits: int, n: int) -> dict:
    return {"value": hits / n if n else None, "n": n}


def parse_hand_value(text: str) -> float | None:
    """A value as typed in a golden sheet: '6,596', '(217)', '$1.2', '18.2%', '4.38x'. Blank -> None."""
    cleaned = text.strip().replace(",", "").replace("$", "").replace("%", "").replace("x", "").strip()
    if not cleaned or cleaned in {"—", "-", "n/a", "na"}:
        return None
    negative = cleaned.startswith("(") and cleaned.endswith(")")
    cleaned = cleaned.strip("()")
    try:
        value = float(cleaned)
    except ValueError:
        return None
    return -value if negative else value


def _decimals(text: str) -> int:
    match = re.search(r"\.(\d+)", text)
    return len(match.group(1)) if match else 0


def matches(kind: str, engine: float, hand: str, unit: float) -> bool:
    """The plan's pass rule. amount: equal after rounding to the filing's unit (and the precision typed);
    ratio_x: within 0.05x; ratio_pct: within 1 percentage point."""
    value = parse_hand_value(hand)
    if value is None or engine is None:
        return False
    if kind == "amount":
        return round(engine / unit, _decimals(hand)) == value
    if kind == "ratio_x":
        return abs(engine - value) <= RATIO_X_TOLERANCE + 1e-9
    if kind == "ratio_pct":
        return abs(engine - value) <= RATIO_PCT_TOLERANCE + 1e-9
    raise ValueError(f"unknown kind {kind}")


def judge_agreement(human: list[str], judge: list[str]) -> dict:
    """Agreement with my labels, and the false-pass rate: the judge says 'supported' where I said
    'unsupported' (the dangerous error), out of the claims I labelled unsupported."""
    pairs = list(zip(human, judge))
    mine_unsupported = [j for h, j in pairs if h == "unsupported"]
    return {
        "agreement": share(sum(h == j for h, j in pairs), len(pairs)),
        "false_pass_rate": share(sum(j == "supported" for j in mine_unsupported), len(mine_unsupported)),
        "confusion": {f"{h}->{j}": sum(1 for a, b in pairs if (a, b) == (h, j)) for h, j in sorted(set(pairs))},
    }


def _ranks(values: list[float]) -> list[float]:
    """Ranks starting at 1; tied values share the average of their ranks."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return ranks


def spearman(x: list[float], y: list[float]) -> float | None:
    """Spearman rank correlation: the Pearson correlation of the ranks. None without variation."""
    rx, ry = _ranks(x), _ranks(y)
    mx, my = mean(rx), mean(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx, vy = sum((a - mx) ** 2 for a in rx), sum((b - my) ** 2 for b in ry)
    if vx == 0 or vy == 0:
        return None
    return cov / (vx * vy) ** 0.5


def spread(values: list[float]) -> dict:
    return {"mean": mean(values), "min": min(values), "max": max(values), "n": len(values)} if values else {"n": 0}
