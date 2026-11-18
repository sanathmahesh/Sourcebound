"""Turn a writer's claim (with placeholders) into segments the reader sees, and format engine values.

{{m:net_leverage:LTM}} becomes the engine's value ("0.96x") as a metric segment linked to its lineage;
{{p:LTM}} becomes a period description; a figure quoted from a cited passage becomes a quoted segment
linked to that passage. The model never produces a displayed engine number.
"""

from __future__ import annotations

from dataclasses import dataclass

from sourcebound.contracts import Metric, PeriodInfo, Segment
from sourcebound.verify.numbers import NUMBER, check_claim_numbers, passage_numbers, split_placeholders


@dataclass(frozen=True)
class TableEntry:
    key: str  # "<metric_id>:<period>"
    label: str
    display: str  # the formatted value the reader sees


@dataclass
class Rendered:
    text: str
    segments: list[Segment]
    problems: list[str]
    metric_keys: list[str]


def format_metric(metric: Metric) -> str:
    """How an engine value reads in prose: $51.5 billion, 0.96x, 23.6%, or a status in words."""
    if metric.status == "not_available":
        return "not available"
    if metric.status == "not_meaningful":
        return "not meaningful"
    if metric.value is None:
        return "net cash" if metric.status == "net_cash" else "not available"
    v = metric.value
    if metric.unit == "USD":
        sign = "-" if v < 0 else ""
        amount = abs(v)
        if amount >= 1e9:
            text = f"{sign}${amount / 1e9:,.1f} billion"
        elif amount >= 1e6:
            text = f"{sign}${amount / 1e6:,.0f} million"
        else:
            text = f"{sign}${amount:,.0f}"
    elif metric.unit == "x":
        text = f"{v:.2f}x"
    elif metric.unit == "%":
        text = f"{v:.1f}%"
    else:
        text = f"{v:g}"
    return f"{text} (net cash)" if metric.status == "net_cash" else text


def period_phrases(periods: list[PeriodInfo]) -> dict[str, str]:
    """{{p:FY0}} -> "the fiscal year ended 31 January 2026"; {{p:LTM}} -> "the twelve months to ..."."""
    phrases = {}
    for p in periods:
        when = f"{p.balance_sheet_date.day} {p.balance_sheet_date:%B %Y}"
        phrases[p.label] = f"the twelve months to {when}" if p.label == "LTM" else f"the fiscal year ended {when}"
    return phrases


def render_claim(text: str, cited_texts: dict[str, str], table: dict[str, TableEntry],
                 periods: dict[str, str]) -> Rendered:
    problems = check_claim_numbers(text, cited_texts, table, periods)
    segments: list[Segment] = []
    keys: list[str] = []

    def add_text(value: str) -> None:
        if value:
            if segments and segments[-1].t == "text":
                segments[-1] = Segment(t="text", v=segments[-1].v + value)
            else:
                segments.append(Segment(t="text", v=value))

    for kind, value in split_placeholders(text):
        if kind == "m":
            entry = table.get(value)
            if entry is None:
                add_text(f"[unknown figure {value}]")
            else:
                segments.append(Segment(t="metric", v=entry.display, metric_id=value))
                keys.append(value)
        elif kind == "p":
            add_text(periods.get(value, f"[unknown period {value}]"))
        else:
            position = 0
            for match in NUMBER.finditer(value):
                source = next((cid for cid, t in cited_texts.items() if match.group() in passage_numbers(t)), None)
                if source is None:
                    continue  # stays in the text; check_claim_numbers has reported it
                add_text(value[position:match.start()])
                segments.append(Segment(t="quoted", v=match.group(), chunk_id=source))
                position = match.end()
            add_text(value[position:])
    return Rendered("".join(s.v for s in segments), segments, problems, keys)
