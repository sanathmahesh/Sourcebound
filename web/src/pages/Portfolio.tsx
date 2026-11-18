// Screen 1: the 15 companies, filterable by sector and IG-like / HY-like, sortable by any column.
import { type ReactNode, useState } from "react";
import type { IndexEntry, SiteIndex } from "../contracts/types";
import { useJson } from "../data";
import { Status } from "./Status";

type Column = { id: string; label: string; sort: (e: IndexEntry) => string | number | null; show: (e: IndexEntry) => ReactNode };

function headline(e: IndexEntry, metricId: string) {
  return e.headline.find((h) => h.metric_id === metricId);
}

const COLUMNS: Column[] = [
  { id: "company", label: "Company", sort: (e) => e.name, show: (e) => <a href={`#/c/${e.ticker}`}>{e.name} ({e.ticker})</a> },
  { id: "sector", label: "Sector", sort: (e) => e.sector, show: (e) => e.sector },
  { id: "grade", label: "SB grade", sort: (e) => e.score,
    show: (e) => e.grade ? <>{e.grade}{e.provisional && <span className="tag">provisional</span>}</> : "not available" },
  ...["debt_to_ebitda", "interest_coverage"].map((id): Column => ({
    id, label: id === "debt_to_ebitda" ? "Debt / EBITDA (LTM)" : "EBITDA / interest (LTM)",
    sort: (e) => headline(e, id)?.value ?? null, show: (e) => headline(e, id)?.display ?? "not available",
  })),
  { id: "filing", label: "Latest filing", sort: (e) => e.latest_filing?.filed ?? null,
    show: (e) => e.latest_filing ? `${e.latest_filing.form} filed ${e.latest_filing.filed}` : "none" },
  { id: "memo", label: "Memo", sort: (e) => e.memo_status, show: (e) => <Status value={e.memo_status} /> },
  { id: "verification", label: "Verification", sort: (e) => e.verification ? e.verification.supported / Math.max(1, e.verification.claims) : null,
    show: (e) => e.verification ? `${e.verification.supported} of ${e.verification.claims} claims supported` : "no memo" },
  { id: "flags", label: "Open flags", sort: (e) => e.open_flags, show: (e) => e.open_flags },
];

function compare(a: string | number | null, b: string | number | null): number {
  if (a === null) return b === null ? 0 : 1;  // missing values last
  if (b === null) return -1;
  return a < b ? -1 : a > b ? 1 : 0;
}

export function Portfolio() {
  const index = useJson<SiteIndex>("/data/index.json");
  const [sector, setSector] = useState("all");
  const [grade, setGrade] = useState("all");
  const [sort, setSort] = useState<{ id: string; dir: 1 | -1 }>({ id: "company", dir: 1 });
  if (index.state !== "ok") return <Status value={index.state} message={index.state === "error" ? index.message : ""} />;

  const companies = index.data.companies;
  const sectors = [...new Set(companies.map((c) => c.sector))].sort();
  const column = COLUMNS.find((c) => c.id === sort.id)!;
  const rows = companies
    .filter((c) => sector === "all" || c.sector === sector)
    .filter((c) => grade === "all" || (grade === "ig" ? c.ig_like === true : c.ig_like === false))
    .sort((a, b) => sort.dir * compare(column.sort(a), column.sort(b)));

  return (
    <section>
      <h1>Portfolio</h1>
      <div className="filters">
        <label>Sector{" "}
          <select value={sector} onChange={(e) => setSector(e.target.value)}>
            <option value="all">All</option>
            {sectors.map((s) => <option key={s}>{s}</option>)}
          </select>
        </label>
        <label>Grade band{" "}
          <select value={grade} onChange={(e) => setGrade(e.target.value)}>
            <option value="all">All</option>
            <option value="ig">IG-like (SB-1 to SB-3)</option>
            <option value="hy">HY-like (SB-4 to SB-6)</option>
          </select>
        </label>
        <span className="note">{rows.length} of {companies.length} companies</span>
      </div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              {COLUMNS.map((c) => (
                <th key={c.id} aria-sort={sort.id === c.id ? (sort.dir === 1 ? "ascending" : "descending") : "none"}>
                  <button type="button" className="sort"
                    onClick={() => setSort({ id: c.id, dir: sort.id === c.id ? (-sort.dir as 1 | -1) : 1 })}>
                    {c.label}{sort.id === c.id ? (sort.dir === 1 ? " ▲" : " ▼") : ""}
                  </button>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((e) => <tr key={e.ticker}>{COLUMNS.map((c) => <td key={c.id}>{c.show(e)}</td>)}</tr>)}
          </tbody>
        </table>
      </div>
    </section>
  );
}
