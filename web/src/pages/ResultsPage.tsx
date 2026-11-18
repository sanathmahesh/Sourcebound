// Screen 5: evaluation results from /data/evals.json. One block per writer model, then judge calibration,
// seeded errors, and engine, retrieval and scorecard checks. Every figure shows its sample size; measures that
// needed human labels or hand-checked values say "not measured" (no human evaluation was done, D62).
// evals.json "results" is an untyped object in the contract (EvalsFile.results: dict); the shapes below are
// what sourcebound/evals/report.py writes, read defensively.
import type { EvalsFile } from "../contracts/types";
import { useJson } from "../data";
import { formatDate, formatPct, toFixedPy } from "../format";
import { LoadError, Loading } from "./Status";

type Rate = { value: number | null; n: number };
interface Writer {
  model: string; memos_run1: number; claims_per_memo: number; judge_supported: Rate; judge_partially: Rate;
  judge_unsupported: Rate; raw_numbers_rejected_per_memo: number; cost_total_per_memo: number; model_seconds_per_memo: number;
  run_to_run_judge_supported?: { mean: number; min: number; max: number; n: number };
}
interface Results {
  generated_at: string; command: string; prices_read_on: string;
  writers: Record<string, Writer>;
  memo_numeric_accuracy: Record<string, { engine_figures: Rate; quoted_figures_in_cited_passage: Rate }>;
  engine_accuracy: { accuracy: Rate };
  retrieval_recall: { top8: Rate };
  labels: { labelled_rows: number; sheet_rows: number;
    per_writer: Record<string, { unsupported_rate: Rate; citation_precision: Rate }> };
  judge_calibration: Record<string, { rows_judged: number; cost_usd: number; agreement: Rate; false_pass_rate: Rate }>;
  seeded_errors: Record<string, Record<string, { n: number; code: number; judge_unsupported: number; judge_partial: number; missed: number }>>;
  scorecard_vs_agencies: { status?: string };
}

type Row = { measure: string; result: string; sample: string; how: string };

const NOT_MEASURED = "not measured";
const rate = (r: Rate | undefined) => (r && r.value !== null ? formatPct(r.value) : NOT_MEASURED);
const sample = (n: number | undefined) => `n = ${n ?? 0}`;

function writerRows(name: string, w: Writer, r: Results): Row[] {
  const memos = sample(w.memos_run1);
  const accuracy = r.memo_numeric_accuracy?.[name];
  const labels = r.labels?.per_writer?.[name];
  const spread = w.run_to_run_judge_supported;
  return [
    { measure: "Claims judged supported", result: rate(w.judge_supported), sample: sample(w.judge_supported?.n),
      how: "Share of all claims in the first-run memos that the judge model marked supported." },
    { measure: "Partially supported", result: rate(w.judge_partially), sample: sample(w.judge_partially?.n),
      how: "Share the judge marked partially supported: the passage covers only part of the claim." },
    { measure: "Unsupported (judge)", result: rate(w.judge_unsupported), sample: sample(w.judge_unsupported?.n),
      how: "Share the judge marked unsupported." },
    { measure: "Quoted figures in the cited passage", result: rate(accuracy?.quoted_figures_in_cited_passage),
      sample: sample(accuracy?.quoted_figures_in_cited_passage?.n),
      how: "Share of figures quoted from filing text that appear in the passage the claim cites." },
    { measure: "Numeric accuracy", result: rate(accuracy?.engine_figures), sample: sample(accuracy?.engine_figures?.n),
      how: "Share of computed figures in the memos that match the author's hand-checked golden values." },
    { measure: "Unsupported-claim rate (human labels)", result: rate(labels?.unsupported_rate), sample: sample(labels?.unsupported_rate?.n),
      how: "Share of claims in the blind sample that the author labelled unsupported." },
    { measure: "Citation precision (human labels)", result: rate(labels?.citation_precision), sample: sample(labels?.citation_precision?.n),
      how: "Share of citations in the blind sample that the author labelled correct." },
    { measure: "Raw numbers rejected per memo", result: toFixedPy(w.raw_numbers_rejected_per_memo, 1), sample: memos,
      how: "Typed digits in first drafts that the validator rejected, before any repair." },
    { measure: "Cost per memo", result: `$${toFixedPy(w.cost_total_per_memo, 3)}`, sample: memos,
      how: `Mean cost of drafting and judging one memo at list prices read on ${formatDate(r.prices_read_on)}.` },
    { measure: "Model time per memo", result: `${toFixedPy(w.model_seconds_per_memo, 0)}s`, sample: memos,
      how: "Mean total time spent waiting on model calls (drafting plus judging) per memo." },
    { measure: "Run-to-run spread", result: spread ? `${formatPct(spread.mean)} (${formatPct(spread.min)} to ${formatPct(spread.max)})` : "not measured",
      sample: `${spread?.n ?? 0} runs`, how: "Share judged supported in each of three drafts of the five golden-set memos: mean (lowest to highest)." },
  ];
}

