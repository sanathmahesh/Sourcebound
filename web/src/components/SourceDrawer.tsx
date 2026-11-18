// The source drawer, a dialog on the right. For a number: its formula and every XBRL input, with fallback
// ranks. For a claim: its verdict and the judge's reason, then every passage it cites with the quote marked
// and whether the quote check found it. Focus moves into the drawer, stays there, and Escape closes it.
import { type ReactNode, useEffect, useRef } from "react";
import type { MemoCitation, Metric } from "../contracts/types";
import { formatDate, formatRaw, formatValue, VERDICT } from "../format";
import type { DrawerSource } from "../sources";
import { claimPlainText } from "./ClaimText";

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** The passage with the quote marked; whitespace and case differences are tolerated, as in the quote check. */
export function highlight(text: string, quote?: string): ReactNode {
  if (!quote?.trim()) return text;
  const pattern = new RegExp(quote.trim().split(/\s+/).map(escapeRegExp).join("\\s+"), "i");
  const match = pattern.exec(text);
  if (!match) return text;
  return <>{text.slice(0, match.index)}<mark>{match[0]}</mark>{text.slice(match.index + match[0].length)}</>;
}

const FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';

export function SourceDrawer({ source, onClose }: { source: DrawerSource | null; onClose: () => void }) {
  const panel = useRef<HTMLElement>(null);
  const closeButton = useRef<HTMLButtonElement>(null);
  const close = useRef(onClose);
  close.current = onClose;
  const open = source !== null;

  useEffect(() => {
    if (!open) return;
    const opener = document.activeElement as HTMLElement | null;
    closeButton.current?.focus();
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") { close.current(); return; }
      if (event.key !== "Tab" || !panel.current) return;
      const items = [...panel.current.querySelectorAll<HTMLElement>(FOCUSABLE)];
      const first = items[0], last = items[items.length - 1];
      const inside = panel.current.contains(document.activeElement);
      if (event.shiftKey && (document.activeElement === first || !inside)) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && (document.activeElement === last || !inside)) { event.preventDefault(); first.focus(); }
    };
    document.addEventListener("keydown", onKey);
    return () => { document.removeEventListener("keydown", onKey); opener?.focus?.(); };
  }, [open]);

  if (!source) return null;
  const kind = source.kind === "metric"
    ? `Number · computed from XBRL · ${source.metric.period}`
    : `Claim ${source.claim.id} · ${source.claim.citations.length ? "citation" : "verdict"}`;
  return (
    <>
      <div className="backdrop" onClick={onClose} />
      <aside className="drawer" role="dialog" aria-modal="true" aria-label="Source" ref={panel}>
        <div className="drawer-head">
          <span className="eyebrow">{kind}</span>
          <button type="button" className="drawer-close" ref={closeButton} onClick={onClose}>Close ✕</button>
        </div>
        {source.kind === "metric" ? <MetricSource metric={source.metric} /> : <ClaimSource source={source} />}
      </aside>
    </>
  );
}

const STATUS_NOTE: Partial<Record<Metric["status"], string>> = {
  not_available: "Not available.",
  not_meaningful: "Not meaningful.",
};

