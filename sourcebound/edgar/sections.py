"""Find the standard sections of a 10-K or 10-Q in its plain text (one paragraph per line).

A 10-K is organised in numbered Items: Item 1 Business, Item 1A Risk Factors, Item 7 Management's Discussion
and Analysis (MD&A), Item 7A Market Risk, Item 8 Financial Statements, and others. A 10-Q has Part I (Item 1
Financial Statements, Item 2 MD&A, Item 3 Market Risk) and Part II (Item 1A updates to Risk Factors, ...).
Inside MD&A sits the liquidity discussion; among the notes to the financial statements, the debt note.

How it works:
1. Item headings are short lines starting "Item 7", "ITEM 1A." or "Items 1 and 2". The table of contents
   lists them too, and some filings repeat a heading at the top of every page. For each item:
   - a heading with a title ("Item 7. Management's ...") beats a bare one ("Item 7"), which is usually a
     contents entry;
   - among the rest, the one followed by the most text before a *different* item's heading wins.
   In a 10-Q the title says which Part an item belongs to ("Management's Discussion" is Part I, "Risk
   Factors" Part II); without a title, the last "Part I"/"Part II" heading seen is used.
2. Each item runs from its heading to the next chosen item heading.
3. Within MD&A, the liquidity discussion starts at one of a few exact headings (LIQUIDITY_HEADINGS) and
   ends at the next of a few known MD&A headings (MDNA_NEXT_HEADINGS), or at the end of MD&A.
4. The debt note is a numbered note ("Note 8 — Debt", "14. Debt", or a number line followed by a title
   line) whose title mentions debt or borrowings, outside the narrative sections. It ends where the next
   note number begins. Some filings print their statements after Item 15, so the whole document is searched.

Anything before the first item is "unlabelled"; detected items without a target label are "other_item".
If nothing is detected, the whole document is one "unlabelled" span. A label is never guessed: every label
comes from a heading found in the text, and spans record that heading.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

ITEM_HEADING = re.compile(r"^items?\s+(\d{1,2}[a-c]?)(?![0-9a-z])[\s\.\:—–-]*(.*)$", re.IGNORECASE)
PART_HEADING = re.compile(r"^part\s+(iv|i{1,3})\b", re.IGNORECASE)
NOTE_ONE_LINE = re.compile(
    r"^(?:note\s+(\d{1,2})(?:\s*[\.\:—–-])?\s+|(\d{1,2})\s*[\.\:—–-]\s*)([A-Za-z].*)$", re.IGNORECASE
)
# A bare note number on its own line must read "Note 6" or "6." (with the full stop): a lone "24" is
# usually a table cell.
NOTE_NUMBER_ONLY = re.compile(r"^(?:note\s+(\d{1,2})|(\d{1,2})\.)$", re.IGNORECASE)
MAX_HEADING_CHARS = 200
MAX_NOTE_HEADING_CHARS = 100

TEN_K_LABELS = {"1": "business", "1A": "risk_factors", "7": "mdna", "7A": "market_risk", "8": "financial_statements"}
TEN_Q_LABELS = {
    ("I", "1"): "financial_statements",
    ("I", "2"): "mdna",
    ("I", "3"): "market_risk",
    ("II", "1A"): "risk_factors",
}
TEN_Q_PART_BY_TITLE = (
    ("financial statements", "I"), ("management", "I"), ("quantitative and qualitative", "I"),
    ("controls and procedures", "I"), ("legal proceedings", "II"), ("risk factors", "II"),
    ("unregistered sales", "II"), ("defaults upon", "II"), ("mine safety", "II"), ("other information", "II"),
    ("exhibits", "II"),
)
LIQUIDITY_HEADINGS = {
    "liquidity and capital resources",
    "liquidity",
    "capital resources and liquidity",
    "financial condition and liquidity",
    "liquidity and financial condition",
    "consolidated financial condition",
    "financial condition",
    "liquidity, financial condition and capital resources",
    "financial condition, liquidity and capital resources",
    "cash flow, financial condition and liquidity",
}
MDNA_NEXT_HEADINGS = (
    "other matters", "commitments and contingen", "contractual obligations", "off-balance sheet",
    "off balance sheet", "critical accounting", "recent accounting", "new accounting", "accounting pronouncements",
    "market risk", "forward-looking", "forward looking", "cautionary statement", "results of operations",
    "segment results", "environmental matters", "legal proceedings",
)
DEBT_NOTE_WORDS = ("debt", "borrowings", "financing arrangements", "credit facilit", "notes payable")
NARRATIVE_LABELS = {"business", "risk_factors", "mdna", "liquidity", "market_risk"}


@dataclass(frozen=True)
class Span:
    label: str  # business, risk_factors, mdna, liquidity, market_risk, financial_statements, debt_note,
    #             other_item or unlabelled
    item: str  # e.g. "7", "1A" (10-K) or "II-1A" (10-Q); "" when unlabelled
    heading: str  # the heading line the label comes from; "" when unlabelled
    start: int  # character offsets into the document text
    end: int


@dataclass(frozen=True)
class _Head:
    offset: int
    key: object  # item code (10-K) or (part, code) (10-Q)
    item: str
    label: str
    line: str
    titled: bool


def _normalise(line: str) -> str:
    line = line.replace("’", "'").lower().strip().rstrip(".:").strip()
    return re.sub(r"\s+", " ", line)


def _line_offsets(text: str) -> list[tuple[int, str]]:
    offsets, position = [], 0
    for line in text.split("\n"):
        offsets.append((position, line))
        position += len(line) + 1
    return offsets


# ----- items ------------------------------------------------------------------------------------------


def _statements_by_title(title: str, could_be_statements: bool) -> str:
    """Joint filers (e.g. American Airlines) split their statements into Items 8A/8B or 10-Q Items 1A/1B;
    such an item is labelled from its own title."""
    return "financial_statements" if could_be_statements and "financial statements" in title.lower() else "other_item"


def _find_heads(lines: list[tuple[int, str]], form: str) -> list[_Head]:
    quarterly = form.startswith("10-Q")
    heads, part = [], None
    for offset, line in lines:
        if len(line) > MAX_HEADING_CHARS:
            continue
        part_match = PART_HEADING.match(line)
        if part_match:
            part = part_match.group(1).upper()
            continue
        item_match = ITEM_HEADING.match(line)
        if not item_match:
            continue
        code, title = item_match.group(1).upper(), item_match.group(2).strip()
        if quarterly:
            title_part = next((p for words, p in TEN_Q_PART_BY_TITLE if words in title.lower()), None)
            item_part = title_part or part
            key, item = (item_part, code), f"{item_part}-{code}" if item_part else code
            label = TEN_Q_LABELS.get(key) or _statements_by_title(title, item_part == "I")
        else:
            key, item = code, code
            label = TEN_K_LABELS.get(code) or _statements_by_title(title, code.startswith("8"))
        heads.append(_Head(offset, key, item, label, line, titled=bool(title)))
    return heads


def _choose_heads(heads: list[_Head], text_length: int) -> list[_Head]:
    """One heading per item: titled beats untitled; then the most text before a different item's heading."""
    def run_length(n: int) -> int:
        following = next((h.offset for h in heads[n + 1:] if h.key != heads[n].key), text_length)
        return following - heads[n].offset

    best: dict = {}
    for n, head in enumerate(heads):
        rank = (head.titled, run_length(n))
        if head.key not in best or rank > best[head.key][0]:
            best[head.key] = (rank, head)
    return sorted((head for _, head in best.values()), key=lambda h: h.offset)


