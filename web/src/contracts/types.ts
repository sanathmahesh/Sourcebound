/* Generated from schema.json by scripts/gen-types.mjs (npm run gen:types). Do not edit by hand. */

export interface SourceboundDataContract {
  [k: string]: unknown;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "AboutDocument".
 */
export interface AboutDocument {
  group: "strategy" | "method" | "reference";
  id: string;
  markdown: string;
  source: string;
  title: string;
}
/**
 * data/published/about.json: the strategy documents, the method and the limitations, as Markdown.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "AboutFile".
 */
export interface AboutFile {
  disclaimer: string;
  documents: AboutDocument[];
  generated_at: string;
  schema_version: string;
}
/**
 * The request body. The ticker fixes which company's files the tools may read.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "AskRequest".
 */
export interface AskRequest {
  question: string;
  ticker: string;
}
/**
 * The answer. Claims have the memo's shape; only claims the judge marked supported are kept.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "AskResponse".
 */
export interface AskResponse {
  claims: MemoClaim[];
  data_to: string | null;
  disclaimer: string;
  judge_model: string;
  metrics: {
    [k: string]: Metric;
  };
  model: string;
  passages: {
    [k: string]: Passage;
  };
  question: string;
  removed: RemovedClaim[];
  schema_version: string;
  seconds: number;
  status: "ok" | "out_of_scope";
  ticker: string;
  trace: ToolTrace[];
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "MemoClaim".
 */
export interface MemoClaim {
  checked_by: "judge" | "deterministic";
  citations: MemoCitation[];
  evidence_quote: string;
  flags: string[];
  id: string;
  judge_reason: string;
  kind: "quantitative" | "qualitative";
  segments: Segment[];
  verdict: "supported" | "partially_supported" | "unsupported";
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "MemoCitation".
 */
export interface MemoCitation {
  check: "ok" | "chunk_not_found" | "quote_too_short" | "quote_not_found";
  chunk_id: string;
  quote: string;
}
/**
 * A piece of a rendered claim: plain text, an engine metric, or a figure quoted from a passage.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Segment".
 */
export interface Segment {
  chunk_id: string | null;
  metric_id: string | null;
  t: "text" | "metric" | "quoted";
  v: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Metric".
 */
export interface Metric {
  formula: string;
  inputs: MetricInput[];
  label: string;
  metric_id: string;
  notes: string[];
  period: string;
  status: "ok" | "not_available" | "not_meaningful" | "net_cash";
  unit: string;
  value: number | null;
}
/**
 * One XBRL fact behind a metric.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "MetricInput".
 */
export interface MetricInput {
  accession: string;
  concept: string;
  fallback_rank: number;
  filed: string;
  form: string;
  label: string;
  period: string;
  role: string;
  sign: number;
  tag: string;
  unit: string;
  url: string;
  value: number;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Passage".
 */
export interface Passage {
  accession: string;
  end: number;
  filed: string;
  form: string;
  period_end: string;
  section: string;
  start: number;
  text: string;
  url: string;
}
/**
 * A claim that failed verification and was taken out of the answer.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "RemovedClaim".
 */
export interface RemovedClaim {
  reason: string;
  text: string;
  verdict: "supported" | "partially_supported" | "unsupported";
}
/**
 * One tool call the model made, for the "what was looked up" list.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "ToolTrace".
 */
export interface ToolTrace {
  arguments: {
    [k: string]: unknown;
  };
  result: string;
  round: number;
  tool: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "CallTotals".
 */
export interface CallTotals {
  cached_input_tokens: number;
  calls: number;
  cost_usd: number;
  input_tokens: number;
  output_tokens: number;
  seconds: number;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "ChecklistItem".
 */
export interface ChecklistItem {
  category:
    | "not_available"
    | "fallback"
    | "assumed_zero"
    | "override"
    | "reconciliation"
    | "structural_change"
    | "provisional_grade"
    | "stale_data"
    | "unsupported_claim"
    | "partially_supported_claim"
    | "draft_problem";
  id: string;
  message: string;
  ref: string;
  severity: "info" | "warning";
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "ClaimCheck".
 */
export interface ClaimCheck {
  checked_by: string;
  citation_checks: string[];
  claim_id: string;
  flags: string[];
  kind: string;
  reason: string;
  section: string;
  verdict: "supported" | "partially_supported" | "unsupported";
}
/**
 * data/published/companies/<TICKER>/metrics.json: the latest metrics, possibly newer than the memo.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "CompanyMetrics".
 */
export interface CompanyMetrics {
  checklist: ChecklistItem[];
  cik: number;
  data_fetched_at: string | null;
  disclaimer: string;
  generated_at: string;
  log: LogItem[];
  maturity_ladder: MaturityLadder | null;
  metrics: {
    [k: string]: Metric;
  };
  name: string;
  period_problems: string[];
  periods: PeriodInfo[];
  schema_version: string;
  scorecard: Scorecard;
  scorecard_fy0: Scorecard;
  sector: string;
  sources: Source[];
  ticker: string;
  trends: TrendRow[];
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "LogItem".
 */
export interface LogItem {
  concept: string;
  kind: string;
  message: string;
  period: string;
  severity: "info" | "warning";
  subject: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "MaturityLadder".
 */
export interface MaturityLadder {
  as_of: string;
  buckets: LadderBucket[];
  metric_keys: string[];
  total: number | null;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "LadderBucket".
 */
export interface LadderBucket {
  id: string;
  label: string;
  metric_key: string;
  status: "ok" | "not_available" | "not_meaningful" | "net_cash";
  value: number | null;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "PeriodInfo".
 */
export interface PeriodInfo {
  balance_sheet_date: string;
  flow_windows: string[];
  label: string;
  note: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Scorecard".
 */
export interface Scorecard {
  basis: "latest" | "FY0";
  disclaimer: string;
  factors: ScorecardFactor[];
  grade: string | null;
  grid_version: string;
  ig_like: boolean | null;
  provisional: boolean;
  weighted_score: number | null;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "ScorecardFactor".
 */
export interface ScorecardFactor {
  band: number | null;
  effective_weight: number | null;
  id: string;
  label: string;
  note: string;
  period: string;
  status: "ok" | "not_available" | "not_meaningful" | "net_cash";
  value: number | null;
  weight: number;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Source".
 */
export interface Source {
  accession: string;
  filed: string;
  form: string;
  period_end: string;
  url: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "TrendRow".
 */
export interface TrendRow {
  direction: "improving" | "worsening" | "stable" | "not available";
  label: string;
  metric_id: string;
  statuses: {
    [k: string]: "ok" | "not_available" | "not_meaningful" | "net_cash";
  };
  unit: string;
  values: {
    [k: string]: number | null;
  };
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "CompanyState".
 */
export interface CompanyState {
  latest_10k: FilingRef | null;
  latest_10q: FilingRef | null;
  memo_date: string | null;
  memo_status: "current" | "stale" | "missing";
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "FilingRef".
 */
export interface FilingRef {
  accession: string;
  filed: string;
  form: string;
  period_end: string;
}
/**
 * data/published/evals.json: the evaluation results (evals/results/results.json), for the site.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "EvalsFile".
 */
export interface EvalsFile {
  generated_at: string;
  results: {
    [k: string]: unknown;
  };
  schema_version: string;
  source: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "HeadlineRatio".
 */
export interface HeadlineRatio {
  display: string;
  label: string;
  metric_id: string;
  period: string;
  status: "ok" | "not_available" | "not_meaningful" | "net_cash";
  unit: string;
  value: number | null;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "IndexEntry".
 */
export interface IndexEntry {
  data_to: string | null;
  flag_types: string[];
  grade: string | null;
  headline: HeadlineRatio[];
  ig_like: boolean | null;
  latest_filing: FilingRef | null;
  memo_date: string | null;
  memo_model: string | null;
  memo_status: "current" | "stale" | "missing";
  name: string;
  open_flags: number;
  provisional: boolean;
  score: number | null;
  sector: string;
  ticker: string;
  verification: VerificationCounts | null;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "VerificationCounts".
 */
export interface VerificationCounts {
  claims: number;
  partially_supported: number;
  supported: number;
  unsupported: number;
}
/**
 * data/published/companies/<TICKER>/memo.json: a dated snapshot with its own metrics and passages.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Memo".
 */
export interface Memo {
  checklist: ChecklistItem[];
  disclaimer: string;
  grade: string | null;
  grade_provisional: boolean;
  judge_model: string;
  maturity_ladder: MaturityLadder | null;
  memo_date: string;
  metrics: {
    [k: string]: Metric;
  };
  model: string;
  name: string;
  passages: {
    [k: string]: Passage;
  };
  run: RunInfo;
  schema_version: string;
  scorecard: Scorecard;
  sections: MemoSection[];
  sources: Source[];
  ticker: string;
  trends: TrendRow[];
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "RunInfo".
 */
export interface RunInfo {
  drafting: CallTotals;
  judge_model: string;
  prices_read_on: string;
  raw_outputs: string;
  reasoning_effort: {
    [k: string]: string;
  };
  run_id: string;
  service_tier: string;
  started_at: string;
  verification: CallTotals;
  writer_model: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "MemoSection".
 */
export interface MemoSection {
  claims: MemoClaim[];
  id: string;
  notes: string[];
  passages_shown: string[];
  title: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "NumberTrace".
 */
export interface NumberTrace {
  chunk_id: string | null;
  claim_id: string;
  kind: "metric" | "quoted";
  metric_id: string | null;
  value: string;
}
/**
 * data/published/index.json: one entry per company, for the portfolio page.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "SiteIndex".
 */
export interface SiteIndex {
  companies: IndexEntry[];
  disclaimer: string;
  generated_at: string;
  schema_version: string;
}
/**
 * data/published/companies/<TICKER>/verification.json
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "VerificationReport".
 */
export interface VerificationReport {
  claims: ClaimCheck[];
  fallback_log: LogItem[];
  judge_model: string;
  memo_date: string;
  numbers: NumberTrace[];
  schema_version: string;
  summary: VerificationSummary;
  ticker: string;
  warnings: LogItem[];
  writer_model: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "VerificationSummary".
 */
export interface VerificationSummary {
  checked_by_judge: number;
  checked_deterministically: number;
  claims: number;
  metric_figures: number;
  partially_supported: number;
  quoted_figures: number;
  raw_numbers_rejected: number;
  repairs: number;
  sections_without_draft: number;
  supported: number;
  unsupported: number;
}
/**
 * A headline ratio's change from the prior fiscal year-end (FY0) to the latest LTM, for the watchlist.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "WatchChange".
 */
export interface WatchChange {
  change: number | null;
  display: string;
  flagged: boolean;
  fy0: number | null;
  label: string;
  ltm: number | null;
  metric_id: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "WatchFlag".
 */
export interface WatchFlag {
  from: string;
  metric_id: string;
  rule: string;
  severity: "warning" | "alert";
  to: string;
  type: string;
}
/**
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "WatchItem".
 */
export interface WatchItem {
  changes: WatchChange[];
  data_to: string | null;
  flags: WatchFlag[];
  latest_filing: FilingRef | null;
  memo_date: string | null;
  memo_status: "current" | "stale" | "missing";
  name: string;
  ticker: string;
}
/**
 * data/published/state.json: what the daily job last saw for each company.
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "WatchState".
 */
export interface WatchState {
  checked_at: string;
  companies: {
    [k: string]: CompanyState;
  };
  last_heartbeat: string;
  schema_version: string;
}
/**
 * data/published/watchlist.json
 *
 * This interface was referenced by `SourceboundDataContract`'s JSON-Schema
 * via the `definition` "Watchlist".
 */
export interface Watchlist {
  checked_at: string;
  items: WatchItem[];
  schema_version: string;
}
