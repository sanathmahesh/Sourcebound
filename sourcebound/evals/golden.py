"""Read a golden-set sheet the author filled in, and compare it with the engine (PLAN.md 4.17).

The sheet is never modified. The comparison applies the plan's pass rule: inputs equal after rounding to the
filing's unit; ratios within 0.05x; FCF / debt within 1 percentage point.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.contracts import CompanyMetrics
from sourcebound.evals.metrics import matches, parse_hand_value

# Golden row -> (engine metric key, kind). Rows 8 and 9 are derived from total debt's lineage.
ROWS = {
    "1": ("revenue:FY0", "amount"), "2": ("operating_income:FY0", "amount"), "3": ("d_and_a:FY0", "amount"),
    "4": ("interest_expense:FY0", "amount"), "5": ("cash:FY0", "amount"),
    "6": ("short_term_investments:FY0", "amount"), "7": ("short_term_debt:FY0", "amount"),
    "8": ("long_term_debt_excluding_current:FY0", "amount"), "9": ("finance_leases_on_own_lines:FY0", "amount"),
    "10": ("cfo:FY0", "amount"), "11": ("capex:FY0", "amount"), "12": ("dividends:FY0", "amount"),
    "13": ("undrawn_revolver:FY0", "amount"), "14": ("maturity_year_1:FY0", "amount"),
    "15": ("maturity_year_2:FY0", "amount"), "16": ("maturity_year_3:FY0", "amount"),
    "17": ("maturity_year_4:FY0", "amount"), "18": ("maturity_year_5:FY0", "amount"),
    "19": ("maturity_after_year_5:FY0", "amount"),
    "D1": ("ebitda:FY0", "amount"), "D2": ("total_debt:FY0", "amount"), "D3": ("debt_to_ebitda:FY0", "ratio_x"),
    "D4": ("net_leverage:FY0", "ratio_x"), "D5": ("interest_coverage:FY0", "ratio_x"),
    "D6": ("fcf_to_debt:FY0", "ratio_pct"), "D7": ("liquidity_coverage:FY0", "ratio_x"),
}
UNITS = {"thousand": 1e3, "million": 1e6, "billion": 1e9}


@dataclass(frozen=True)
class FactQuestion:
    id: str
    question: str
    answer: str
    location: str
    quote: str


@dataclass
class GoldenSheet:
    unit: float | None
    values: dict[str, str]  # row id ("1".."19", "D1".."D7") -> text as typed
    facts: list[FactQuestion]


@dataclass(frozen=True)
class RowResult:
    row: str
    key: str
    kind: str
    hand: str
    engine: float | None
    status: str  # match | mismatch | engine_missing | not_filled | units_missing


def parse_golden_sheet(text: str) -> GoldenSheet:
    unit, values, facts = None, {}, []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        first = cells[0]
        if first.lower().startswith("units in filing"):
            unit = next((u for word, u in UNITS.items() if word in cells[1].lower()), None)
        elif first.isdigit() and len(cells) >= 4:
            values[first] = cells[3]
        elif first.startswith("D") and first[1:].isdigit() and len(cells) >= 4:
            values[first] = cells[3]
        elif first.startswith("Q") and first[1:].isdigit() and len(cells) >= 4:
            facts.append(FactQuestion(first, cells[1], cells[2], cells[3], cells[4] if len(cells) > 4 else ""))
    return GoldenSheet(unit, values, facts)


def engine_value(cm: CompanyMetrics, key: str) -> float | None:
    if key in ("long_term_debt_excluding_current:FY0", "finance_leases_on_own_lines:FY0"):
        debt, short = cm.metrics.get("total_debt:FY0"), cm.metrics.get("short_term_debt:FY0")
        if debt is None or debt.value is None:
            return None
        leases = sum(i.value * i.sign for i in debt.inputs if i.concept == "finance_lease_liabilities")
        if key.startswith("finance"):
            return leases
        return None if short is None or short.value is None else debt.value - short.value - leases
    metric = cm.metrics.get(key)
    if metric is None or metric.status == "not_available":
        return None
    return metric.value


def compare_sheet(sheet: GoldenSheet, cm: CompanyMetrics) -> list[RowResult]:
    results = []
    for row, (key, kind) in ROWS.items():
        hand = sheet.values.get(row, "")
        engine = engine_value(cm, key)
        if parse_hand_value(hand) is None:
            status = "not_filled"
        elif kind == "amount" and sheet.unit is None:
            status = "units_missing"
        elif engine is None:
            status = "engine_missing"
        else:
            status = "match" if matches(kind, engine, hand, sheet.unit or 1.0) else "mismatch"
        results.append(RowResult(row, key, kind, hand, engine, status))
    return results