def _item_spans(text: str, lines: list[tuple[int, str]], form: str) -> list[Span]:
    chosen = _choose_heads(_find_heads(lines, form), len(text))
    spans = []
    for n, head in enumerate(chosen):
        end = chosen[n + 1].offset if n + 1 < len(chosen) else len(text)
        spans.append(Span(head.label, head.item, head.line, head.offset, end))
    return spans


# ----- subsections ------------------------------------------------------------------------------------


def _liquidity(lines: list[tuple[int, str]], mdna: Span) -> Span | None:
    inside = [(offset, line) for offset, line in lines if mdna.start <= offset < mdna.end]
    best = None
    for n, (offset, line) in enumerate(inside):
        if _normalise(line) not in LIQUIDITY_HEADINGS:
            continue
        end = next(
            (o for o, l in inside[n + 1:] if len(l) <= 100 and _normalise(l).startswith(MDNA_NEXT_HEADINGS)),
            mdna.end,
        )
        if best is None or end - offset > best.end - best.start:
            best = Span("liquidity", mdna.item, line, offset, end)
    return best


def _is_debt_title(title: str) -> bool:
    lowered = title.lower()
    return (
        any(word in lowered for word in DEBT_NOTE_WORDS)
        and not lowered.rstrip().endswith("(continued)")
        and "$" not in title
        and len(title) <= MAX_NOTE_HEADING_CHARS
    )