function MetricSource({ metric: m }: { metric: Metric }) {
  const fallback = m.inputs.some((i) => i.fallback_rank > 1);
  const noteTitle = STATUS_NOTE[m.status] ?? (fallback ? "Fallback tag used." : m.notes.length ? "Note." : null);
  const noteText = [fallback && !STATUS_NOTE[m.status] ? "At least one input uses a lower-ranked XBRL tag; its rank is shown beside it." : "",
    ...m.notes].filter(Boolean).join(" ");
  return (
    <>
      <h2 className="drawer-title">{m.label}</h2>
      <div className={`drawer-value${m.status === "ok" ? "" : " muted"}`}>{formatValue(m.value, m.unit, m.status)}</div>
      <h3 className="eyebrow drawer-sub">Formula</h3>
      <div className="formula">{m.formula}</div>
      {noteTitle && <div className="note-box"><strong>! {noteTitle}</strong> {noteText}</div>}
      <h3 className="eyebrow drawer-sub ruled">Inputs ({m.inputs.length})</h3>
      {m.inputs.length === 0 && (
        <p className="muted small">{m.status === "not_available" ? "No inputs were retrieved for this figure."
          : "No XBRL inputs: this figure is computed from other figures in this memo."}</p>
      )}
      {m.inputs.map((i, n) => (
        <div key={n} className="input-row">
          <div className="input-top"><span className="strong">{i.label}</span><span className="mono">{formatRaw(i.value, i.unit)}</span></div>
          <div className="mono tag-line">{i.tag}
            {i.fallback_rank > 1 && <> <span className="badge-warn">fallback, rank {i.fallback_rank}</span></>}</div>
          <div className="input-meta">
            <span>Period: {i.period}{i.role ? ` · ${i.role}` : ""}{i.sign < 0 ? " · subtracted" : ""}</span>
            <span>{i.form}, filed {formatDate(i.filed)}</span>
            <span className="mono small">{i.accession}</span>
            <a href={i.url} target="_blank" rel="noreferrer">EDGAR ↗</a>
          </div>
        </div>
      ))}
    </>
  );
}

const CHECK_WORDS: Record<MemoCitation["check"], string> = {
  ok: "yes",
  chunk_not_found: "no (passage not found)",
  quote_too_short: "no (quote too short to check)",
  quote_not_found: "no (quote not found)",
};

function ClaimSource({ source }: { source: Extract<DrawerSource, { kind: "claim" }> }) {
  const { claim, passages, judgeModel, focus } = source;
  const verdict = VERDICT[claim.verdict];
  const cited = [...claim.citations].sort((a, b) => Number(b.chunk_id === focus) - Number(a.chunk_id === focus));
  const extra = focus && !cited.some((c) => c.chunk_id === focus) ? [focus] : [];
  return (
    <>
      <p className="drawer-claim">{claimPlainText(claim)}</p>
      <div className={`verdict-box verdict-${claim.verdict}`}>
        <div className="strong verdict-colour">{verdict.glyph} {verdict.words[0].toUpperCase() + verdict.words.slice(1)}</div>
        <div className="small-14"><span className="muted">Judge:</span> {claim.judge_reason}</div>
        <div className="muted small">{claim.checked_by === "judge"
          ? `Checked by ${judgeModel}, independent of the drafting model.`
          : "Checked by code (the number or quote check); no model was asked."}</div>
      </div>
      {claim.flags.length > 0 && <div className="note-box"><strong>! Note.</strong> {claim.flags.join("; ")}</div>}
      {cited.length === 0 && extra.length === 0 && (
        <p className="muted small">This claim cites no passage. Its figures are computed from XBRL: close this panel and
          select a figure to see its inputs.</p>
      )}
      {cited.map((c, n) => (
        <PassageBlock key={`${c.chunk_id}-${n}`} chunkId={c.chunk_id} quote={c.quote} check={c.check}
          title={cited.length > 1 ? `Passage ${n + 1} of ${cited.length}` : "Passage"} passages={passages} />
      ))}
      {extra.map((chunkId) => <PassageBlock key={chunkId} chunkId={chunkId} title="Passage quoted" passages={passages} />)}
    </>
  );
}

function PassageBlock({ chunkId, quote, check, title, passages }: {
  chunkId: string; quote?: string; check?: MemoCitation["check"]; title: string;
  passages: Extract<DrawerSource, { kind: "claim" }>["passages"];
}) {
  const p = passages[chunkId];
  return (
    <section>
      <h3 className="eyebrow drawer-sub">{title}</h3>
      {p ? <blockquote className="passage">{highlight(p.text, quote)}</blockquote>
        : <p className="muted small">Passage {chunkId} is not in this file.</p>}
      {check && <div className="small">Quote found in passage: {CHECK_WORDS[check]}</div>}
      {p && (
        <div className="input-meta">
          <span>{p.form} for the period to {formatDate(p.period_end)}, filed {formatDate(p.filed)}</span>
          <span>{p.section}</span>
          <span className="mono small">{chunkId}</span>
          <a href={p.url} target="_blank" rel="noreferrer">EDGAR ↗</a>
        </div>
      )}
    </section>
  );
}