function Block({ kicker, title, mono, rows }: { kicker: string; title: string; mono?: boolean; rows: Row[] }) {
  return (
    <section className="result-block">
      <div className="eyebrow">{kicker}</div>
      <h2 className={mono ? "result-title mono" : "result-title serif"}>{title}</h2>
      <div className="scroller ruled-top">
        <table className="data-table results-table">
          <thead><tr><th className="col-measure">Measure</th><th className="num col-result">Result</th><th className="num col-sample">Sample</th><th className="col-how">How this was measured</th></tr></thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.measure}>
                <td>{row.measure}</td>
                <td className={`num mono strong-500${row.result === NOT_MEASURED ? " muted" : ""}`}>{row.result}</td>
                <td className="num mono muted">{row.sample}</td>
                <td className="muted small-14 col-how">{row.how}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export function ResultsPage() {
  const evals = useJson<EvalsFile>("/data/evals.json");
  if (evals.state === "loading") return <main className="page page-narrow"><Loading what="the results" /></main>;
  if (evals.state === "error") return <main className="page page-narrow"><LoadError what="the results" /></main>;
  const r = evals.data.results as unknown as Results;
  const scorecardPending = r.scorecard_vs_agencies?.status?.startsWith("pending") ?? true;
  return (
    <main className="page page-narrow">
      <h1 className="page-title">Results</h1>
      <p className="muted lede-tight">Evaluation results generated {formatDate(r.generated_at)} by <code>{r.command}</code>. Every figure shows its
        sample size. No human evaluation was done, so measures that needed human labels or hand-checked values read
        “not measured”.</p>
      {Object.entries(r.writers ?? {}).map(([name, w]) => (
        <Block key={name} kicker="Drafting model" title={w.model} mono rows={writerRows(name, w, r)} />
      ))}
      {Object.entries(r.judge_calibration ?? {}).map(([judge, j]) => (
        <Block key={judge} kicker="Judge calibration" title={judge} mono rows={[
          { measure: "Agreement with human labels", result: rate(j.agreement), sample: sample(j.agreement?.n),
            how: "Share of sample claims where the judge's verdict matches the author's label." },
          { measure: "False-pass rate", result: rate(j.false_pass_rate), sample: sample(j.false_pass_rate?.n),
            how: "Of the sample claims the author labelled unsupported, the share the judge called supported." },
          { measure: "Claims re-judged", result: String(j.rows_judged), sample: sample(j.rows_judged),
            how: "Claims in the blind sample this judge re-judged for calibration." },
          { measure: "Calibration cost", result: `$${toFixedPy(j.cost_usd, 4)}`, sample: sample(j.rows_judged),
            how: "Cost of re-judging the sample at list prices." },
        ]} />
      ))}
      {Object.entries(r.seeded_errors ?? {}).map(([judge, kinds]) => (
        <section key={judge} className="result-block">
          <div className="eyebrow">Seeded errors</div>
          <h2 className="result-title mono">{judge}</h2>
          <div className="scroller ruled-top">
            <table className="data-table">
              <thead><tr><th>Error planted</th><th className="num">Sample</th><th className="num">Caught by code</th>
                <th className="num">Judged unsupported</th><th className="num">Judged partially</th><th className="num">Missed</th></tr></thead>
              <tbody>
                {Object.entries(kinds).map(([kind, k]) => (
                  <tr key={kind}><td>{kind.replaceAll("_", " ")}</td><td className="num mono muted">n = {k.n}</td><td className="num mono">{k.code}</td>
                    <td className="num mono">{k.judge_unsupported}</td><td className="num mono">{k.judge_partial}</td><td className="num mono">{k.missed}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="muted small-14">Claims the judge had marked supported were corrupted in five ways (a typed wrong figure, a swapped
            placeholder, a negation, a citation moved to another passage, and one moved with a real quote from it) and run through
            the same checks.</p>
        </section>
      ))}
      <Block kicker="Engine, retrieval and scorecard" title="Checks against hand-made answers" rows={[
        { measure: "Engine figures against golden values", result: rate(r.engine_accuracy?.accuracy), sample: sample(r.engine_accuracy?.accuracy?.n),
          how: "Share of engine figures that match the author's hand-checked values from the filings." },
        { measure: "Retrieval recall (top 8)", result: rate(r.retrieval_recall?.top8), sample: sample(r.retrieval_recall?.top8?.n),
          how: "Share of golden fact questions whose hand-located passage is among the top 8 search results." },
        { measure: "Scorecard against agency ratings", result: scorecardPending ? NOT_MEASURED : "see results.json",
          sample: scorecardPending ? "n = 0" : "–", how: "Rank correlation and IG / HY agreement with public agency ratings; none were entered." },
      ]} />
    </main>
  );
}
