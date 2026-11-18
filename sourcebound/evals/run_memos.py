"""Generate the evaluation memos (PLAN.md 4.11 steps 1 and 5).

Run:  uv run python -m sourcebound.evals.run_memos                 (everything, resumable)
      uv run python -m sourcebound.evals.run_memos --golden-only   (golden set, run 1, for the labelling sheet)

Each writer model drafts a memo for all 15 companies (run 1), and the golden five twice more (runs 2 and 3)
to measure run-to-run spread. Verification uses the judge (SAIL_MODEL_JUDGE). Memos go to
evals/results/memos/<writer>/run<n>/; raw requests and responses to data/runs/. A memo already on disk is
skipped, so a rerun never pays twice. Several memos run at once (--workers); each memo's own calls stay in
order.
"""

from __future__ import annotations

import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv

from sourcebound.llm.prices import load_prices
from sourcebound.llm.provider import LlmError, LlmSettings, SailClient
from sourcebound.paths import CONFIG_DIR, ENV_FILE, PROJECT_ROOT
from sourcebound.pipeline.export import load_companies
from sourcebound.pipeline.generate_memo import PUBLISHED_DIR, generate_memo

EVAL_MEMOS = PROJECT_ROOT / "evals" / "results" / "memos"


@dataclass(frozen=True)
class Job:
    writer: str
    ticker: str
    run: int
    out_dir: Path


def short_name(model: str) -> str:
    return model.split("/")[-1]


def plan_jobs(writers: list[str], companies: list[str], golden: list[str], runs: int, root: Path = EVAL_MEMOS) -> list[Job]:
    """Golden run 1 first (the labelling sheet needs it), then the other companies, then golden repeats."""
    ordered = [(t, 1) for t in companies if t in golden] + [(t, 1) for t in companies if t not in golden]
    ordered += [(t, r) for r in range(2, runs + 1) for t in companies if t in golden]
    jobs = []
    for ticker, run in ordered:
        for writer in writers:
            out = root / short_name(writer) / f"run{run}"
            if not (out / "companies" / ticker / "memo.json").exists():
                jobs.append(Job(writer, ticker, run, out))
    return jobs


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate evaluation memos (resumable).")
    parser.add_argument("--golden-only", action="store_true", help="only the golden set, run 1")
    parser.add_argument("--runs", type=int, default=3, help="runs per writer for the golden set (default 3)")
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    client = SailClient(settings)
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    writers = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())["writers"]
    rows = load_companies()
    golden = [r["ticker"] for r in rows if r["golden"]]
    companies = golden if args.golden_only else [r["ticker"] for r in rows]
    jobs = plan_jobs(writers, companies, golden, 1 if args.golden_only else args.runs)
    print(f"{len(jobs)} memos to generate (judge {settings.judge_model}, {args.workers} at a time)", flush=True)

    def run(job: Job):
        memo, report = generate_memo(job.ticker, client, settings=settings, prices=prices, writer_model=job.writer,
                                     published_dir=job.out_dir, reports_dir=job.out_dir / "reports",
                                     metrics_dir=PUBLISHED_DIR)
        return memo, report

    started, spent = time.monotonic(), 0.0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run, job): job for job in jobs}
        for future in as_completed(futures):
            job = futures[future]
            try:
                memo, report = future.result()
            except (LlmError, ValueError) as exc:  # reported, never worked around; rerun to resume
                print(f"FAILED {short_name(job.writer)} {job.ticker} run{job.run}: {exc}", flush=True)
                continue
            cost = memo.run.drafting.cost_usd + memo.run.verification.cost_usd
            spent += cost
            s = report.summary
            print(f"{short_name(job.writer):26} {job.ticker:5} run{job.run}: {s.claims} claims, {s.supported}/"
                  f"{s.partially_supported}/{s.unsupported} S/P/U, ${cost:.3f}, "
                  f"{memo.run.drafting.seconds + memo.run.verification.seconds:.0f}s model time", flush=True)
    print(f"done: ${spent:.2f} at list price, {time.monotonic() - started:.0f}s wall time", flush=True)


if __name__ == "__main__":
    main()
