# Sourcebound: design brief

Paste this whole file into Claude Design.

**Product.** Sourcebound is a credit-analysis tool. It drafts a credit memo on a public company from its SEC filings and proves every figure and claim against source data. The audience is a bank credit analyst and the people who review that analyst's work. It is a portfolio project, so do not imitate any real bank's branding.

**The one idea the design must carry.** Provenance is the product. Any number can be clicked to show the filing fact it came from. Any claim can be clicked to show the passage that supports it and whether an independent check agreed. Unverified content is never hidden; it is visibly marked and listed for human sign-off.

**Tone.** A serious internal tool: dense, calm, legible. Tables and text come first. Works at laptop width and on a phone. Light and dark themes. Status must never rely on colour alone.

**Handoff format.** React and TypeScript components for a Vite app, styled with CSS variables for tokens. Components receive the JSON shapes below as props. No data-fetching logic and no component library that needs a server.

## Screens

**1. Portfolio (home).** A table of 15 companies.
- Columns: company, sector, internal grade (SB-1 to SB-6), debt / EBITDA, EBITDA / interest, latest filing and its date, memo status (current or stale), verification summary ("41 of 43 claims supported"), open watchlist flags.
- Filter by sector and by IG-like or HY-like. Sort by any column.
- A footer line states the data date and "Educational project. Not investment advice."

**2. Memo.** The core screen.
- *Header:* company, grade, memo date, the filings used with their filing dates, the model that drafted it.
- *Stale banner:* "A newer filing exists (10-Q filed [date]). Figures below are as of [date]." Links to the watchlist.
- *Ratio panel:* six ratios, each with three fiscal years plus LTM (last twelve months) as a small trend; a maturity-ladder bar chart by year; the scorecard breakdown (factor, value, band, weight).
- *Body:* six sections: business profile, financial risk, liquidity, maturity wall, key risks, rating rationale. Prose is made of claims.
- *Numbers* are inline chips of two visibly different kinds: computed from XBRL, or quoted from filing text.
- *Qualitative claims* end with a citation marker and carry a verdict state: supported, partially supported, unsupported.
- *Source drawer,* opened by clicking a number or citation.
  - For a number: the formula; a table of inputs (label, XBRL tag, value, period, form, accession number, filing date, link to EDGAR); a note if a fallback tag was used.
  - For a citation: the passage with the supporting quote highlighted, filing and section, link, the judge's verdict and one-line reason.
- *Reviewer checklist* at the end: items grouped by category (unsupported claim, figure not available, fallback used, reconciliation warning, stale data), each with a checkbox and a link to the place in the memo. A progress count and a "signed off" state when all are ticked. A note that sign-off is stored in this browser only.
- *Ask a follow-up:* an input below the memo. The answer uses the same chips, citations and verdicts. Beneath it sit a collapsible "what was looked up" trace and a "removed: could not be verified" list.
- *States:* thinking, rate-limited ("try again in a few minutes"), provider unavailable, out of scope.

**3. Verification report.** Per company.
- Summary tiles: numbers traced, claims supported / partial / unsupported, checklist items open.
- Tab 1: every number with its lineage.
- Tab 2: every claim with its passage, verdict and reason.
- Tab 3: the fallback log and data-quality warnings.

**4. Watchlist.**
- "Last checked" time.
- A row per company: latest filing, change in leverage and coverage against the prior year-end, flags with severity (information, warning, alert), memo status.
- Expanding a row shows each flag's before and after values and the rule that fired.
- Empty state: "No deterioration flags."

**5. Results.**
- One table per model: numeric accuracy, citation precision, unsupported-claim rate, cost per memo, time per memo. Each shows its sample size.
- Judge calibration: agreement with human labels, false-pass rate.
- Scorecard against agency ratings: rank correlation and IG/HY agreement.
- A short "how this was measured" note beside each figure.

**6. About.** Six plain-English documents with a side navigation: opportunity map (a scored table of 8 to 10 workflows), manual versus tool-assisted effort, model recommendation, risk and control table, rollout plan, decision log. Also: method (the grid and thresholds), model card, limitations. This is long-form reading with wide tables.

**Value states to design for:** "not available", "not meaningful", "net cash", provisional grade (fewer than six factors), loading, error.

## Data behind the screens

All values below are illustrative.

`GET /data/index.json` — screen 1
```json
{"generated_at":"2026-11-20","companies":[{"ticker":"EXMP","name":"Example Corp","sector":"Retail",
 "grade":"SB-3","score":2.9,"provisional":false,
 "headline":{"debt_to_ebitda":{"value":2.4,"status":"ok"},"interest_coverage":{"value":8.1,"status":"ok"}},
 "latest_filing":{"form":"10-Q","period_end":"2026-09-30","filed":"2026-10-28"},
 "memo_status":"current","verification":{"claims_total":43,"supported":41,"partial":1,"unsupported":1},
 "open_flags":1}]}
```

