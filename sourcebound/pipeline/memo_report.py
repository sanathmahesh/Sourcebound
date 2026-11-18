"""A readable Markdown copy of a memo (reports/memos/<TICKER>.md), for checking by hand.

Every engine figure is bold with a reference [F1], [F2] ... to a table listing its formula and the XBRL
facts behind it; every quoted figure and citation points to its passage, listed in full at the end.
"""

from __future__ import annotations

from sourcebound.contracts import Memo, VerificationReport
from sourcebound.memo.render import format_metric

VERDICT_MARK = {"supported": "✅ supported", "partially_supported": "◐ partially supported", "unsupported": "❌ unsupported"}


def render_memo_markdown(memo: Memo, report: VerificationReport) -> str:
    refs: dict[str, str] = {}
    lines = [
        f"# Credit memo: {memo.name} ({memo.ticker})",
        "",
        f"**{memo.disclaimer}**",
        "",
        f"Drafted {memo.memo_date} by `{memo.model}`, each claim checked by `{memo.judge_model}` and by code. "
        f"SB grade: **{memo.grade or 'not available'}**{' (provisional)' if memo.grade_provisional else ''}.",
        "Sources: " + "; ".join(f"[{s.form} for {s.period_end}]({s.url})" for s in memo.sources),
        "",
        f"Claims: {report.summary.claims} — {report.summary.supported} supported, "
        f"{report.summary.partially_supported} partially supported, {report.summary.unsupported} unsupported. "
        f"Raw numbers rejected in first drafts: {report.summary.raw_numbers_rejected}; repairs: {report.summary.repairs}.",
        "",
    ]
    for section in memo.sections:
        lines += [f"## {section.title}", ""]
        if not section.claims:
            lines += ["_No claims._", ""]
        for n, claim in enumerate(section.claims, start=1):
            parts = []
            for seg in claim.segments:
                if seg.t == "metric":
                    ref = refs.setdefault(seg.metric_id, f"F{len(refs) + 1}")
                    parts.append(f"**{seg.v}** [{ref}]")
                elif seg.t == "quoted":
                    parts.append(f"**{seg.v}** [quoted: {seg.chunk_id}]")
                else:
                    parts.append(seg.v)
            lines.append(f"{n}. {''.join(parts)}  ")
            lines.append(f"   {VERDICT_MARK[claim.verdict]} ({claim.checked_by}): {claim.judge_reason}")
            for cit in claim.citations:
                mark = "✓" if cit.check == "ok" else f"✗ {cit.check.replace('_', ' ')}"
                lines.append(f"   - cites `{cit.chunk_id}` {mark}: “{cit.quote}”")
            for flag in claim.flags:
                lines.append(f"   - flag: {flag}")
        for note in section.notes:
            lines.append(f"\n_Note: {note}_")
        lines.append("")
    lines += ["## Reviewer checklist", ""]
    lines += [f"- [ ] **{i.category.replace('_', ' ')}** ({i.severity}): {i.message}" for i in memo.checklist] or ["None."]
    lines += ["", "## Figures and their sources", "", "| Ref | Figure | Value | Formula | XBRL facts |", "|---|---|---|---|---|"]
    for key, ref in refs.items():
        metric = memo.metrics.get(key)
        if metric is None:
            continue
        facts = "<br>".join(f"{i.tag} {i.value:,.0f} ({i.period}, {i.role}) [{i.form} {i.accession}]({i.url})"
                            for i in metric.inputs[:8])
        lines.append(f"| {ref} | {metric.label} ({key}) | {format_metric(metric)} | {metric.formula} | {facts or '—'} |")
    lines += ["", "## Passages cited", ""]
    for cid, passage in memo.passages.items():
        lines += [f"### {cid}", "",
                  f"{passage.section}, [{passage.form} for {passage.period_end}]({passage.url}), characters "
                  f"{passage.start}–{passage.end}", "", "> " + passage.text.replace("\n", "\n> "), ""]
    d, v = memo.run.drafting, memo.run.verification
    lines += ["## Run", "",
              f"Run `{memo.run.run_id}`; service tier {memo.run.service_tier}; reasoning effort {memo.run.reasoning_effort}.",
              f"Drafting: {d.calls} calls, {d.input_tokens:,} input ({d.cached_input_tokens:,} cached) and {d.output_tokens:,} "
              f"output tokens, ${d.cost_usd:.4f}, {d.seconds:.0f}s. Verification: {v.calls} calls, {v.input_tokens:,} input "
              f"({v.cached_input_tokens:,} cached) and {v.output_tokens:,} output tokens, ${v.cost_usd:.4f}, {v.seconds:.0f}s. "
              f"Prices read {memo.run.prices_read_on}. Raw requests and responses: data/runs/{memo.run.raw_outputs}."]
    return "\n".join(lines) + "\n"