def _note_starts(line: str, next_line: str, number: int) -> bool:
    """Does this line start note `number`? Either "Note 9 — Leases" / "9. Leases" (a word right after the
    number, so "9.40%" does not count), or a bare "Note 9" / "9." followed by a title line."""
    if len(line) > MAX_NOTE_HEADING_CHARS:
        return False
    one_line = rf"^(?:note\s+{number}(?:\s*[\.\:—–-])?\s+|{number}\s*[\.\:—–-]\s*)[A-Za-z]"
    if re.match(one_line, line, re.IGNORECASE):
        return True
    bare = NOTE_NUMBER_ONLY.match(line)
    return bool(bare) and int(bare.group(1) or bare.group(2)) == number and re.match(r"^[A-Za-z]", next_line) is not None


def _debt_note(lines: list[tuple[int, str]], spans: list[Span], text_length: int) -> Span | None:
    """The longest numbered note about debt, outside the narrative sections, ending at the next note."""
    def label_at(offset: int) -> str:
        return next(s.label for s in spans if s.start <= offset < s.end)

    best = None
    for n, (offset, line) in enumerate(lines):
        if len(line) > MAX_NOTE_HEADING_CHARS:
            continue
        number, heading = None, None
        one_line = NOTE_ONE_LINE.match(line)
        if one_line and _is_debt_title(one_line.group(3)):
            number, heading = int(one_line.group(1) or one_line.group(2)), line
        else:
            bare = NOTE_NUMBER_ONLY.match(line)
            if bare and n + 1 < len(lines) and re.match(r"^[A-Za-z]", lines[n + 1][1]) \
                    and _is_debt_title(lines[n + 1][1]):
                number, heading = int(bare.group(1) or bare.group(2)), f"{line} {lines[n + 1][1]}"
        if number is None or label_at(offset) in NARRATIVE_LABELS:
            continue
        following = lines[n + 1:]
        end = next(
            (o for k, (o, l) in enumerate(following)
             if _note_starts(l, following[k + 1][1] if k + 1 < len(following) else "", number + 1)),
            None,
        )
        if end is None:
            continue  # no next note found: the extent is unknown, so no label
        if best is None or end - offset > best.end - best.start:
            best = Span("debt_note", "", heading, offset, end)
    return best


def _carve(spans: list[Span], inner: Span | None) -> list[Span]:
    """Replace the part of the span containing inner.start with inner (clipped to that span)."""
    if inner is None:
        return spans
    result = []
    for span in spans:
        if not (span.start <= inner.start < span.end):
            result.append(span)
            continue
        piece = Span(inner.label, inner.item or span.item, inner.heading, inner.start, min(inner.end, span.end))
        parts = [
            Span(span.label, span.item, span.heading, span.start, piece.start),
            piece,
            Span(span.label, span.item, span.heading, piece.end, span.end),
        ]
        result += [p for p in parts if p.end > p.start]
    return result


def detect_sections(text: str, form: str) -> list[Span]:
    """Ordered, contiguous spans covering the whole text, each with a label from a heading found in it."""
    lines = _line_offsets(text)
    items = _item_spans(text, lines, form)
    if not items:
        spans = [Span("unlabelled", "", "", 0, len(text))]
    else:
        spans = [Span("unlabelled", "", "", 0, items[0].start)] if items[0].start > 0 else []
        spans += items
    for mdna in [s for s in spans if s.label == "mdna"]:
        spans = _carve(spans, _liquidity(lines, mdna))
    return _carve(spans, _debt_note(lines, spans, len(text)))
