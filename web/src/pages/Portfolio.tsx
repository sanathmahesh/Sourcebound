// Screen 1: the 15 companies, filterable by sector and by IG-like or HY-like, sortable by any column.
// Ratios are shown as the Python engine formatted them (HeadlineRatio.display).
import { type ReactNode, useState } from "react";
import type { IndexEntry, SiteIndex } from "../contracts/types";
import { useJson } from "../data";
import { formatDate } from "../format";
import { LoadError, Loading, MemoStatus } from "./Status";

type Key = string | number | null;
type Column = { id: string; label: string; numeric?: boolean; sort: (e: IndexEntry) => Key; show: (e: IndexEntry) => ReactNode };

function Ratio({ entry, metricId }: { entry: IndexEntry; metricId: string }) {
  const h = entry.headline.find((r) => r.metric_id === metricId);
  if (!h) return <span className="muted italic">not available</span>;
  return <span className={h.status === "ok" ? "" : "muted italic"}>{h.display}</span>;
}

function ratioKey(e: IndexEntry, metricId: string): Key {
  const h = e.headline.find((r) => r.metric_id === metricId);
  return h && h.status === "ok" ? h.value : null;
}

function Verification({ entry }: { entry: IndexEntry }) {
  const v = entry.verification;
  if (!v) return <span className="muted">no memo</span>;
  const note = [v.partially_supported ? `${v.partially_supported} partial` : "", v.unsupported ? `${v.unsupported} unsupported` : ""]
    .filter(Boolean).join(", ");
  return <>{v.supported} of {v.claims} supported{note && <> <span className={`small ${v.unsupported ? "bad" : "warn"}`}>({note})</span></>}</>;
}

const COLUMNS: Column[] = [
  { id: "company", label: "Company", sort: (e) => e.name,
    show: (e) => <><a href={`#/memo/${e.ticker}`} className="company-link">{e.name}</a> <span className="ticker">{e.ticker}</span></> },
  { id: "sector", label: "Sector", sort: (e) => e.sector, show: (e) => <span className="muted">{e.sector}</span> },
  { id: "grade", label: "Grade", sort: (e) => e.score,
    show: (e) => <span className="nowrap">{e.grade ? <span className="mono grade">{e.grade}</span> : <span className="muted italic">not available</span>}
      {e.provisional && <> <span className="badge-warn" title="Fewer than six factors available">provisional</span></>}</span> },
  { id: "debt_to_ebitda", label: "Debt / EBITDA", numeric: true, sort: (e) => ratioKey(e, "debt_to_ebitda"),
    show: (e) => <Ratio entry={e} metricId="debt_to_ebitda" /> },
  { id: "interest_coverage", label: "EBITDA / interest", numeric: true, sort: (e) => ratioKey(e, "interest_coverage"),
    show: (e) => <Ratio entry={e} metricId="interest_coverage" /> },
  { id: "filing", label: "Latest filing", sort: (e) => e.latest_filing?.filed ?? null,
    show: (e) => e.latest_filing ? <span className="nowrap"><span className="mono">{e.latest_filing.form}</span>{" "}
      <span className="muted">{formatDate(e.latest_filing.filed)}</span></span> : <span className="muted">none</span> },
  { id: "memo", label: "Memo", sort: (e) => e.memo_status, show: (e) => <span className="nowrap"><MemoStatus status={e.memo_status} /></span> },
  { id: "verification", label: "Verification", sort: (e) => e.verification ? e.verification.supported / Math.max(1, e.verification.claims) : null,
    show: (e) => <span className="nowrap"><Verification entry={e} /></span> },
  { id: "flags", label: "Flags", numeric: true, sort: (e) => e.open_flags,
    show: (e) => e.open_flags ? <span className="mono">{e.open_flags}</span> : <span className="mono muted">–</span> },
];

function compare(a: Key, b: Key): number {
  if (a === null) return b === null ? 0 : 1;  // missing values last
  if (b === null) return -1;
  if (typeof a === "string" && typeof b === "string") return a.localeCompare(b, "en", { sensitivity: "base" });
  return a < b ? -1 : a > b ? 1 : 0;
}

const CLASSES = [["all", "All"], ["ig", "IG-like"], ["hy", "HY-like"]] as const;

export function Portfolio() {
  const index = useJson<SiteIndex>("/data/index.json");
  const [sector, setSector] = useState("all");
  const [grade, setGrade] = useState<(typeof CLASSES)[number][0]>("all");
  const [sort, setSort] = useState<{ id: string; dir: 1 | -1 }>({ id: "company", dir: 1 });
  const companies = index.state === "ok" ? index.data.companies : [];
  const sectors = [...new Set(companies.map((c) => c.sector))].sort();
  const column = COLUMNS.find((c) => c.id === sort.id)!;
  const rows = companies
    .filter((c) => sector === "all" || c.sector === sector)
    .filter((c) => grade === "all" || (grade === "ig" ? c.ig_like === true : c.ig_like === false))
    .sort((a, b) => sort.dir * compare(column.sort(a), column.sort(b)));
  const open = (ticker: string) => { window.location.hash = `#/memo/${ticker}`; };

  return (
    <main className="page">
      <div className="page-head">
        <div>
          <h1 className="page-title">Portfolio</h1>
          <p className="muted lede-tight">{rows.length} of {companies.length} companies. IG-like is SB-1 to SB-3; HY-like is SB-4 to SB-6.</p>
        </div>
        <div className="filters">
          <label className="filter-label">Sector
            <select value={sector} onChange={(e) => setSector(e.target.value)}>
              <option value="all">All sectors</option>
              {sectors.map((s) => <option key={s} value={s}>{s}</option>)}
            </select>
          </label>
          <div role="group" aria-label="Grade class" className="segmented">
            {CLASSES.map(([id, label]) => (
              <button key={id} type="button" aria-pressed={grade === id} onClick={() => setGrade(id)}>{label}</button>
            ))}
          </div>
        </div>
      </div>
      {index.state === "loading" && <Loading what="portfolio data" />}
      {index.state === "error" && <LoadError what="portfolio data" />}
      {index.state === "ok" && (
        <>
          <div className="scroller ruled-top">
            <table className="data-table portfolio-table">
              <thead>
                <tr>
                  {COLUMNS.map((c) => (
                    <th key={c.id} className={c.numeric ? "num" : ""}
                      aria-sort={sort.id === c.id ? (sort.dir === 1 ? "ascending" : "descending") : "none"}>
                      <button type="button" className="sort"
                        onClick={() => setSort({ id: c.id, dir: sort.id === c.id ? (-sort.dir as 1 | -1) : 1 })}>
                        {c.label} <span className="arrow">{sort.id === c.id ? (sort.dir === 1 ? "▲" : "▼") : ""}</span>
                      </button>
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.map((e) => (
                  <tr key={e.ticker} className="clickable" onClick={() => open(e.ticker)}>
                    {COLUMNS.map((c) => <td key={c.id} className={c.numeric ? "num mono" : ""}>{c.show(e)}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {rows.length === 0 && companies.length > 0 && <p className="empty">No companies match these filters.</p>}
        </>
      )}
    </main>
  );
}
