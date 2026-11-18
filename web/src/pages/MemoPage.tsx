// Screen 2: the memo. Header, stale banner, ratio panel, the six sections, the reviewer checklist and the
// follow-up panel. Every figure and citation opens the source drawer.
import { useState } from "react";
import { AskPanel } from "../components/AskPanel";
import { Checklist } from "../components/Checklist";
import { ClaimText } from "../components/ClaimText";
import { SourceDrawer } from "../components/SourceDrawer";
import type { Memo, SiteIndex } from "../contracts/types";
import { useJson } from "../data";
import { formatValue, toFixedPy } from "../format";
import type { DrawerSource } from "../sources";
import { Status } from "./Status";

const PERIODS = ["FY-2", "FY-1", "FY0", "LTM"];

export function MemoPage({ ticker }: { ticker: string }) {
  const memo = useJson<Memo>(`/data/companies/${ticker}/memo.json`);
  const index = useJson<SiteIndex>("/data/index.json");
  const [source, setSource] = useState<DrawerSource | null>(null);
  if (memo.state !== "ok") {
    return <Status value={memo.state} message={memo.state === "error" ? `No memo for ${ticker}.` : ""} />;
  }
  const m = memo.data;
  const entry = index.state === "ok" ? index.data.companies.find((c) => c.ticker === ticker) : undefined;
  const dataTo = m.sources.map((s) => s.period_end).sort().at(-1);

  return (
    <article className="memo">
      <header>
        <h1>{m.name} ({m.ticker})</h1>
        <p>
          <strong>SB grade {m.grade ?? "not available"}</strong>
          {m.grade_provisional && <span className="tag">provisional: fewer than six factors scored</span>}
          {" · "}Memo dated {m.memo_date} · drafted by {m.model}, checked by {m.judge_model}
          {" · "}<a href={`#/c/${ticker}/verification`}>Verification report</a>
        </p>
        <details>
          <summary>Filings used ({m.sources.length})</summary>
          <ul>
            {m.sources.map((s) => (
              <li key={s.accession}>{s.form} for the period ended {s.period_end}, filed {s.filed}:{" "}
                <a href={s.url} target="_blank" rel="noreferrer">{s.accession}</a></li>
            ))}
          </ul>
        </details>
      </header>

      {entry?.memo_status === "stale" && entry.latest_filing && (
        <p className="banner" role="note">
          <strong>Stale.</strong> A newer filing exists ({entry.latest_filing.form} filed {entry.latest_filing.filed}).
          Figures below are as of {dataTo}. <a href="#/watchlist">See the watchlist</a>.
        </p>
      )}

      <section className="ratios" aria-label="Ratio panel">
        <h2>Ratios</h2>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Ratio</th>{PERIODS.map((p) => <th key={p}>{p}</th>)}<th>Direction</th></tr></thead>
            <tbody>
              {m.trends.map((t) => (
                <tr key={t.metric_id}>
                  <td>{t.label}</td>
                  {PERIODS.map((p) => (
                    <td key={p} className="num">{formatValue(t.values[p] ?? null, t.unit, t.statuses[p] ?? "not_available")}</td>
                  ))}
                  <td>{t.direction}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <h3>Maturity ladder</h3>
        {m.maturity_ladder ? (
          <div className="table-wrap">
            <table>
              <thead><tr><th>Due</th><th>Amount</th></tr></thead>
              <tbody>
                {m.maturity_ladder.buckets.map((b) => (
                  <tr key={b.id}><td>{b.label}</td><td className="num">{formatValue(b.value, "USD", b.status)}</td></tr>
                ))}
                <tr><td>Total (as of {m.maturity_ladder.as_of})</td>
                  <td className="num">{formatValue(m.maturity_ladder.total, "USD", m.maturity_ladder.total === null ? "not_available" : "ok")}</td></tr>
              </tbody>
            </table>
          </div>
        ) : <p>Maturity ladder not available.</p>}

        <h3>Scorecard ({m.scorecard.grid_version})</h3>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Factor</th><th>Value</th><th>Band (1 strongest, 6 weakest)</th><th>Weight</th></tr></thead>
            <tbody>
              {m.scorecard.factors.map((f) => {
                const metric = m.metrics[`${f.id}:${f.period}`];
                return (
                  <tr key={f.id}>
                    <td>{f.label} ({f.period})</td>
                    <td className="num">{formatValue(f.value, metric?.unit ?? "", f.status)}</td>
                    <td className="num">{f.band ?? "not scored"}</td>
                    <td className="num">{toFixedPy(f.weight * 100, 0)}%</td>
                  </tr>
                );
              })}
              <tr>
                <td colSpan={2}><strong>Weighted score and grade</strong></td>
                <td className="num">{m.scorecard.weighted_score === null ? "not available" : toFixedPy(m.scorecard.weighted_score, 2)}</td>
                <td>{m.scorecard.grade ?? "not available"}{m.scorecard.provisional ? " (provisional)" : ""}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p className="note">{m.scorecard.disclaimer}</p>
      </section>

      {m.sections.map((section) => (
        <section key={section.id} className="memo-section">
          <h2>{section.title}</h2>
          {section.claims.length === 0 && <p className="note">No claims. {section.notes.join(" ")}</p>}
          <ul className="claims">
            {section.claims.map((claim) => (
              <li key={claim.id}>
                <ClaimText claim={claim} metrics={m.metrics} passages={m.passages} onOpen={setSource} />
                {claim.flags.length > 0 && <span className="note"> ({claim.flags.join("; ")})</span>}
              </li>
            ))}
          </ul>
        </section>
      ))}

      <Checklist items={m.checklist} storageKey={`sourcebound:signoff:${ticker}:${m.run.run_id}`} />
      <AskPanel ticker={ticker} onOpen={setSource} />
      <SourceDrawer source={source} onClose={() => setSource(null)} />
    </article>
  );
}
