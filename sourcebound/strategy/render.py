"""Render the strategy artifacts from templates, so every figure in them comes from a results file.

Templates live in docs/strategy/templates/. As in the memos, no figure is typed. Two kinds of placeholder:
- {{r:writers>GLM-5.3>cost_total_per_memo|usd3}}: a value from evals/results/results.json (path parts
  separated by ">", because model names contain dots and slashes), in a named format. Rates always show their
  sample size, and an unmeasured rate reads "not measured (n = 0)".
- {{table:writers}}: a table built by code from results.json or the timing log (evals/timings.csv).
Then stray_numbers() lists any digit in the rendered text that did not come from a placeholder and is not an
identifier (a regulation number, a form type, a date, a decision number, list numbering, a name in a code
span); a test requires none.
The decision log (06) is written by hand and records settings and dated observations, so it is not a template.
"""

from __future__ import annotations

import re
from collections.abc import Callable

from sourcebound.paths import PROJECT_ROOT
from sourcebound.strategy.timings import Timing, summarise

STRATEGY_DIR = PROJECT_ROOT / "docs" / "strategy"
TEMPLATE_DIR = STRATEGY_DIR / "templates"
RESULTS_FILE = PROJECT_ROOT / "evals" / "results" / "results.json"
TIMINGS_FILE = PROJECT_ROOT / "evals" / "timings.csv"
HEADER = ("<!-- Generated from docs/strategy/templates/{name} by "
          "`uv run python -m sourcebound.pipeline.build_strategy`. Edit the template, not this file. -->\n\n")
PLACEHOLDER = re.compile(r"\{\{(r|table):([^}|]+)(?:\|([a-z0-9]+))?\}\}")

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
IDENTIFIERS = [
    r"\bSR \d{2}-\d{1,2}\b", r"\bOCC Bulletin \d{4}-\d{1,3}\b", r"\bFIL-\d{1,3}-\d{4}\b",
    r"\b10-[KQ]\b", r"\b8-K\b", r"\bD\d{1,3}\b", r"\bSB-[1-6]\b", r"\bgrid-v\d+\b", r"\bItem \d+[AB]?\b",
    rf"\b\d{{1,2}} (?:{MONTHS}) \d{{4}}\b", rf"\b(?:{MONTHS}) \d{{4}}\b", r"\b\d{4}-\d{2}-\d{2}\b",
    r"\b(?:19|20)\d{2}\b", r"\bphases? \d+(?:(?: to | and )\d+)?\b", r"\bfootnote \d+\b",
    r"\bPLAN\.md \d+\.\d+\b", r"\b0\d-[a-z-]+\.md\b",
    r"\b(?:zai-org/)?GLM-\d+(?:\.\d+)*\b", r"\b(?:deepseek-ai/)?DeepSeek-V\d+(?:\.\d+)?(?:-[A-Za-z]+)?-\d{4}\b",
    r"\bBM25\b", r"(?m)^\s*\d+\. ",  # numbered-list markers
    r"`[^`\n]+`",  # code spans: test, file and command names
]
# Facts quoted from external documents, each with its source (they are not measurements of this project).
EXTERNAL_FACTS = [
    "$30 billion",  # SR 26-2 / OCC Bulletin 2026-13: guidance expected to be most relevant above this asset size
]
NUMBER = re.compile(r"\d+(?:[.,]\d+)*")


def _pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def _rate(rate: dict) -> str:
    return f"not measured (n = {rate['n']})" if rate["value"] is None else f"{_pct(rate['value'])} (n = {rate['n']})"


def _spread(s: dict) -> str:
    return f"{_pct(s['mean'])} ({_pct(s['min'])} to {_pct(s['max'])}, {s['n']} runs)"


def _int(value) -> str:
    if value != int(value):
        raise ValueError(f"{value} is not a whole number")
    return str(int(value))


FORMATS: dict[str, Callable] = {
    "rate": _rate, "pct1": _pct, "usd3": lambda v: f"${v:.3f}", "usd4": lambda v: f"${v:.4f}",
    "num1": lambda v: f"{v:.1f}", "int": _int, "sec0": lambda v: f"{v:.0f} s", "spread": _spread, "text": str,
}


def lookup(results: dict, path: str):
    value = results
    for part in path.split(">"):
        value = value[part]  # KeyError on a wrong path: never a silent blank
    return value


