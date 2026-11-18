"""Section detection on synthetic text and on three saved real filings.

Expected headings below were read directly from the saved texts (tests/fixtures/filings/), not from the
parser's output.
"""

import gzip
from pathlib import Path

import pytest

from sourcebound.edgar.sections import detect_sections

FILINGS = Path(__file__).parent / "fixtures" / "filings"


def saved(name: str) -> str:
    with gzip.open(FILINGS / name, "rt", encoding="utf-8") as f:
        return f.read()


def spans_by_label(spans, label):
    return [s for s in spans if s.label == label]


def heading_of(spans, label) -> str:
    """The heading a label came from. MD&A and financial statements can be split in two around their
    liquidity or debt-note subsection; both parts carry the parent's heading."""
    found = spans_by_label(spans, label)
    assert found, f"no {label} span"
    assert len({s.heading for s in found}) == 1
    return found[0].heading


def assert_partition(text, spans):
    """Spans are ordered, contiguous and cover the whole document."""
    assert spans[0].start == 0 and spans[-1].end == len(text)
    for a, b in zip(spans, spans[1:]):
        assert a.end == b.start


# ----- synthetic ---------------------------------------------------------------------------------------

SYNTHETIC_10K = "\n".join([
    "Cover page",
    "Table of Contents",
    "Item 1", "Item 1A", "Item 7", "Item 8",  # contents entries: tiny spans
    "ITEM 1. BUSINESS",
    "We sell things. " * 20,
    "ITEM 1A. RISK FACTORS",
    "Debt is risky. " * 20,
    "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS",
    "Overview text. " * 20,
    "Liquidity and Capital Resources",
    "We have a revolving credit facility. " * 20,
    "Critical Accounting Estimates",
    "Estimates text. " * 20,
    "ITEM 8. FINANCIAL STATEMENTS",
    "Note 1. Accounting Policies",
    "Policies text. " * 20,
    "Note 2. Debt",
    "Our notes mature in 2030. " * 20,
    "Note 3. Leases",
    "Lease text. " * 20,
])


def test_synthetic_10k_sections():
    spans = detect_sections(SYNTHETIC_10K, "10-K")
    assert_partition(SYNTHETIC_10K, spans)
    assert [s.label for s in spans] == [
        "unlabelled", "business", "risk_factors", "mdna", "liquidity", "mdna",
        "financial_statements", "debt_note", "financial_statements",
    ]
    assert heading_of(spans, "liquidity") == "Liquidity and Capital Resources"
    assert heading_of(spans, "debt_note") == "Note 2. Debt"
    # the contents entries stay in the unlabelled front matter
    assert "Item 1A" in SYNTHETIC_10K[spans[0].start:spans[0].end]


def test_no_item_headings_means_one_unlabelled_span():
    text = "Some document\nwith no item headings at all."
    spans = detect_sections(text, "10-K")
    assert [(s.label, s.start, s.end) for s in spans] == [("unlabelled", 0, len(text))]


def test_10q_parts_distinguish_repeated_item_numbers():
    text = "\n".join([
        "PART I - FINANCIAL INFORMATION",
        "Item 1. Financial Statements",
        "Statements. " * 30,
        "Item 2. Management's Discussion and Analysis",
        "Discussion. " * 30,
        "PART II - OTHER INFORMATION",
        "Item 1. Legal Proceedings",
        "Legal. " * 5,
        "Item 1A. Risk Factors",
        "Risk update. " * 10,
    ])
    labels = [s.label for s in detect_sections(text, "10-Q")]
    assert labels == ["unlabelled", "financial_statements", "mdna", "other_item", "risk_factors"]


# ----- three saved filings ----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def wmt():
    text = saved("WMT-10-K-0000104169-26-000055.txt.gz")
    return text, detect_sections(text, "10-K")


@pytest.fixture(scope="module")
def gt():
    text = saved("GT-10-K-0001628280-26-006708.txt.gz")
    return text, detect_sections(text, "10-K")


@pytest.fixture(scope="module")
def vz():
    text = saved("VZ-10-Q-0000732712-26-000052.txt.gz")
    return text, detect_sections(text, "10-Q")


def test_wmt_10k(wmt):
    text, spans = wmt
    assert_partition(text, spans)
    assert heading_of(spans, "business") == "ITEM 1. BUSINESS"
    assert heading_of(spans, "risk_factors") == "ITEM 1A. RISK FACTORS"
    assert heading_of(spans, "market_risk") == "ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK"
    assert heading_of(spans, "financial_statements") == "ITEM 8. FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA"
    assert heading_of(spans, "liquidity") == "Liquidity and Capital Resources"
    assert heading_of(spans, "debt_note") == "Note 5. Short-term Borrowings and Long-term Debt"
    [debt] = spans_by_label(spans, "debt_note")
    assert text[debt.end:].startswith("Note 6. Leases")
    [liquidity] = spans_by_label(spans, "liquidity")
    assert text[liquidity.end:].startswith("Other Matters")
    mdna = spans_by_label(spans, "mdna")
    assert mdna[0].heading.startswith("ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS")


