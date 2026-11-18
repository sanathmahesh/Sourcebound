"""Golden-set sheets (PLAN.md 4.17): blank templates the author fills in by hand from the latest 10-K.

Run:  uv run python -m sourcebound.pipeline.golden_templates

Writes evals/golden/<TICKER>.md for each golden company in config/companies.yaml, and
evals/agency_ratings.csv (header only) if missing. Existing files are never overwritten: once the author has
started filling a sheet in, it is theirs. The author fills values in before seeing Sourcebound's; a phase-5
script adds Sourcebound's values and the match column afterwards.

The derived rows use the same definitions as the engine (decisions D18-D21), so a hand-computed ratio
and Sourcebound's ratio measure the same thing.
"""

from __future__ import annotations

from pathlib import Path

from sourcebound.edgar.filings import filing_index_url
from sourcebound.engine.analysis import CompanyAnalysis
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT

GOLDEN_DIR = PROJECT_ROOT / "evals" / "golden"
AGENCY_FILE = PROJECT_ROOT / "evals" / "agency_ratings.csv"

INPUTS = [
    ("Revenue (total revenues)", "Income statement, top line"),
    ("Operating income (if there is no such line: pre-tax income from continuing operations + interest expense)",
     "Income statement"),
    ("Depreciation and amortisation", "Cash flow statement, operating activities"),
    ("Interest expense (including interest on finance leases)", "Income statement or interest note"),
    ("Cash and cash equivalents", "Balance sheet"),
    ("Short-term investments (0 if none)", "Balance sheet"),
    ("Short-term borrowings + current portion of long-term debt", "Balance sheet, current liabilities"),
    ("Long-term debt excluding current portion", "Balance sheet"),
    ("Finance-lease liabilities on their own lines, current + non-current (0 if inside the debt lines)",
     "Balance sheet or lease note"),
    ("Cash from operations", "Cash flow statement"),
    ("Capital expenditure", "Cash flow statement, investing activities"),
    ("Dividends paid (0 if none)", "Cash flow statement, financing activities"),
    ("Undrawn revolver capacity", "Liquidity section of MD&A, or the debt note"),
    ("Debt due in year 1", "Debt note, maturity table"),
    ("Debt due in year 2", "Debt note, maturity table"),
    ("Debt due in year 3", "Debt note, maturity table"),
    ("Debt due in year 4", "Debt note, maturity table"),
    ("Debt due in year 5", "Debt note, maturity table"),
    ("Debt due later than year 5", "Debt note, maturity table"),
]

DERIVED = [
    ("D1", "EBITDA", "2 + 3"),
    ("D2", "Total debt", "7 + 8 + 9"),
    ("D3", "Debt / EBITDA", "D2 / D1"),
    ("D4", "Net debt / EBITDA", "(D2 - 5 - 6) / D1"),
    ("D5", "EBITDA / interest", "D1 / 4"),
    ("D6", "FCF / debt (%)", "(10 - 11) / D2 x 100"),
    ("D7", "Liquidity coverage", "(5 + 6 + 13 + 10, using 0 for 10 if it is negative) / (7 + 11 + 12)"),
]

QUESTIONS = [
    ("Q1", "Size and expiry of the main revolving credit facility"),
    ("Q2", "Financial covenants, and whether the company states it complies"),
    ("Q3", "Largest single debt maturity in the next three years"),
    ("Q4", "Management's stated sources of liquidity"),
    ("Q5", "The risk factor most relevant to repaying debt"),
]


def render_golden_sheet(a: CompanyAnalysis) -> str:
    k = a.latest_10k
    lines = [
        f"# Golden-set sheet: {a.name} ({a.ticker})",
        "",
        "Fill in **Value in filing** from the 10-K below **before** looking at Sourcebound's figures. Leave a",
        "cell blank if the filing does not show the item; write 0 only when it shows zero or no such item.",
        "A script adds Sourcebound's values and a match column afterwards.",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Company | {a.name} |",
        f"| Ticker | {a.ticker} |",
        f"| Form 10-K, fiscal year ended | {k.report_date} |",
        f"| Accession number | {k.accession} |",
        f"| Filed | {k.filed} |",
        f"| Filing | {filing_index_url(a.cik, k.accession)} |",
        "| Units in filing (e.g. millions) | |",
        "| Verified by | |",
        "| Date verified | |",
        "",
        "## Inputs",
        "",
        "| # | Item | Where to look | Value in filing | Page or note |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| {n} | {item} | {where} | | |" for n, (item, where) in enumerate(INPUTS, start=1)]
    lines += [
        "",
        "## Derived, by calculator from your own values above",
        "",
        "| # | Item | Formula | Your value |",
        "|---|---|---|---|",
    ]
    lines += [f"| {code} | {item} | {formula} | |" for code, item, formula in DERIVED]
    lines += [
        "",
        "Pass rule: inputs match after rounding to the filing's unit; ratios within 0.05x or 1 percentage point.",
        "",
        "## Fact questions",
        "",
        "| # | Question | Answer | Exact location (section and page) |",
        "|---|---|---|---|",
    ]
    lines += [f"| {code} | {question} | | |" for code, question in QUESTIONS]
    return "\n".join(lines) + "\n"


def write_golden_sheet(a: CompanyAnalysis, out_dir: Path = GOLDEN_DIR) -> bool:
    """Write the sheet unless it already exists. Returns True if written."""
    path = out_dir / f"{a.ticker}.md"
    if path.exists():
        return False
    out_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(render_golden_sheet(a))
    return True


def main() -> None:
    from sourcebound.engine.concepts import load_concepts
    from sourcebound.pipeline.export import load_companies
    from sourcebound.pipeline.load import load_and_analyse, make_client

    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    client = make_client()
    for row in load_companies():
        if row["golden"]:
            written = write_golden_sheet(load_and_analyse(client, row["ticker"], specs))
            print(f"{row['ticker']}: {'written' if written else 'already exists, left untouched'}")
    if not AGENCY_FILE.exists():
        AGENCY_FILE.write_text("ticker,agency,rating,date,source\n")
        print(f"{AGENCY_FILE.relative_to(PROJECT_ROOT)}: header written")


if __name__ == "__main__":
    main()
