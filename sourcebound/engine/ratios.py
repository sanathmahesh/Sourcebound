"""The four core credit ratios, plus EBITDA, computed deterministically.

- EBITDA = operating income + depreciation and amortisation (unadjusted). A rough measure of the cash a
  business generates before paying lenders, tax and reinvestment.
- Debt / EBITDA (leverage): years of EBITDA needed to repay all debt. Higher is riskier.
- Net leverage = (debt - cash - short-term investments) / EBITDA. Negative net debt is shown as "net cash".
- EBITDA / interest (coverage): how many times earnings cover the interest bill. Lower is riskier.
- FCF / debt = (cash from operations - capital expenditure) / debt, in percent: the share of debt one
  year's free cash flow could repay.

Edge-case rules, in order of precedence:
1. Any input not available -> the ratio is not available (never estimated).
2. Zero debt -> debt / EBITDA is 0; net leverage is net cash (or 0 with no cash); FCF / debt is
   "not meaningful: no debt". This takes precedence over rule 3.
3. EBITDA at or below zero -> leverage, net leverage and coverage are "not meaningful".
4. Interest expense at or below zero -> coverage is "not meaningful".
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.engine.resolver import Resolved

NOT_AVAILABLE = "not_available"
NOT_MEANINGFUL = "not_meaningful"
NET_CASH = "net_cash"
OK = "ok"


@dataclass(frozen=True)
class RatioValue:
    value: float | None
    status: str
    reason: str = ""


@dataclass
class Ratio:
    """A computed metric for one period, with its formula and the resolved inputs behind it."""

    metric_id: str
    label: str
    period: str
    value: float | None
    unit: str  # "USD", "x" or "%"
    status: str
    formula: str
    reason: str
    inputs: list[Resolved]


def _missing(*values: float | None) -> bool:
    return any(v is None for v in values)


def ebitda(operating_income: float | None, d_and_a: float | None) -> float | None:
    if _missing(operating_income, d_and_a):
        return None
    return operating_income + d_and_a


def debt_to_ebitda(total_debt: float | None, ebitda_value: float | None) -> RatioValue:
    if _missing(total_debt, ebitda_value):
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    if total_debt == 0:
        return RatioValue(0.0, OK, "no debt")
    if ebitda_value <= 0:
        return RatioValue(None, NOT_MEANINGFUL, "EBITDA at or below zero")
    return RatioValue(total_debt / ebitda_value, OK)


def net_leverage(total_debt: float | None, cash: float | None, ebitda_value: float | None) -> RatioValue:
    """cash here is cash plus short-term investments."""
    if _missing(total_debt, cash, ebitda_value):
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    net_debt = total_debt - cash
    if total_debt == 0:
        if net_debt < 0:
            return RatioValue(net_debt / ebitda_value if ebitda_value > 0 else None, NET_CASH, "no debt; net cash")
        return RatioValue(0.0, OK, "no debt")
    if ebitda_value <= 0:
        return RatioValue(None, NOT_MEANINGFUL, "EBITDA at or below zero")
    if net_debt < 0:
        return RatioValue(net_debt / ebitda_value, NET_CASH, "cash exceeds debt")
    return RatioValue(net_debt / ebitda_value, OK)


def interest_coverage(ebitda_value: float | None, interest_expense: float | None) -> RatioValue:
    if _missing(ebitda_value, interest_expense):
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    if ebitda_value <= 0:
        return RatioValue(None, NOT_MEANINGFUL, "EBITDA at or below zero")
    if interest_expense <= 0:
        return RatioValue(None, NOT_MEANINGFUL, "interest expense at or below zero")
    return RatioValue(ebitda_value / interest_expense, OK)


def fcf_to_debt(cfo: float | None, capex: float | None, total_debt: float | None) -> RatioValue:
    """Free cash flow as a percentage of total debt."""
    if _missing(cfo, capex, total_debt):
        return RatioValue(None, NOT_AVAILABLE, "an input is not available")
    if total_debt == 0:
        return RatioValue(None, NOT_MEANINGFUL, "not meaningful: no debt")
    return RatioValue((cfo - capex) / total_debt * 100, OK)


def compute_ratios(values: dict[str, Resolved], period: str) -> list[Ratio]:
    """EBITDA and the four core ratios for one period, from that period's resolved concepts."""

    def v(concept: str) -> float | None:
        return values[concept].value

    def ratio(metric_id, label, unit, formula, concepts, result: RatioValue) -> Ratio:
        inputs = [values[c] for c in concepts]
        reason = result.reason
        if result.status == NOT_AVAILABLE:
            missing = [i.concept for i in inputs if i.status == "not_available"]
            reason = "not available: no value for " + ", ".join(missing)
        return Ratio(metric_id, label, period, result.value, unit, result.status, formula, reason, inputs)

    e = ebitda(v("operating_income"), v("d_and_a"))
    cash = None if _missing(v("cash"), v("short_term_investments")) else v("cash") + v("short_term_investments")
    ebitda_result = RatioValue(e, OK) if e is not None else RatioValue(None, NOT_AVAILABLE)
    ebitda_inputs = ["operating_income", "d_and_a"]
    return [
        ratio("ebitda", "EBITDA", "USD", "operating_income + d_and_a", ebitda_inputs, ebitda_result),
        ratio("debt_to_ebitda", "Debt / EBITDA", "x", "total_debt / EBITDA",
              ["total_debt", *ebitda_inputs], debt_to_ebitda(v("total_debt"), e)),
        ratio("net_leverage", "Net leverage", "x", "(total_debt - cash - short_term_investments) / EBITDA",
              ["total_debt", "cash", "short_term_investments", *ebitda_inputs], net_leverage(v("total_debt"), cash, e)),
        ratio("interest_coverage", "EBITDA / interest", "x", "EBITDA / interest_expense",
              [*ebitda_inputs, "interest_expense"], interest_coverage(e, v("interest_expense"))),
        ratio("fcf_to_debt", "FCF / debt", "%", "(cfo - capex) / total_debt",
              ["cfo", "capex", "total_debt"], fcf_to_debt(v("cfo"), v("capex"), v("total_debt"))),
    ]
