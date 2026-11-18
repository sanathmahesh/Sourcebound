// Screen 3: the verification report. Five summary tiles, then three tabs: every figure in the memo with its
// lineage, every claim with its verdict, reason and supporting quote, and the fallback log with data-quality
// warnings. Rows open the same source drawer as the memo.
import { useState } from "react";
import { readTicks } from "../components/Checklist";
import { claimPlainText } from "../components/ClaimText";
import { SourceDrawer } from "../components/SourceDrawer";
import type { Memo, MemoClaim, NumberTrace, VerificationReport } from "../contracts/types";
import { useJson } from "../data";
import { formatDate, SEVERITY, VERDICT } from "../format";
import type { DrawerSource } from "../sources";
import { signoffKey } from "./MemoPage";
import { LoadError, Loading } from "./Status";

const TABS = [["numbers", "Numbers"], ["claims", "Claims"], ["log", "Fallbacks and warnings"]] as const;
type Tab = (typeof TABS)[number][0];

function Tile({ label, value, note, tone }: { label: string; value: string; note: string; tone?: string }) {
  return (
    <div className="v-tile">
      <div className="muted small">{label}</div>
      <div className={`v-tile-value${tone ? ` ${tone}` : ""}`}>{value}</div>
      <div className="muted small">{note}</div>
    </div>
  );
}

export function VerificationPage({ ticker }: { ticker: string }) {
  const report = useJson<VerificationReport>(`/data/companies/${ticker}/verification.json`);
  const memo = useJson<Memo>(`/data/companies/${ticker}/memo.json`);
  const [tab, setTab] = useState<Tab>("numbers");
  const [source, setSource] = useState<DrawerSource | null>(null);
  if (report.state === "error" || memo.state === "error") return <main className="page"><LoadError what={`a verification report for ${ticker}`} /></main>;
  if (report.state !== "ok" || memo.state !== "ok") return <main className="page"><Loading what="the verification report" /></main>;

  const r = report.data, m = memo.data, s = r.summary;
  const claims: Record<string, MemoClaim> = Object.fromEntries(m.sections.flatMap((sec) => sec.claims.map((c) => [c.id, c])));
  const traced = r.numbers.filter((n) => isTraced(n, m)).length;
  const ticks = new Set(readTicks(signoffKey(m)));
  const open = m.checklist.filter((i) => !ticks.has(i.id)).length;
  const openClaim = (claim: MemoClaim, focus?: string) =>
    setSource({ kind: "claim", claim, passages: m.passages, judgeModel: m.judge_model, focus });
  const counts: Record<Tab, number> = { numbers: r.numbers.length, claims: r.claims.length, log: r.fallback_log.length + r.warnings.length };

  return (
    <>
      <main className="page">
        <a href={`#/memo/${ticker}`} className="back">← Memo</a>
        <div className="eyebrow head-gap">Verification report</div>
        <h1 className="page-title">{m.name} <span className="ticker-lg">{ticker}</span></h1>
        <p className="muted small">Memo of {formatDate(m.memo_date)} · written by <span className="mono">{r.writer_model}</span> · judged by <span className="mono">{r.judge_model}</span></p>
        <div className="v-tiles">
          <Tile label="Numbers traced" value={`${traced} / ${r.numbers.length}`}
            note={`${s.metric_figures} from XBRL, ${s.quoted_figures} quoted; ${r.numbers.length - traced} not available`} />
          <Tile label="Claims supported" value={`${VERDICT.supported.glyph} ${s.supported}`} note={`of ${s.claims} claims`} tone={s.supported ? "ok" : ""} />
          <Tile label="Partially supported" value={`${VERDICT.partially_supported.glyph} ${s.partially_supported}`}
            note="passage covers part of the claim" tone={s.partially_supported ? "warn" : ""} />
          <Tile label="Unsupported" value={`${VERDICT.unsupported.glyph} ${s.unsupported}`}
            note="passage does not support the claim" tone={s.unsupported ? "bad" : ""} />
          <Tile label="Checklist items open" value={String(open)} note={`of ${m.checklist.length} for sign-off`} />
        </div>
        <div role="tablist" className="tabs">
          {TABS.map(([id, label]) => (
            <button key={id} type="button" role="tab" id={`tab-${id}`} aria-selected={tab === id} aria-controls={`panel-${id}`}
              onClick={() => setTab(id)}>{label} <span className="mono small muted">{counts[id]}</span></button>
          ))}
        </div>
        <div role="tabpanel" id={`panel-${tab}`} aria-labelledby={`tab-${tab}`}>
          {tab === "numbers" && <NumbersTab report={r} memo={m} claims={claims} onMetric={setSource} onClaim={openClaim} />}
          {tab === "claims" && <ClaimsTab memo={m} onClaim={openClaim} />}
          {tab === "log" && <LogTab report={r} />}
        </div>
      </main>
      <SourceDrawer source={source} onClose={() => setSource(null)} />
    </>
  );
}

function isTraced(n: NumberTrace, m: Memo): boolean {
  if (n.kind === "metric") return !!n.metric_id && !!m.metrics[n.metric_id] && m.metrics[n.metric_id].status !== "not_available";
  return !!n.chunk_id && !!m.passages[n.chunk_id];
}