def test_gt_10k_picks_the_full_liquidity_section_not_the_overview_line(gt):
    text, spans = gt
    assert_partition(text, spans)
    assert heading_of(spans, "liquidity") == "LIQUIDITY AND CAPITAL RESOURCES"
    [liquidity] = spans_by_label(spans, "liquidity")
    assert text[liquidity.end:].startswith("COMMITMENTS AND CONTINGENT LIABILITIES")
    assert heading_of(spans, "debt_note") == "Note 16. Financing Arrangements and Derivative Financial Instruments"
    assert heading_of(spans, "business") == "ITEM 1. BUSINESS."


def test_vz_10q(vz):
    text, spans = vz
    assert_partition(text, spans)
    assert heading_of(spans, "financial_statements") == "Item 1. Financial Statements (Unaudited)"
    assert heading_of(spans, "market_risk") == "Item 3. Quantitative and Qualitative Disclosures About Market Risk"
    assert heading_of(spans, "risk_factors") == "Item 1A. Risk Factors"
    assert heading_of(spans, "liquidity") == "Consolidated Financial Condition"
    [liquidity] = spans_by_label(spans, "liquidity")
    assert text[liquidity.end:].startswith("Market Risk")
    assert heading_of(spans, "debt_note") == "Note 5. Debt"
    # Part II Item 1 (legal proceedings) is not mistaken for Part I Item 1
    assert any(s.label == "other_item" and s.heading == "Item 1. Legal Proceedings" for s in spans)


# ----- patterns found across the 15 companies (phase 3 section-coverage review) ------------------------

FILLER = "Text about the business and its operations. " * 12


def test_repeated_page_headers_do_not_cut_a_section_short():
    """HCA's 10-Qs repeat 'ITEM 2. MANAGEMENT'S DISCUSSION ...' at the top of every page."""
    text = "\n".join([
        "PART I", "Item 1. Financial Statements", FILLER,
        "ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS OF", FILLER,
        "ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS OF", FILLER,
        "ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS OF", FILLER * 3,  # the longest page is the last
        "Item 3. Quantitative and Qualitative Disclosures About Market Risk", FILLER,
    ])
    spans = detect_sections(text, "10-Q")
    [mdna] = spans_by_label(spans, "mdna")
    assert text[mdna.end:].startswith("Item 3.")
    assert mdna.start == text.index("ITEM 2.")


def test_10q_titles_identify_part_one_items_without_a_part_heading():
    """Community Health's 10-Qs have contents entries for Parts I and II, then no 'Part I' in the body."""
    text = "\n".join([
        "Part I.", "Item 1.", "Item 2.", "Part II.", "Item 1.", "Item 1A.",
        "Item 1. Financial Statements", FILLER,
        "Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations", FILLER,
        "PART II OTHER INFORMATION", "Item 1. Legal Proceedings", FILLER,
        "Item 1A. Risk Factors", FILLER,
    ])
    spans = detect_sections(text, "10-Q")
    assert heading_of(spans, "financial_statements") == "Item 1. Financial Statements"
    assert heading_of(spans, "mdna").startswith("Item 2. Management's Discussion")
    assert heading_of(spans, "risk_factors") == "Item 1A. Risk Factors"


def test_an_untitled_contents_entry_loses_to_a_titled_body_heading():
    """HCA's 10-Q: the last contents entry ('Item 6.') would otherwise swallow the statements that follow,
    because the body has no 'Item 1' heading. A titled heading ('Item 6. Exhibits') beats an untitled one."""
    text = "\n".join([
        "Part I.", "Item 1.", "Item 2.", "Part II.", "Item 6.",
        FILLER * 3,  # financial statements with no body 'Item 1' heading
        "ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS", FILLER,
        "PART II", "Item 6. Exhibits", "List of exhibits.",
    ])
    spans = detect_sections(text, "10-Q")
    statements = spans_by_label(spans, "financial_statements")
    assert statements and FILLER[:40] in text[statements[0].start:statements[0].end]


