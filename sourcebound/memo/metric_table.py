"""The placeholders a writer may use for one company: every published metric, plus scorecard figures.

Keys are "<metric_id>:<period>", the same as in metrics.json, so {{m:net_leverage:LTM}} renders the value
in metrics["net_leverage:LTM"]. The scorecard adds band_<factor>:latest, weight_<factor>:latest,
sb_score:latest and sb_grade:latest, so the rating rationale never needs to type a digit either.
"""

from __future__ import annotations

from sourcebound.contracts import CompanyMetrics, Metric
from sourcebound.memo.render import TableEntry, format_metric


def scorecard_metrics(cm: CompanyMetrics) -> dict[str, Metric]:
    card = cm.scorecard
    extras: dict[str, Metric] = {}
    for f in card.factors:
        extras[f"band_{f.id}:latest"] = Metric(
            metric_id=f"band_{f.id}", period="latest", label=f"{f.label}: scorecard band (1 strongest, 6 weakest)",
            value=f.band, unit="band", status="ok" if f.band is not None else "not_available",
            formula=f"band of {f.id}:{f.period} on config/grid.yaml ({card.grid_version})", notes=[f.note] if f.note else [],
            inputs=[])
        extras[f"weight_{f.id}:latest"] = Metric(
            metric_id=f"weight_{f.id}", period="latest", label=f"{f.label}: scorecard weight", value=f.weight * 100,
            unit="%", status="ok", formula=f"config/grid.yaml ({card.grid_version})", notes=[], inputs=[])
    available = card.weighted_score is not None
    extras["sb_score:latest"] = Metric(
        metric_id="sb_score", period="latest", label="SB weighted score (1 strongest, 6 weakest)",
        value=card.weighted_score, unit="score", status="ok" if available else "not_available",
        formula="sum of weight x band over the factors scored, divided by their weights",
        notes=["provisional: weights renormalised"] if card.provisional else [], inputs=[])
    extras["sb_grade:latest"] = Metric(
        metric_id="sb_grade", period="latest", label="SB grade (a stylized scorecard grade, not a credit rating)",
        value=card.weighted_score, unit="grade", status="ok" if available else "not_available",
        formula="weighted score mapped to SB-1 ... SB-6 (config/grid.yaml)",
        notes=[card.grade or "not available"] + (["provisional"] if card.provisional else []), inputs=[])
    return extras


def _display(metric: Metric) -> str:
    if metric.unit == "band" and metric.value is not None:
        return f"{metric.value:g}"
    if metric.unit == "score" and metric.value is not None:
        return f"{metric.value:.2f}"
    if metric.unit == "grade":
        return metric.notes[0] if metric.status == "ok" else "not available"
    return format_metric(metric)


def build_table(cm: CompanyMetrics) -> tuple[dict[str, TableEntry], dict[str, Metric]]:
    """All placeholders (key -> what it renders to) and the metrics behind them."""
    metrics = dict(cm.metrics) | scorecard_metrics(cm)
    table = {}
    for key, metric in metrics.items():
        notes = [n for n in metric.notes if "assumed zero" in n or "not available" in n or "net cash" in n]
        label = f"{metric.label}, {metric.period}" + (f" [{'; '.join(notes)[:120]}]" if notes else "")
        table[key] = TableEntry(key, label, _display(metric))
    return table, metrics


def rationale_keys(cm: CompanyMetrics) -> list[str]:
    keys = []
    for f in cm.scorecard.factors:
        keys += [f"{f.id}:{f.period}", f"band_{f.id}:latest", f"weight_{f.id}:latest"]
    return keys + ["sb_score:latest", "sb_grade:latest"]
