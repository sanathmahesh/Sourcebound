// Screen 3: the verification report. Summary tiles, then three tabs: numbers with their lineage, claims with
// their passage, verdict and reason, and the fallback log with data-quality warnings.
import { useState } from "react";
import { ClaimText } from "../components/ClaimText";
import { SourceDrawer } from "../components/SourceDrawer";
import type { LogItem, Memo, MemoClaim, VerificationReport } from "../contracts/types";
import { useJson } from "../data";
import { VERDICT_LABEL } from "../format";
import type { DrawerSource } from "../sources";
import { Status } from "./Status";

const TABS = ["Numbers", "Claims", "Fallbacks and warnings"] as const;

export function VerificationPage({ ticker }: { ticker: string }) {
  const report = useJson<VerificationReport>(`/data/companies/${ticker}/verification.json`);
  const memo = useJson<Memo>(`/data/companies/${ticker}/memo.json`);
  const [tab, setTab] = useState<(typeof TABS)[number]>("Numbers");
  const [source, setSource] = useState<DrawerSource | null>(null);
  if (report.state !== "ok" || memo.state !== "ok") {
    const failed = report.state === "error" || memo.state === "error";
    return <Status value={failed ? "error" : "loading"} message={failed ? `No report for ${ticker}.` : ""} />;
  }
  const r = report.data, m = memo.data;
  const s = r.summary;
  const claims: Record<string, MemoClaim> = Object.fromEntries(m.sections.flatMap((sec) => sec.claims.map((c) => [c.id, c])));

  return (
    <article>
      <h1>Verification report: {m.name} ({ticker})</h1>
      <p>Memo dated {r.memo_date} · written by {r.writer_model} · judged by {r.judge_model} ·{" "}
        <a href={`#/c/${ticker}`}>Back to the memo</a></p>
      <div className="tiles">
        <Tile label="Numbers traced" value={r.numbers.length} detail={`${s.metric_figures} from XBRL, ${s.quoted_figures} quoted`} />
        <Tile label="Supported" value={s.supported} detail={`of ${s.claims} claims`} />
        <Tile label="Partly supported" value={s.partially_supported} detail={`of ${s.claims} claims`} />
        <Tile label="Unsupported" value={s.unsupported} detail={`of ${s.claims} claims`} />
        <Tile label="Checklist items" value={m.checklist.length} detail="for the reviewer" />
        <Tile label="Raw numbers rejected" value={s.raw_numbers_rejected} detail={`${s.repairs} repairs`} />
      </div>
      <div role="tablist">
        {TABS.map((t) => (
          <button key={t} type="button" role="tab" aria-selected={tab === t} className={tab === t ? "tab on" : "tab"}
            onClick={() => setTab(t)}>{t}</button>
        ))}
      </div>

      {tab === "Numbers" && (
        <div className="table-wrap" role="tabpanel">
          <table>
            <thead><tr><th>Claim</th><th>Kind</th><th>Value</th><th>Source</th></tr></thead>
            <tbody>
              {r.numbers.map((n, i) => {
                const metric = n.metric_id ? m.metrics[n.metric_id] : undefined;
                const passage = n.chunk_id ? m.passages[n.chunk_id] : undefined;
                return (
                  <tr key={i}>
                    <td><a href={`#/c/${ticker}`}>{n.claim_id}</a></td>
                    <td>{n.kind === "metric" ? "computed from XBRL" : "quoted from filing"}</td>
                    <td className="num">{n.value}</td>
                    <td>
                      {metric && <button type="button" className="link" onClick={() => setSource({ kind: "metric", key: n.metric_id!, metric })}>
                        {n.metric_id}: {metric.formula}</button>}
                      {passage && <button type="button" className="link" onClick={() => setSource({ kind: "passage", chunkId: n.chunk_id!, passage })}>
                        {passage.form} {passage.period_end}, {passage.section}</button>}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {tab === "Claims" && (
        <div className="table-wrap" role="tabpanel">
          <table>
            <thead><tr><th>Claim</th><th>Text</th><th>Verdict</th><th>Checked by</th><th>Reason</th></tr></thead>
            <tbody>
              {r.claims.map((c) => (
                <tr key={c.claim_id}>
                  <td>{c.claim_id}<br /><span className="note">{c.section}</span></td>
                  <td>{claims[c.claim_id] && <ClaimText claim={claims[c.claim_id]} metrics={m.metrics} passages={m.passages} onOpen={setSource} />}</td>
                  <td>{VERDICT_LABEL[c.verdict]}</td>
                  <td>{c.checked_by === "judge" ? "judge" : "code (number or quote check)"}</td>
                  <td>{c.reason}{c.flags.length > 0 && <><br /><span className="note">{c.flags.join("; ")}</span></>}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {tab === "Fallbacks and warnings" && (
        <div role="tabpanel">
          <h2>Fallback log ({r.fallback_log.length})</h2>
          <LogTable items={r.fallback_log} />
          <h2>Data-quality warnings ({r.warnings.length})</h2>
          <LogTable items={r.warnings} />
        </div>
      )}
      <SourceDrawer source={source} onClose={() => setSource(null)} />
    </article>
  );
}

function Tile({ label, value, detail }: { label: string; value: number; detail: string }) {
  return <div className="tile"><div className="tile-value">{value}</div><div>{label}</div><div className="note">{detail}</div></div>;
}

function LogTable({ items }: { items: LogItem[] }) {
  if (items.length === 0) return <p>None.</p>;
  return (
    <div className="table-wrap">
      <table>
        <thead><tr><th>Kind</th><th>Concept</th><th>Period</th><th>Severity</th><th>Message</th></tr></thead>
        <tbody>
          {items.map((i, n) => (
            <tr key={n}><td>{i.kind}</td><td>{i.concept}</td><td>{i.period}</td><td>{i.severity}</td><td>{i.message}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
