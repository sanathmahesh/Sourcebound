// Screen 5: evaluation results from /data/evals.json, every figure with its sample size. Figures that need
// my hand labels or hand-checked values show "pending" until those exist.
// evals.json "results" is an untyped object in the contract (EvalsFile.results: dict); the shapes below are
// what sourcebound/evals/report.py writes, read defensively.
import type { EvalsFile } from "../contracts/types";
import { useJson } from "../data";
import { formatRate, toFixedPy } from "../format";
import { Status } from "./Status";

type Rate = { value: number | null; n: number };
interface Writer {
  model: string; memos_run1: number; claims_per_memo: number; judge_supported: Rate; judge_partially: Rate;
  judge_unsupported: Rate; raw_numbers_rejected_per_memo: number; repairs_per_memo: number;
  cost_total_per_memo: number; model_seconds_per_memo: number;
  run_to_run_judge_supported?: { mean: number; min: number; max: number; n: number };
}
interface Results {
  generated_at: string; command: string; prices_read_on: string;
  writers: Record<string, Writer>;
  memo_numeric_accuracy: Record<string, { engine_figures: Rate; quoted_figures_in_cited_passage: Rate }>;
  engine_accuracy: { accuracy: Rate; coverage: Rate };
  retrieval_recall: { top8: Rate };
  labels: { labelled_rows: number; sheet_rows: number;
    per_writer: Record<string, { unsupported_rate: Rate; partially_rate: Rate; citation_precision: Rate }> };
  judge_calibration: Record<string, { rows_judged: number; cost_usd: number; agreement: Rate; false_pass_rate: Rate }>;
  seeded_errors: Record<string, Record<string, { n: number; code: number; judge_unsupported: number; judge_partial: number; missed: number }>>;
  scorecard_vs_agencies: Record<string, unknown>;
}

const pct = (v: number) => `${toFixedPy(v * 100, 1)}%`;

export function ResultsPage() {
  const evals = useJson<EvalsFile>("/data/evals.json");
  if (evals.state !== "ok") return <Status value={evals.state} message={evals.state === "error" ? evals.message : ""} />;
  const r = evals.data.results as unknown as Results;
  const writers = Object.entries(r.writers ?? {});
  return (
    <article>
      <h1>Results</h1>
      <p className="note">Generated {r.generated_at} by <code>{r.command}</code>. Costs at list prices read on {r.prices_read_on}.
        Every figure shows its sample size; "pending" means it needs hand labels or hand-checked values not yet entered.</p>

      <h2>Writer models</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Measure</th>{writers.map(([name]) => <th key={name}>{name}</th>)}</tr></thead>
          <tbody>
            <Row label="Memos (first run)" cells={writers.map(([, w]) => String(w.memos_run1))} />
            <Row label="Claims per memo" cells={writers.map(([, w]) => toFixedPy(w.claims_per_memo, 1))} />
            <Row label="Judge: supported" cells={writers.map(([, w]) => formatRate(w.judge_supported))} />
            <Row label="Judge: partly supported" cells={writers.map(([, w]) => formatRate(w.judge_partially))} />
            <Row label="Judge: unsupported" cells={writers.map(([, w]) => formatRate(w.judge_unsupported))} />
            <Row label="Quoted figures found in the cited passage" cells={writers.map(([n]) => formatRate(r.memo_numeric_accuracy?.[n]?.quoted_figures_in_cited_passage))} />
            <Row label="Engine figures matching hand-checked values" cells={writers.map(([n]) => formatRate(r.memo_numeric_accuracy?.[n]?.engine_figures))} />
            <Row label="Unsupported-claim rate (human labels)" cells={writers.map(([n]) => formatRate(r.labels?.per_writer?.[n]?.unsupported_rate))} />
            <Row label="Citation precision (human labels)" cells={writers.map(([n]) => formatRate(r.labels?.per_writer?.[n]?.citation_precision))} />
            <Row label="Raw numbers rejected per memo" cells={writers.map(([, w]) => toFixedPy(w.raw_numbers_rejected_per_memo, 1))} />
            <Row label="Cost per memo (USD, list price)" cells={writers.map(([, w]) => `$${toFixedPy(w.cost_total_per_memo, 3)}`)} />
            <Row label="Model time per memo" cells={writers.map(([, w]) => `${toFixedPy(w.model_seconds_per_memo, 0)} s`)} />
            <Row label="Run-to-run: judge supported, mean (min to max)" cells={writers.map(([, w]) => {
              const s = w.run_to_run_judge_supported;
              return s ? `${pct(s.mean)} (${pct(s.min)} to ${pct(s.max)}), ${s.n} runs` : "not measured";
            })} />
          </tbody>
        </table>
      </div>
      <p className="note">How measured: each writer drafted all 15 memos once, and the 5 golden-set memos twice more.
        Verdicts are from the judge model; human labels come from a blind 180-claim sample
        ({r.labels?.labelled_rows ?? 0} of {r.labels?.sheet_rows ?? 0} labelled so far).</p>

      <h2>Judge calibration</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Judge</th><th>Claims judged</th><th>Agreement with human labels</th><th>False-pass rate</th><th>Cost (USD)</th></tr></thead>
          <tbody>
            {Object.entries(r.judge_calibration ?? {}).map(([name, j]) => (
              <tr key={name}><td>{name}</td><td className="num">{j.rows_judged}</td><td>{formatRate(j.agreement)}</td>
                <td>{formatRate(j.false_pass_rate)}</td><td className="num">${toFixedPy(j.cost_usd, 4)}</td></tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="note">How measured: both candidate judges re-judged the 180-claim sample. Agreement is the share
        of claims where judge and human label match; the false-pass rate is, of the claims labelled unsupported by a
        human, the share the judge called supported.</p>

      <h2>Seeded errors</h2>
      {Object.entries(r.seeded_errors ?? {}).map(([judge, kinds]) => (
        <div key={judge} className="table-wrap">
          <h3>{judge}</h3>
          <table>
            <thead><tr><th>Error planted</th><th>n</th><th>Caught by code</th><th>Judge: unsupported</th><th>Judge: partly</th><th>Missed</th></tr></thead>
            <tbody>
              {Object.entries(kinds).map(([kind, k]) => (
                <tr key={kind}><td>{kind.replaceAll("_", " ")}</td><td className="num">{k.n}</td><td className="num">{k.code}</td>
                  <td className="num">{k.judge_unsupported}</td><td className="num">{k.judge_partial}</td><td className="num">{k.missed}</td></tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
      <p className="note">How measured: claims the judge had marked supported were corrupted in five ways (a typed
        wrong figure, a swapped placeholder, a negation, a citation moved to another passage, and one moved with a
        real quote from it) and run through the same checks.</p>

      <h2>Engine, retrieval and scorecard</h2>
      <ul>
        <li>Engine figures against hand-checked golden values: {formatRate(r.engine_accuracy?.accuracy)}</li>
        <li>Retrieval: golden fact questions whose hand-located passage is in the top 8 results: {formatRate(r.retrieval_recall?.top8)}</li>
        <li>Scorecard against agency ratings: {String(r.scorecard_vs_agencies?.status ?? "see results.json")}</li>
      </ul>
    </article>
  );
}

function Row({ label, cells }: { label: string; cells: string[] }) {
  return <tr><td>{label}</td>{cells.map((c, n) => <td key={n} className="num">{c}</td>)}</tr>;
}
