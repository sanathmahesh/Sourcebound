// The source drawer: for a number, its formula and XBRL inputs; for a citation, the passage with the quote
// highlighted, the filing it is from and the judge's verdict.
import type { ReactNode } from "react";
import { formatRaw, formatValue, VERDICT_LABEL } from "../format";
import type { DrawerSource } from "../sources";

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** The passage with the quote marked; whitespace and case differences are tolerated, as in the quote check. */
export function highlight(text: string, quote?: string): ReactNode {
  if (!quote) return text;
  const pattern = new RegExp(quote.trim().split(/\s+/).map(escapeRegExp).join("\\s+"), "i");
  const match = pattern.exec(text);
  if (!match) return text;
  return <>{text.slice(0, match.index)}<mark>{match[0]}</mark>{text.slice(match.index + match[0].length)}</>;
}

export function SourceDrawer({ source, onClose }: { source: DrawerSource | null; onClose: () => void }) {
  if (!source) return null;
  return (
    <aside className="drawer" aria-label="Source">
      <button type="button" className="drawer-close" onClick={onClose}>Close</button>
      {source.kind === "metric" ? <MetricSource source={source} /> : <PassageSource source={source} />}
    </aside>
  );
}

function MetricSource({ source }: { source: Extract<DrawerSource, { kind: "metric" }> }) {
  const m = source.metric;
  const fallback = m.inputs.some((i) => i.fallback_rank > 1);
  return (
    <div>
      <h3>{m.label}, {m.period}: {formatValue(m.value, m.unit, m.status)}</h3>
      <p><strong>Computed from XBRL.</strong> Formula: {m.formula}</p>
      {fallback && <p className="note">A fallback tag was used for at least one input (rank above 1).</p>}
      {m.notes.map((note) => <p key={note} className="note">{note}</p>)}
      {m.inputs.length === 0 ? <p>No XBRL inputs: this figure is derived from other metrics or the scorecard.</p> : (
        <div className="table-wrap">
          <table>
            <thead><tr><th>Input</th><th>XBRL tag</th><th>Value</th><th>Period</th><th>Form</th><th>Accession</th><th>Filed</th></tr></thead>
            <tbody>
              {m.inputs.map((i, n) => (
                <tr key={n}>
                  <td>{i.label}{i.fallback_rank > 1 ? ` (fallback ${i.fallback_rank})` : ""}</td>
                  <td><code>{i.tag}</code></td>
                  <td className="num">{formatRaw(i.value, i.unit)}</td>
                  <td>{i.period}</td>
                  <td>{i.form}</td>
                  <td><a href={i.url} target="_blank" rel="noreferrer">{i.accession}</a></td>
                  <td>{i.filed}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function PassageSource({ source }: { source: Extract<DrawerSource, { kind: "passage" }> }) {
  const p = source.passage;
  return (
    <div>
      <h3>Quoted from the {p.form} for the period ended {p.period_end}</h3>
      <p>Section: {p.section}. Filed {p.filed}. <a href={p.url} target="_blank" rel="noreferrer">Open on EDGAR</a></p>
      <blockquote className="passage">{highlight(p.text, source.quote)}</blockquote>
      {source.verdict && (
        <p>Judge: <strong>{VERDICT_LABEL[source.verdict as keyof typeof VERDICT_LABEL] ?? source.verdict}</strong>
          {source.reason ? `: ${source.reason}` : ""}</p>
      )}
      <p className="note">Passage {source.chunkId}, characters {p.start} to {p.end} of the filing's text.</p>
    </div>
  );
}
