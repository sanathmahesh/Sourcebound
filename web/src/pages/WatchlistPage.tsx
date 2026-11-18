// Screen 4: the watchlist. When it was last checked; a row per company with its latest filing, the change in
// Debt / EBITDA and EBITDA / interest since the prior fiscal year-end (computed by the Python watchlist job),
// its flags by severity and its memo status. Expanding a row shows each flag's values and the rule that fired.
import { useState } from "react";
import type { WatchFlag, Watchlist } from "../contracts/types";
import { useJson } from "../data";
import { formatDate, SEVERITY } from "../format";
import { LoadError, Loading, MemoStatus } from "./Status";

const FLAG_LABEL: Record<string, string> = {
  leverage_up: "Debt / EBITDA up",
  coverage_down: "EBITDA / interest down",
  liquidity_shortfall: "Liquidity coverage low",
  near_term_maturities: "Debt due within 12 months",
  grade_change: "Worse SB grade",
};

const CHANGE_COLUMNS = [["debt_to_ebitda", "Δ Debt / EBITDA"], ["interest_coverage", "Δ EBITDA / interest"]] as const;

function FlagBadge({ flag }: { flag: WatchFlag }) {
  return <span className={`flag-badge flag-${flag.severity}`}>{SEVERITY[flag.severity]}</span>;
}

export function WatchlistPage() {
  const watch = useJson<Watchlist>("/data/watchlist.json");
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  if (watch.state === "loading") return <main className="page"><Loading what="the watchlist" /></main>;
  if (watch.state === "error") return <main className="page"><LoadError what="the watchlist" /></main>;
  const w = watch.data;
  const toggle = (ticker: string) => {
    const next = new Set(expanded);
    if (next.has(ticker)) next.delete(ticker);
    else next.add(ticker);
    setExpanded(next);
  };

  return (
    <main className="page">
      <h1 className="page-title">Watchlist</h1>
      <p className="muted lede-tight page-sub">
        Last checked {formatDate(w.checked_at)}, {w.checked_at.slice(11, 16)} UTC. Changes are against the prior fiscal year-end.
      </p>
      <div className="scroller ruled-top">
        <table className="data-table watch-table">
          <thead>
            <tr>
              <th className="expander-col" /><th>Company</th><th>Latest filing</th>
              {CHANGE_COLUMNS.map(([id, label]) => <th key={id} className="num">{label}</th>)}
              <th>Flags</th><th>Memo</th>
            </tr>
          </thead>
          {w.items.map((item) => {
            const open = expanded.has(item.ticker) && item.flags.length > 0;
            return (
              <tbody key={item.ticker}>
                <tr data-testid={`watch-${item.ticker}`} className={item.flags.length ? "clickable" : ""}
                  onClick={() => item.flags.length && toggle(item.ticker)}>
                  <td className="expander-col">
                    {item.flags.length > 0 && (
                      <button type="button" className="expander" aria-expanded={open} aria-label={`Show flag detail for ${item.name}`}
                        onClick={(e) => { e.stopPropagation(); toggle(item.ticker); }}>{open ? "▾" : "▸"}</button>
                    )}
                  </td>
                  <td><span className="company-name">{item.name}</span> <span className="ticker">{item.ticker}</span></td>
                  <td className="nowrap">{item.latest_filing ? <><span className="mono">{item.latest_filing.form}</span>{" "}
                    <span className="muted">{formatDate(item.latest_filing.filed)}</span></> : <span className="muted">none</span>}</td>
                  {CHANGE_COLUMNS.map(([id]) => {
                    const change = item.changes.find((c) => c.metric_id === id);
                    const plain = change?.change !== null && change?.change !== undefined;
                    const className = `${plain ? "" : "muted italic"}${change?.flagged ? " delta-flagged" : ""}`;
                    return (
                      <td key={id} className="num mono">
                        <span data-metric={id} className={className} title={change?.flagged ? "A watch flag fired on this ratio" : undefined}>
                          {change?.display ?? "not available"}
                        </span>
                      </td>
                    );
                  })}
                  <td>
                    <div className="flag-list">
                      {item.flags.map((f, n) => <FlagBadge key={n} flag={f} />)}
                      {item.flags.length === 0 && <span className="muted">No deterioration flags.</span>}
                    </div>
                  </td>
                  <td className="nowrap"><a href={`#/memo/${item.ticker}`} className="inherit" onClick={(e) => e.stopPropagation()}>
                    <MemoStatus status={item.memo_status} /></a></td>
                </tr>
                {open && (
                  <tr className="flag-detail">
                    <td />
                    <td colSpan={6}>
                      {item.flags.map((f, n) => (
                        <div key={n} className="flag-line">
                          <span className={`strong flag-text-${f.severity}`}>{SEVERITY[f.severity]}</span>
                          <span>{FLAG_LABEL[f.type] ?? f.type}</span>
                          <span className="mono">{f.from} → {f.to}</span>
                          <span className="muted">Rule: {f.rule}</span>
                        </div>
                      ))}
                    </td>
                  </tr>
                )}
              </tbody>
            );
          })}
        </table>
      </div>
      <p className="muted small page-note">Severity: ! warning, ‼ alert. Ratio changes in bold red are ones a flag fired on.</p>
    </main>
  );
}
