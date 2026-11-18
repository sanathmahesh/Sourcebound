// Screen 2: the memo. Header and metadata, the stale banner, the ratio panel, a key to the chips and
// verdict labels, the six sections as prose made of claims, the reviewer checklist and the follow-up panel.
// Every figure and verdict label opens the source drawer.
import { useState } from "react";
import { AskPanel } from "../components/AskPanel";
import { Checklist, type ChecklistLink } from "../components/Checklist";
import { ClaimText } from "../components/ClaimText";
import { RatioPanel } from "../components/RatioPanel";
import { SourceDrawer } from "../components/SourceDrawer";
import type { ChecklistItem, Memo, SiteIndex } from "../contracts/types";
import { useJson } from "../data";
import { formatDate, VERDICT } from "../format";
import type { DrawerSource } from "../sources";
import { LoadError, Loading } from "./Status";

export const signoffKey = (memo: Memo) => `sourcebound:signoff:${memo.ticker}:${memo.run.run_id}`;

function Key() {
  return (
    <div className="key">
      <span className="strong ink">Key</span>
      <span className="key-item"><span className="chip chip-metric">figure</span> computed from XBRL</span>
      <span className="key-item"><span className="chip chip-quoted">“figure”</span> quoted from filing text</span>
      {(Object.keys(VERDICT) as (keyof typeof VERDICT)[]).map((v) => (
        <span key={v} className={`verdict verdict-${v} key-verdict`}>{VERDICT[v].glyph} {VERDICT[v].words}</span>
      ))}
    </div>
  );
}

export function MemoPage({ ticker }: { ticker: string }) {
  const memo = useJson<Memo>(`/data/companies/${ticker}/memo.json`);
  const index = useJson<SiteIndex>("/data/index.json");
  const [source, setSource] = useState<DrawerSource | null>(null);
  if (memo.state === "loading") return <main className="page"><Loading what="the memo" /></main>;
  if (memo.state === "error") return <main className="page"><LoadError what={`a memo for ${ticker}`} /></main>;

  const m = memo.data;
  const entry = index.state === "ok" ? index.data.companies.find((c) => c.ticker === ticker) : undefined;
  const stale = entry?.memo_status === "stale" && entry.latest_filing ? entry.latest_filing : null;
  const asOf = m.sources.map((s) => s.period_end).sort().at(-1);
  const claims = m.sections.flatMap((s) => s.claims);
  const supported = claims.filter((c) => c.verdict === "supported").length;
  const claimIds = new Set(claims.map((c) => c.id));
  const linkFor = (item: ChecklistItem): ChecklistLink => {
    if (claimIds.has(item.ref)) return { id: `claim-${item.ref}`, label: item.ref };
    if (item.category === "stale_data" && stale) return { id: "memo-stale", label: "banner" };
    if (item.ref === "scorecard") return { id: "scorecard", label: "scorecard" };
    if (item.ref.startsWith("maturity")) return { id: "ladder", label: "maturity ladder" };
    return null;
  };

  return (
    <>
      <main className="page memo-page" id="memo-top">
        <a href="#/" className="back">← Portfolio</a>
        <div className="memo-head">
          <div>
            <div className="eyebrow">Credit memo{entry ? ` · ${entry.sector}` : ""}</div>
            <h1 className="memo-title">{m.name} <span className="ticker-lg">{m.ticker}</span></h1>
          </div>
          <div className="grade-box">
            <span className="eyebrow">Internal grade</span>
            <span className="grade-big">{m.grade ?? "n/a"}</span>
            {m.grade_provisional && <span className="badge-warn">provisional: fewer than six factors</span>}
          </div>
        </div>
        <dl className="meta-grid">
          <div><dt>Memo date</dt><dd>{formatDate(m.memo_date)}</dd></div>
          <div><dt>Drafted by</dt><dd className="mono small">{m.model}</dd></div>
          <div className="meta-wide"><dt>Filings used</dt>
            <dd className="filings">
              {m.sources.map((s) => (
                <span key={s.accession}><a href={s.url} target="_blank" rel="noreferrer" className="mono small">{s.form} ↗</a>{" "}
                  period to {formatDate(s.period_end)}, filed {formatDate(s.filed)}</span>
              ))}
            </dd>
          </div>
          <div><dt>Verification</dt><dd><a href={`#/memo/${ticker}/verification`}>{supported} of {claims.length} claims supported →</a></dd></div>
        </dl>
        {stale && (
          <div role="status" className="stale-banner" id="memo-stale">
            <strong className="warn">! Stale</strong>
            <span className="grow">A newer filing exists ({stale.form} filed {formatDate(stale.filed)}). Figures below are as of {formatDate(asOf)}.</span>
            <a href="#/watchlist">See watchlist →</a>
          </div>
        )}
        <RatioPanel memo={m} onOpen={setSource} />
        <Key />
        <article className="memo-body">
          {m.sections.map((section) => (
            <section key={section.id} id={`sec-${section.id}`} className="memo-section">
              <h2 className="serif-h2">{section.title}</h2>
              {section.claims.length === 0 ? <p className="muted">No claims. {section.notes.join(" ")}</p> : (
                <p className="prose">
                  {section.claims.map((claim) => (
                    <span key={claim.id}>
                      <ClaimText claim={claim} metrics={m.metrics} passages={m.passages} judgeModel={m.judge_model} onOpen={setSource} />{" "}
                    </span>
                  ))}
                </p>
              )}
            </section>
          ))}
        </article>
        <div className="memo-column">
          <Checklist items={m.checklist} storageKey={signoffKey(m)} linkFor={linkFor} />
          <AskPanel ticker={ticker} onOpen={setSource} />
        </div>
      </main>
      <SourceDrawer source={source} onClose={() => setSource(null)} />
    </>
  );
}
