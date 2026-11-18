"""Judge calibration (PLAN.md 4.11 step 3): run each judge candidate over the labelling-sheet claims.

Run:  uv run python -m sourcebound.evals.run_judges

Each claim is rebuilt from the saved draft (no new drafting) and verified with each candidate in
config/models.yaml (judge_candidates). Results go to evals/results/judges/<judge>.json, keyed by sheet row.
Resumable: rows already judged are skipped. Agreement with the author's labels is computed by the report.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor

import yaml
from dotenv import load_dotenv

from sourcebound.contracts import Memo
from sourcebound.evals.make_label_sheet import KEY
from sourcebound.evals.replay import MemoReplay
from sourcebound.evals.run_memos import short_name
from sourcebound.llm.prices import call_cost, load_prices
from sourcebound.llm.provider import LlmError, LlmSettings, SailClient
from sourcebound.paths import CONFIG_DIR, ENV_FILE, PROJECT_ROOT
from sourcebound.verify.claims import verify_claim

JUDGE_DIR = PROJECT_ROOT / "evals" / "results" / "judges"


def main() -> None:
    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    client = SailClient(settings)
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    config = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())
    key = json.loads(KEY.read_text())
    replays: dict[str, MemoReplay] = {}
    for row in key.values():
        memo_path = PROJECT_ROOT / row["run"] / "companies" / row["ticker"] / "memo.json"
        if str(memo_path) not in replays:
            replays[str(memo_path)] = MemoReplay(Memo.model_validate_json(memo_path.read_text()))
        row["_memo"] = str(memo_path)
    JUDGE_DIR.mkdir(parents=True, exist_ok=True)
    for judge in config["judge_candidates"]:
        out = JUDGE_DIR / f"{short_name(judge)}.json"
        done = json.loads(out.read_text())["rows"] if out.exists() else {}
        todo = [(rid, row) for rid, row in key.items() if rid not in done]

        def check(item):
            rid, row = item
            replay = replays[row["_memo"]]
            claim, calls = verify_claim(row["claim_id"], replay.claim(row["claim_id"]), replay.context(row["section"]),
                                        client, model=judge, reasoning_effort=config["reasoning_effort"]["judge"],
                                        max_tokens=config["max_completion_tokens"]["judge"])
            return rid, {"verdict": claim.verdict, "checked_by": claim.checked_by, "reason": claim.judge_reason,
                         "cost_usd": sum(call_cost(prices, judge, c.usage) for c in calls),
                         "seconds": sum(c.seconds for c in calls)}

        with ThreadPoolExecutor(max_workers=6) as pool:
            for future in [pool.submit(check, item) for item in todo]:
                try:
                    rid, result = future.result()
                    done[rid] = result
                except LlmError as exc:
                    print(f"{short_name(judge)}: a row failed ({exc}); rerun to resume")
        out.write_text(json.dumps({"judge": judge, "rows": dict(sorted(done.items()))}, indent=1))
        cost = sum(r["cost_usd"] for r in done.values())
        print(f"{short_name(judge)}: {len(done)}/{len(key)} rows judged, ${cost:.3f} -> {out.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