@pytest.mark.parametrize(
    "heading_lines,expected_heading",
    [
        (["NOTE 8 — DEBT"], "NOTE 8 — DEBT"),  # HCA, with a '(continued)' page header inside
        (["14. Debt"], "14. Debt"),  # Union Pacific
        (["6.", "NOTES PAYABLE AND OTHER BORROWINGS"], "6. NOTES PAYABLE AND OTHER BORROWINGS"),  # Oracle
        (["NOTE 10", "SHORT-TERM AND LONG-TERM DEBT"], "NOTE 10 SHORT-TERM AND LONG-TERM DEBT"),  # P&G
    ],
)
def test_debt_note_heading_formats(heading_lines, expected_heading):
    number = int(expected_heading.split()[1] if expected_heading.startswith("NOTE") else expected_heading.split(".")[0])
    note_word = "NOTE " if expected_heading.startswith("NOTE") else ""
    text = "\n".join([
        "ITEM 8. FINANCIAL STATEMENTS",
        f"{note_word}{number - 1}. Leases" if not note_word else f"NOTE {number - 1} — LEASES",
        FILLER,
        *heading_lines,
        "Our notes mature between 2027 and 2055. " * 10,
        f"NOTE {number} — DEBT (continued)" if note_word else "More debt text.",
        "The revolving credit facility is undrawn. " * 10,
        f"{note_word}{number + 1}. Fair Value" if not note_word else f"NOTE {number + 1} — FAIR VALUE",
        FILLER,
    ])
    spans = detect_sections(text, "10-K")
    [debt] = spans_by_label(spans, "debt_note")
    assert debt.heading == expected_heading
    covered = text[debt.start:debt.end]
    assert "revolving credit facility is undrawn" in covered and "FAIR VALUE" not in covered.upper().split("\n")[-1]


def test_debt_note_found_when_statements_follow_item_15():
    """HCA, Oracle and others put a pointer under Item 8 and the statements after Item 15."""
    text = "\n".join([
        "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS", FILLER,
        "ITEM 8. FINANCIAL STATEMENTS", "The information required is on pages F-1 to F-40.",
        "ITEM 15. EXHIBITS AND FINANCIAL STATEMENT SCHEDULES", FILLER,
        "NOTE 7 — DEBT", "Debt text. " * 40,
        "NOTE 8 — LEASES", FILLER,
    ])
    spans = detect_sections(text, "10-K")
    assert heading_of(spans, "debt_note") == "NOTE 7 — DEBT"


def test_a_numbered_debt_line_inside_mdna_is_not_a_note():
    text = "\n".join([
        "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS",
        "1. Revenue", FILLER, "2. Debt", FILLER, "3. Outlook", FILLER,
        "ITEM 8. FINANCIAL STATEMENTS", FILLER,
    ])
    assert not spans_by_label(detect_sections(text, "10-K"), "debt_note")


@pytest.mark.parametrize("heading", [
    "Liquidity, Financial Condition and Capital Resources",  # Carnival
    "CASH FLOW, FINANCIAL CONDITION AND LIQUIDITY",  # Procter & Gamble
])
def test_liquidity_heading_variants(heading):
    text = "\n".join(["ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS", FILLER, heading, FILLER,
                      "Critical Accounting Estimates", FILLER, "ITEM 8. FINANCIAL STATEMENTS", FILLER])
    assert heading_of(detect_sections(text, "10-K"), "liquidity") == heading


def test_table_numbers_neither_start_nor_end_a_note():
    """Some filings put each table cell on its own line. Kohl's '3.40%' is not the start of note 3, and
    Community Health's '24' above 'Less: Unamortized deferred debt issuance costs' is not a note heading."""
    text = "\n".join([
        "ITEM 8. FINANCIAL STATEMENTS",
        "1. Accounting Policies", FILLER,
        "24", "Less: Unamortized deferred debt issuance costs", "25", "Other long-term liabilities",
        "2. Debt", "Senior notes outstanding:", "3.40%", "5.13%", "Notes due 2033. " * 30,
        "3. Leases", FILLER,
    ])
    spans = detect_sections(text, "10-K")
    [debt] = spans_by_label(spans, "debt_note")
    assert debt.heading == "2. Debt"
    assert text[debt.end:].startswith("3. Leases")


def test_joint_filers_items_8a_8b_and_10q_1a_1b_are_financial_statements():
    """American Airlines files with its subsidiary: Items 8A/8B (10-K) and Part I Items 1A/1B (10-Q)."""
    ten_k = "\n".join([
        "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS", FILLER,
        "ITEM 8A. CONSOLIDATED FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA OF AMERICAN AIRLINES GROUP INC.", FILLER,
        "ITEM 8B. CONSOLIDATED FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA OF AMERICAN AIRLINES, INC.", FILLER,
        "ITEM 9. CHANGES IN AND DISAGREEMENTS WITH ACCOUNTANTS", FILLER,
    ])
    assert [s.item for s in detect_sections(ten_k, "10-K") if s.label == "financial_statements"] == ["8A", "8B"]
    ten_q = "\n".join([
        "PART I", "ITEM 1A. CONDENSED CONSOLIDATED FINANCIAL STATEMENTS OF AMERICAN AIRLINES GROUP INC.", FILLER,
        "ITEM 1B. CONDENSED CONSOLIDATED FINANCIAL STATEMENTS OF AMERICAN AIRLINES, INC.", FILLER,
        "ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS", FILLER,
        "PART II", "ITEM 1A. RISK FACTORS", FILLER,
    ])
    labels = [(s.item, s.label) for s in detect_sections(ten_q, "10-Q") if s.label != "unlabelled"]
    assert labels == [("I-1A", "financial_statements"), ("I-1B", "financial_statements"), ("I-2", "mdna"),
                      ("II-1A", "risk_factors")]