`GET /data/companies/{ticker}/memo.json` — screen 2
```json
{"ticker":"EXMP","memo_date":"2026-11-20","model":"<model id>","grade":"SB-3",
 "sources":[{"form":"10-K","accession":"0000000000-26-000001","period_end":"2025-12-31","filed":"2026-02-14","url":"https://www.sec.gov/..."}],
 "sections":[{"id":"liquidity","title":"Liquidity","claims":[
   {"id":"liq-1","kind":"quantitative","verdict":"traced",
    "segments":[{"t":"text","v":"Sources cover uses "},{"t":"metric","v":"1.8x","metric_id":"liquidity_coverage:LTM"},{"t":"text","v":"."}]},
   {"id":"liq-2","kind":"qualitative","verdict":"supported","judge_reason":"Passage states the facility size and expiry.",
    "segments":[{"t":"text","v":"The company has a "},{"t":"quoted","v":"$2.0 billion","chunk_id":"c-10k-0412"},{"t":"text","v":" revolver."}],
    "citations":[{"chunk_id":"c-10k-0412","quote":"a $2.0 billion revolving credit facility expiring in 2029"}]}]}],
 "metrics":{"liquidity_coverage:LTM":{"label":"Liquidity sources / uses","value":1.8,"unit":"x","status":"ok",
   "formula":"(cash + undrawn revolver + operating cash flow) / (debt due in 12 months + capex + dividends)",
   "inputs":[{"label":"Cash and equivalents","tag":"us-gaap:CashAndCashEquivalentsAtCarryingValue","fallback_rank":1,
     "value":1200000000,"unit":"USD","period":{"end":"2026-09-30"},"form":"10-Q","accession":"0000000000-26-000009","filed":"2026-10-28","url":"https://www.sec.gov/..."}]}},
 "passages":{"c-10k-0412":{"text":"...","section":"Liquidity and Capital Resources","form":"10-K","filed":"2026-02-14","url":"https://www.sec.gov/..."}},
 "trends":[{"metric":"debt_to_ebitda","points":[{"period":"FY2023","value":2.9},{"period":"FY2024","value":2.6},{"period":"FY2025","value":2.5},{"period":"LTM","value":2.4}]}],
 "maturity_ladder":[{"bucket":"Year 1","amount":500000000},{"bucket":"Year 2","amount":750000000}],
 "scorecard":{"factors":[{"id":"debt_to_ebitda","value":2.4,"band":3,"weight":0.2}],"weighted_score":2.9,"grade":"SB-3"},
 "checklist":[{"id":"ck-1","category":"unsupported_claim","severity":"warning","message":"Claim risk-4 is not supported by its cited passage.","ref":"risk-4"}]}
```

`GET /data/companies/{ticker}/verification.json` — screen 3
```json
{"summary":{"numbers_total":38,"numbers_traced":38,"claims_total":43,"supported":41,"partial":1,"unsupported":1,"checklist_open":4},
 "numbers":[{"metric_id":"debt_to_ebitda:LTM","value":2.4,"inputs_traced":4}],
 "claims":[{"claim_id":"risk-4","verdict":"unsupported","reason":"Passage discusses supplier risk, not refinancing.","quote_found":true}],
 "fallback_log":[{"concept":"interest_expense","tag_used":"us-gaap:InterestExpenseNonoperating","fallback_rank":2,"period":"FY2025"}],
 "warnings":[{"type":"ladder_reconciliation","message":"Maturity ladder sums to 96% of total debt."}]}
```

`GET /data/watchlist.json` — screen 4
```json
{"checked_at":"2026-11-20T11:05:00Z","items":[{"ticker":"EXMP","latest_filing":{"form":"10-Q","filed":"2026-10-28"},
 "memo_status":"stale","flags":[{"type":"leverage_up","severity":"warning","rule":"Debt / EBITDA rose by 0.5x or more since the last fiscal year-end",
 "metric_id":"debt_to_ebitda","from":2.5,"to":3.1}]}]}
```

`GET /data/evals.json` — screen 5
```json
{"run_date":"2026-11-20","models":[{"model":"<model id>","numeric_accuracy":{"value":0.99,"n":120},
 "citation_precision":{"value":0.93,"n":60},"unsupported_claim_rate":{"value":0.04,"n":60},
 "cost_per_memo_usd":0.08,"seconds_per_memo":95}],
 "judge":{"model":"<model id>","agreement":0.91,"false_pass_rate":0.03,"n":180},
 "scorecard_vs_agency":{"spearman":0.8,"n":15,"ig_hy_agreement":"13 of 15"}}
```

`POST /api/ask` — follow-up panel. Request: `{"ticker":"EXMP","question":"When does the revolver expire?"}`
```json
{"status":"ok","claims":[],"removed":[{"text":"...","reason":"Quote not found in cited passage."}],
 "metrics":{},"passages":{},"trace":[{"tool":"search_filing","args":{"query":"revolving credit facility expiry"},"results":5}],
 "model":"<model id>","seconds":9.2}
```
`claims` uses the same claim shape as `memo.json`. Other statuses: `out_of_scope`; HTTP 429 (rate limited); HTTP 503 (model provider unavailable).

About-page documents arrive as Markdown strings from `GET /data/about.json`: `{"documents":[{"id":"opportunity-map","title":"...","markdown":"..."}]}`.