def _md_table(header: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    return "\n".join(lines + ["| " + " | ".join(row) + " |" for row in rows])


def writers_table(results: dict) -> str:
    writers = results["writers"]
    accuracy, labels = results.get("memo_numeric_accuracy", {}), results.get("labels", {}).get("per_writer", {})
    names = list(writers)
    rows = [
        ("Model ID", lambda n: writers[n]["model"]),
        ("Memos drafted (first run)", lambda n: _int(writers[n]["memos_run1"])),
        ("Claims per memo", lambda n: f"{writers[n]['claims_per_memo']:.1f}"),
        ("Judge: supported", lambda n: _rate(writers[n]["judge_supported"])),
        ("Judge: partly supported", lambda n: _rate(writers[n]["judge_partially"])),
        ("Judge: unsupported", lambda n: _rate(writers[n]["judge_unsupported"])),
        ("Quoted figures found in the cited passage", lambda n: _rate(accuracy[n]["quoted_figures_in_cited_passage"])),
        ("Engine figures matching hand-checked values", lambda n: _rate(accuracy[n]["engine_figures"])),
        ("Unsupported-claim rate (human labels)", lambda n: _rate(labels[n]["unsupported_rate"])),
        ("Citation precision (human labels)", lambda n: _rate(labels[n]["citation_precision"])),
        ("Raw numbers rejected per memo", lambda n: f"{writers[n]['raw_numbers_rejected_per_memo']:.1f}"),
        ("Repairs per memo", lambda n: f"{writers[n]['repairs_per_memo']:.1f}"),
        ("Cost per memo (USD, list price)", lambda n: f"${writers[n]['cost_total_per_memo']:.3f}"),
        ("Model time per memo", lambda n: f"{writers[n]['model_seconds_per_memo']:.0f} s"),
        ("Run-to-run: judge supported", lambda n: _spread(writers[n]["run_to_run_judge_supported"])),
    ]
    return _md_table(["Measure"] + names, [[label] + [cell(n) for n in names] for label, cell in rows])


def judges_table(results: dict) -> str:
    rows = [[name, _int(j["rows_judged"]), _rate(j["agreement"]), _rate(j["false_pass_rate"]), f"${j['cost_usd']:.4f}"]
            for name, j in results["judge_calibration"].items()]
    return _md_table(["Judge", "Claims judged", "Agreement with human labels", "False-pass rate", "Cost (USD)"], rows)


def seeded_table(results: dict) -> str:
    rows = []
    for judge, kinds in results["seeded_errors"].items():
        for kind, k in kinds.items():
            rows.append([judge, kind.replace("_", " "), _int(k["n"]), f"{k['code']} of {k['n']}",
                         f"{k['judge_unsupported']} of {k['n']}", f"{k['judge_partial']} of {k['n']}",
                         f"{k['missed']} of {k['n']}"])
    return _md_table(["Judge", "Error planted", "n", "Caught by code", "Judge: unsupported", "Judge: partly",
                      "Missed"], rows)


def timings_table(timings: list[Timing]) -> str:
    summary = summarise(timings)
    if not summary:
        return "No timings were recorded, so the effort comparison is not measured (n = 0)."
    return _md_table(["Task", "Condition", "Tasks timed", "Median minutes", "Errors found later"],
                     [[s.task, s.condition, str(s.n), f"{s.median_minutes:.0f}", str(s.errors_found_later)]
                      for s in summary])


TABLES: dict[str, Callable] = {"writers": writers_table, "judges": judges_table, "seeded": seeded_table}


def render(template: str, results: dict, timings: list[Timing]) -> tuple[str, list[tuple[int, int]]]:
    """(rendered text, the character spans that placeholders produced)."""
    out, spans, position = [], [], 0
    length = 0
    for match in PLACEHOLDER.finditer(template):
        literal = template[position:match.start()]
        out.append(literal)
        length += len(literal)
        kind, name, fmt = match.groups()
        if kind == "table":
            value = timings_table(timings) if name == "timings" else TABLES[name](results)
        else:
            if fmt not in FORMATS:
                raise ValueError(f"unknown format {fmt!r} in {match.group()}")
            value = FORMATS[fmt](lookup(results, name))
        out.append(value)
        spans.append((length, length + len(value)))
        length += len(value)
        position = match.end()
    out.append(template[position:])
    return "".join(out), spans


def stray_numbers(text: str, spans: list[tuple[int, int]]) -> list[str]:
    """Digits not produced by a placeholder and not part of an identifier or a quoted external fact."""
    chars = list(text)
    for start, end in spans:
        chars[start:end] = " " * (end - start)
    rest = "".join(chars)
    for fact in EXTERNAL_FACTS:
        rest = rest.replace(fact, " ")
    for pattern in IDENTIFIERS:
        rest = re.sub(pattern, " ", rest)
    return NUMBER.findall(rest)
