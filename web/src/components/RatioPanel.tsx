// The memo's ratio panel: a tile per ratio with three fiscal years and LTM as small bars, the maturity
// ladder as bars in $ millions, and the scorecard breakdown. Bar heights are drawing geometry only; every
// figure shown is an engine value, formatted as the engine formats it.
import type { ChecklistItem, MaturityLadder, Memo, Metric, TrendRow } from "../contracts/types";
import { formatDate, formatMillions, formatValue, toFixedPy } from "../format";
import type { OpenSource } from "../sources";

const PERIODS = ["FY-2", "FY-1", "FY0", "LTM"] as const;
const SHORT_STATUS: Partial<Record<Metric["status"], string>> = { not_available: "n/a", not_meaningful: "n.m.", net_cash: "net cash" };

/** Bar heights in pixels for the plain positive values; zero for the rest, which are drawn as a baseline. */
export function barHeights(values: (number | null)[], tallest: number, shortest = 4): number[] {
  const max = Math.max(0, ...values.filter((v): v is number => v !== null));
  return values.map((v) => (v !== null && v > 0 && max > 0 ? Math.max(shortest, Math.round((v / max) * tallest)) : 0));
}

function shortValue(t: TrendRow, period: string): string {
  const status = t.statuses[period] ?? "not_available";
  return SHORT_STATUS[status] ?? formatValue(t.values[period] ?? null, t.unit, status);
}

function Tile({ trend, metric, onOpen }: { trend: TrendRow; metric?: Metric; onOpen: OpenSource }) {
  const plain = PERIODS.map((p) => (trend.statuses[p] === "ok" ? trend.values[p] ?? null : null));
  const heights = barHeights(plain, 38);
  const ltmStatus = trend.statuses.LTM ?? "not_available";
  return (
    <button type="button" className="ratio-tile" disabled={!metric} title="Show source"
      onClick={() => metric && onOpen({ kind: "metric", key: `${trend.metric_id}:LTM`, metric })}>
      <div className="muted small">{trend.label}</div>
      <div className={`tile-chip${ltmStatus === "ok" ? "" : " chip-na"}`}>{formatValue(trend.values.LTM ?? null, trend.unit, ltmStatus)}</div>
      <div className="bars" aria-hidden="true">
        {PERIODS.map((p, n) => (
          <div key={p} className={`bar${p === "LTM" ? " bar-ltm" : ""}${heights[n] === 0 ? " bar-empty" : ""}`} style={{ height: heights[n] }} />
        ))}
      </div>
      <div className="bar-labels">
        {PERIODS.map((p) => (
          <div key={p} title={formatValue(trend.values[p] ?? null, trend.unit, trend.statuses[p] ?? "not_available")}>
            {shortValue(trend, p)}<div className="bar-period">{p}</div>
          </div>
        ))}
      </div>
    </button>
  );
}

function Ladder({ ladder, warnings }: { ladder: MaturityLadder; warnings: ChecklistItem[] }) {
  const heights = barHeights(ladder.buckets.map((b) => (b.status === "ok" ? b.value : null)), 118, 0);
  const columns = { gridTemplateColumns: `repeat(${ladder.buckets.length}, 1fr)` };
  return (
    <div id="ladder">
      <h2 className="eyebrow panel-head">Maturity ladder · $ millions by year after {formatDate(ladder.as_of)}</h2>
      <div className="ladder" style={columns}>
        {ladder.buckets.map((b, n) => (
          <div key={b.id} className="ladder-col">
            <span className="mono small">{b.status === "ok" && b.value !== null ? formatMillions(b.value) : "n/a"}</span>
            <div className="ladder-bar" style={{ height: heights[n] }} />
          </div>
        ))}
      </div>
      <div className="ladder-labels" style={columns}>
        {ladder.buckets.map((b) => <span key={b.id}>{b.label}</span>)}
      </div>
      <p className="muted small ladder-note">
        Total {formatValue(ladder.total, "USD", ladder.total === null ? "not_available" : "ok")} at {formatDate(ladder.as_of)}.
        {ladder.buckets.some((b) => b.status !== "ok") && " n/a = not available."}
      </p>
      {warnings.map((w) => <p key={w.id} className="warn small ladder-note">! {w.message} See reviewer checklist.</p>)}
    </div>
  );
}

function Scorecard({ memo }: { memo: Memo }) {
  const card = memo.scorecard;
  return (
    <div id="scorecard" className="min0">
      <h2 className="eyebrow panel-head">Scorecard · {card.grid_version}</h2>
      <div className="scroller ruled-top">
        <table className="data-table compact">
          <thead><tr><th>Factor</th><th className="num">Value</th><th className="num">Band</th><th className="num">Weight</th></tr></thead>
          <tbody>
            {card.factors.map((f) => {
              const unit = memo.metrics[`${f.id}:${f.period}`]?.unit ?? "";
              return (
                <tr key={f.id}>
                  <td>{f.label} <span className="muted small">{f.period}</span>{f.note && <div className="muted small">{f.note}</div>}</td>
                  <td className="num mono">{formatValue(f.value, unit, f.status)}</td>
                  <td className="num mono">{f.band ?? <span className="muted italic">not scored</span>}</td>
                  <td className="num mono">{toFixedPy(f.weight * 100, 0)}%</td>
                </tr>
              );
            })}
            <tr className="total-row">
              <td>Weighted score</td><td />
              <td className="num mono">{card.weighted_score === null ? "n/a" : toFixedPy(card.weighted_score, 2)}</td>
              <td className="num mono">→ {card.grade ?? "not available"}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p className="muted small">Band 1 is strongest, 6 weakest.{card.provisional ? " Provisional: fewer than six factors could be scored." : ""} {card.disclaimer}</p>
    </div>
  );
}

export function RatioPanel({ memo, onOpen }: { memo: Memo; onOpen: OpenSource }) {
  const ladderWarnings = memo.checklist.filter((c) => c.category === "reconciliation" && c.ref === "maturity_ladder");
  return (
    <section aria-label="Ratios" className="ratio-panel">
      <h2 className="eyebrow panel-head">Ratios · three fiscal years and last twelve months (LTM)</h2>
      <div className="tiles">
        {memo.trends.map((t) => <Tile key={t.metric_id} trend={t} metric={memo.metrics[`${t.metric_id}:LTM`]} onOpen={onOpen} />)}
      </div>
      {memo.trends.some((t) => PERIODS.some((p) => SHORT_STATUS[t.statuses[p] ?? "not_available"])) && (
        <p className="muted small">n/a = not available; n.m. = not meaningful.</p>
      )}
      <div className="panel-pair">
        {memo.maturity_ladder ? <Ladder ladder={memo.maturity_ladder} warnings={ladderWarnings} />
          : <div id="ladder"><h2 className="eyebrow panel-head">Maturity ladder</h2><p className="muted">Not available.</p></div>}
        <Scorecard memo={memo} />
      </div>
    </section>
  );
}
