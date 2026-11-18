"""Layer (a): every figure in a claim must be traceable.

The writer may only produce figures two ways:
- a placeholder, {{m:<metric_id>:<period>}}, which code replaces with the engine's value (traced to XBRL), or
  {{p:<period>}} for a period's description;
- a figure copied word for word from a passage it cites (a "quoted figure", traced to that passage).
Any other digit fails. Figures are compared as number tokens: "$15.0 billion" in a claim needs the token
"15.0" in a cited passage.
"""

from __future__ import annotations

import re

PLACEHOLDER = re.compile(r"\{\{\s*(m|p)\s*:\s*([A-Za-z0-9_.\-]+)(?:\s*:\s*([A-Za-z0-9_.\-]+))?\s*\}\}")
NUMBER = re.compile(r"\d+(?:[.,]\d+)*")


def split_placeholders(text: str) -> list[tuple[str, str]]:
    """[("text", literal) | ("m", "<metric_id>:<period>") | ("p", "<period>"), ...] in order."""
    parts, position = [], 0
    for match in PLACEHOLDER.finditer(text):
        if match.start() > position:
            parts.append(("text", text[position:match.start()]))
        kind, first, second = match.groups()
        key = f"{first}:{second}" if kind == "m" and second else first if kind == "p" else f"{first}:"
        parts.append((kind, key))
        position = match.end()
    if position < len(text):
        parts.append(("text", text[position:]))
    return parts


def passage_numbers(text: str) -> set[str]:
    return set(NUMBER.findall(text))


def check_claim_numbers(text: str, cited_texts: dict[str, str], table: dict, periods: dict[str, str]) -> list[str]:
    """Problems with the claim's figures, in order of appearance. Empty means every figure is traceable."""
    allowed = set().union(*(passage_numbers(t) for t in cited_texts.values())) if cited_texts else set()
    problems = []
    for kind, value in split_placeholders(text):
        if kind == "m" and value not in table:
            problems.append(f"unknown metric placeholder: {value}")
        elif kind == "p" and value not in periods:
            problems.append(f"unknown period placeholder: {value}")
        elif kind == "text":
            problems += [f"number not from a placeholder or a cited passage: {n}"
                         for n in NUMBER.findall(value) if n not in allowed]
    return problems
