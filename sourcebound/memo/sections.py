"""The six memo sections: what each must cover, the fixed searches that feed it, and its metric table.

The memo is a fixed pipeline (decision D5): every company gets the same searches and the same table rows,
so the memo is repeatable and auditable. Rating rationale gets no new passages: it works from the scorecard
and the claims already verified in the earlier sections.
"""

from __future__ import annotations

from dataclasses import dataclass

PERIODS = ["FY-2", "FY-1", "FY0", "LTM"]
RATIOS = ["debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt"]


@dataclass(frozen=True)
class SectionSpec:
    id: str
    title: str
    instructions: str
    queries: tuple[str, ...]
    sections: frozenset[str] | None  # section filter for retrieval; None = all
    metric_keys: tuple[str, ...]


SECTION_SPECS = [
    SectionSpec(
        "business_profile", "Business profile",
        "Describe what the company does, its main businesses and markets, its scale (use the revenue and EBITDA "
        "placeholders), and anything in the passages that makes its cash flows more or less stable, such as "
        "diversification, market position or cyclicality.",
        ("business overview segments products customers", "competition market position strategy",
         "operations stores facilities employees"),
        frozenset({"business", "mdna"}),
        tuple(f"revenue:{p}" for p in PERIODS) + ("operating_income:FY0", "operating_income:LTM", "ebitda:FY0", "ebitda:LTM"),
    ),
    SectionSpec(
        "financial_risk", "Financial risk",
        "Assess leverage and debt service: debt / EBITDA, net leverage, EBITDA / interest and FCF / debt, and their "
        "trend from FY-2 to LTM (the trend words are given). Explain what drove the changes, using the passages "
        "(earnings, capital spending, debt issued or repaid).",
        ("results of operations operating income margin", "interest expense debt issuance repayment",
         "cash provided by operating activities capital expenditures"),
        frozenset({"mdna", "liquidity", "financial_statements"}),
        tuple(f"{r}:{p}" for r in RATIOS for p in PERIODS)
        + ("ebitda:LTM", "total_debt:FY0", "total_debt:LTM", "interest_expense:LTM", "cfo:LTM", "capex:LTM"),
    ),
    SectionSpec(
        "liquidity", "Liquidity",
        "Assess whether liquidity sources cover the next twelve months' needs: cash, undrawn credit facilities and "
        "cash from operations against debt due, capital expenditure and dividends. Use the liquidity coverage "
        "placeholder. Quote facility sizes and availability from the passages.",
        ("liquidity sources cash revolving credit facility", "commercial paper borrowing capacity undrawn available",
         "cash flows operating investing financing activities"),
        frozenset({"liquidity", "mdna", "debt_note"}),
        ("liquidity_coverage:FY0", "liquidity_coverage:LTM", "cash:LTM", "short_term_investments:LTM",
         "undrawn_revolver:LTM", "cfo:LTM", "capex:LTM", "dividends:LTM", "short_term_debt:LTM"),
    ),
    SectionSpec(
        "maturity_wall", "Maturity wall",
        "Describe the debt maturity profile: amounts due in each of the next five years and after, the share due "
        "within 24 months, near-term maturity cover, and any refinancing, repayment or covenant points in the "
        "passages.",
        ("debt maturities principal due next five years", "senior notes matured repaid refinanced issued",
         "credit agreement financial covenants compliance"),
        frozenset({"debt_note", "liquidity"}),
        ("maturity_year_1:FY0", "maturity_year_2:FY0", "maturity_year_3:FY0", "maturity_year_4:FY0",
         "maturity_year_5:FY0", "maturity_after_year_5:FY0", "debt_due_24m:FY0", "share_due_24m:FY0",
         "near_term_maturity_cover:FY0", "total_debt:FY0", "short_term_debt:FY0", "cash:FY0", "undrawn_revolver:FY0"),
    ),
    SectionSpec(
        "key_risks", "Key risks",
        "Identify the three to five risks most relevant to the company's ability to repay its debt, each grounded "
        "in a risk-factor passage. Prefer risks to cash flow, refinancing and access to credit over general ones.",
        ("indebtedness credit ratings borrowing costs access to capital", "economic conditions demand competition pricing",
         "interest rates refinancing liquidity risk"),
        frozenset({"risk_factors"}),
        ("debt_to_ebitda:LTM", "interest_coverage:LTM", "liquidity_coverage:LTM", "fcf_to_debt:LTM"),
    ),
    SectionSpec(
        "rating_rationale", "Rating rationale",
        "Explain the SB grade from the scorecard: which factors score strongest and weakest (use the value, band and "
        "weight placeholders), whether the grade is provisional, and how the earlier findings support or temper it. "
        "Say that the SB grade is a stylized internal scorecard grade, not a credit rating. Cite only passages already "
        "cited by the earlier findings.",
        (),
        None,
        (),  # filled from the scorecard at run time
    ),
]