function NumbersTab({ report, memo, claims, onMetric, onClaim }: {
  report: VerificationReport; memo: Memo; claims: Record<string, MemoClaim>;
  onMetric: (s: DrawerSource) => void; onClaim: (c: MemoClaim, focus?: string) => void;
}) {
  return (
    <div className="scroller">
      <table className="data-table v-table">
        <thead><tr><th>Number</th><th className="num">Value</th><th>Lineage</th><th>Inputs</th><th>Notes</th><th /></tr></thead>
        <tbody>
          {report.numbers.map((n, i) => {
            const metric = n.metric_id ? memo.metrics[n.metric_id] : undefined;
            const passage = n.chunk_id ? memo.passages[n.chunk_id] : undefined;
            const claim = claims[n.claim_id];
            const openRow = () => {
              if (metric && n.metric_id) onMetric({ kind: "metric", key: n.metric_id, metric });
              else if (claim) onClaim(claim, n.chunk_id ?? undefined);
            };
            const traced = isTraced(n, memo);
            const fallback = metric?.inputs.some((x) => x.fallback_rank > 1);
            return (
              <tr key={i} className="clickable" onClick={openRow}>
                <td>
                  <div className="strong">{metric ? `${metric.label} · ${metric.period}` : "Quoted figure"}</div>
                  <div className="mono small muted">{n.metric_id ?? n.chunk_id} · in {n.claim_id}</div>
                </td>
                <td className={`num mono nowrap${traced ? "" : " muted"}`}>{n.kind === "quoted" ? `“${n.value}”` : n.value}</td>
                <td className={`nowrap${traced ? " ok" : " muted"}`}>
                  {!traced ? "○ not available"
                    : n.kind === "quoted" ? "✓ in the cited passage"
                    : metric!.inputs.length ? `✓ ${metric!.inputs.length} XBRL ${metric!.inputs.length === 1 ? "input" : "inputs"}`
                    : "ƒ from other figures"}
                </td>
                <td className="mono small tags">
                  {metric ? metric.inputs.map((x) => x.tag.replace("us-gaap:", "")).join(" · ") || "–"
                    : passage ? `${passage.form} · ${passage.section}` : "–"}
                </td>
                <td className="warn small-14">{fallback ? "! fallback tag" : ""}</td>
                <td className="num nowrap"><button type="button" className="row-link" onClick={(e) => { e.stopPropagation(); openRow(); }}>
                  {metric ? "Source →" : "Passage →"}</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function ClaimsTab({ memo, onClaim }: { memo: Memo; onClaim: (c: MemoClaim) => void }) {
  const claims = memo.sections.flatMap((s) => s.claims);
  return (
    <div className="scroller">
      <table className="data-table v-table claims-table">
        <thead><tr><th>Claim</th><th>Verdict</th><th>Judge’s reason</th><th>Supporting quote</th><th /></tr></thead>
        <tbody>
          {claims.map((c) => {
            const cite = c.citations[0];
            const passage = cite ? memo.passages[cite.chunk_id] : undefined;
            const v = VERDICT[c.verdict];
            return (
              <tr key={c.id} className="clickable" onClick={() => onClaim(c)}>
                <td className="claim-cell"><div className="serif-16">{claimPlainText(c)}</div><div className="mono small muted">{c.id}</div></td>
                <td className={`nowrap strong verdict-${c.verdict} verdict-colour`}>{v.glyph} {v.words}</td>
                <td className="small-14 reason-cell">{c.judge_reason}
                  {c.checked_by !== "judge" && <div className="muted small">Checked by code; no model was asked.</div>}</td>
                <td className="small-14 quote-cell">
                  {cite ? <><span className="hl">“{cite.quote}”</span>
                    <div className="muted small">{passage ? `${passage.form} · ${passage.section}` : cite.chunk_id}
                      {c.citations.length > 1 ? ` · and ${c.citations.length - 1} more` : ""}</div></>
                    : <span className="muted">No passage cited: figures computed from XBRL.</span>}
                </td>
                <td className="num nowrap"><button type="button" className="row-link" onClick={(e) => { e.stopPropagation(); onClaim(c); }}>
                  {cite ? "Passage →" : "Verdict →"}</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function LogTab({ report }: { report: VerificationReport }) {
  return (
    <>
      <h2 className="eyebrow panel-head log-head">Fallback log</h2>
      {report.fallback_log.length === 0 ? <p className="muted">None.</p> : (
        <div className="scroller">
          <table className="data-table">
            <thead><tr><th>Concept</th><th>Tag used</th><th>Period</th><th>Detail</th></tr></thead>
            <tbody>
              {report.fallback_log.map((f, n) => (
                <tr key={n}><td className="mono small-13">{f.concept}</td><td className="mono small-13 tags">{f.subject}</td>
                  <td className="nowrap">{f.period}</td><td className="small-14">{f.message}</td></tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <h2 className="eyebrow panel-head log-head ruled-bottom">Data-quality warnings</h2>
      {report.warnings.length === 0 && <p className="muted">None.</p>}
      {report.warnings.map((w, n) => (
        <div key={n} className="warning-row">
          <span className={`strong ${w.severity === "warning" ? "warn" : "muted"}`}>{SEVERITY[w.severity]}</span>
          <span className="mono small-13">{w.kind} · {w.concept} · {w.period}</span>
          <span>{w.message}</span>
        </div>
      ))}
    </>
  );
}
