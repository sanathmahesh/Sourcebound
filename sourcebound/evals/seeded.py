"""Seeded-error test (PLAN.md 4.11 step 4): corrupt known-good claims and see which layer catches them.

Run:  uv run python -m sourcebound.evals.seeded     (needs golden run-1 memos; calls each judge candidate)

Five corruptions of a claim the judge marked supported:
- raw_number: an engine placeholder replaced by a wrong typed figure   -> the number check should catch it
- wrong_placeholder: a placeholder swapped for another valid one with a different value -> only the judge
- negation: "It is not the case that ..."                                -> only the judge
- citation_swap: the citation moved to another passage, quote unchanged -> the quote check
- citation_swap_with_quote: another passage and a real quote from it    -> the judge (or the number check,
  if the claim quoted a figure from the original passage)
Results go to evals/results/seeded/<judge>.json; nothing is published.
"""

from __future__ import annotations

import json
import random
from concurrent.futures import ThreadPoolExecutor

import yaml
from dotenv import load_dotenv

from sourcebound.contracts import CompanyMetrics, Memo
from sourcebound.evals.replay import MemoReplay
from sourcebound.evals.run_memos import EVAL_MEMOS, short_name
from sourcebound.llm.prices import call_cost, load_prices
from sourcebound.llm.provider import LlmSettings, SailClient
from sourcebound.llm.schemas import DraftCitation, DraftClaim
from sourcebound.memo.draft import SectionContext
from sourcebound.paths import CONFIG_DIR, ENV_FILE, PROJECT_ROOT
from sourcebound.pipeline.export import load_companies
from sourcebound.verify.claims import verify_claim
from sourcebound.verify.numbers import NUMBER, PLACEHOLDER

SEEDED_DIR = PROJECT_ROOT / "evals" / "results" / "seeded"
BASE_CLAIMS_PER_MEMO = 4
SEED = 20261118


def negate(text: str) -> str:
    return "It is not the case that " + text[:1].lower() + text[1:]


def _wrong_figure(display: str) -> str:
    """'1.21x' -> '2.82x': the first number scaled by 1.5 and moved by 1, keeping its decimals."""
    match = NUMBER.search(display)
    if not match:
        return "7.77"
    token = match.group().replace(",", "")
    decimals = len(token.split(".")[1]) if "." in token else 0
    wrong = f"{float(token) * 1.5 + 1:,.{decimals}f}"
    return display[:match.start()] + wrong + display[match.end():]


def corrupt(draft: DraftClaim, ctx: SectionContext, cm: CompanyMetrics) -> list[tuple[str, DraftClaim]]:
    out = [("negation", draft.model_copy(update={"text": negate(draft.text)}))]
    placeholder = next((m for m in PLACEHOLDER.finditer(draft.text) if m.group(1) == "m"), None)
    if placeholder:
        key = f"{placeholder.group(2)}:{placeholder.group(3)}"
        before, after = draft.text[:placeholder.start()], draft.text[placeholder.end():]
        out.append(("raw_number", draft.model_copy(update={"text": before + _wrong_figure(ctx.table[key].display) + after})))
        unit = cm.metrics[key].unit if key in cm.metrics else None
        period = key.rsplit(":", 1)[-1]
        swap = next((k for k in sorted(cm.metrics) if k.endswith(f":{period}") and k != key and cm.metrics[k].unit == unit
                     and k in ctx.table and ctx.table[k].display != ctx.table[key].display), None)
        if swap:
            out.append(("wrong_placeholder", draft.model_copy(update={"text": before + "{{m:" + swap + "}}" + after})))
    if draft.citations:
        cited = {c.chunk_id for c in draft.citations}
        other = next((p for p in ctx.passages if p.id not in cited), None)
        if other:
            first = draft.citations[0]
            out.append(("citation_swap", draft.model_copy(update={
                "citations": [DraftCitation(chunk_id=other.id, quote=first.quote)] + draft.citations[1:]})))
            words = other.text.split()[:10]
            out.append(("citation_swap_with_quote", draft.model_copy(update={
                "citations": [DraftCitation(chunk_id=other.id, quote=" ".join(words))]})))
    return out


def base_claims() -> list[tuple[Memo, MemoReplay, str]]:
    """Up to four judge-supported claims per golden run-1 memo, drawn with a fixed seed."""
    rng = random.Random(SEED)
    golden = [r["ticker"] for r in load_companies() if r["golden"]]
    writers = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())["writers"]
    chosen = []
    for writer in writers:
        for ticker in golden:
            path = EVAL_MEMOS / short_name(writer) / "run1" / "companies" / ticker / "memo.json"
            if not path.exists():
                continue
            memo = Memo.model_validate_json(path.read_text())
            replay = MemoReplay(memo)
            supported = [c.id for s in memo.sections for c in s.claims if c.verdict == "supported"]
            chosen += [(memo, replay, cid) for cid in rng.sample(supported, min(BASE_CLAIMS_PER_MEMO, len(supported)))]
    return chosen


def main() -> None:
    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    client = SailClient(settings)
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    config = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())
    cases = []
    for memo, replay, claim_id in base_claims():
        draft = replay.claim(claim_id)
        ctx = replay.context(claim_id.rsplit("-", 1)[0])
        cases += [(memo, claim_id, kind, bad, ctx) for kind, bad in corrupt(draft, ctx, replay.cm)]
    SEEDED_DIR.mkdir(parents=True, exist_ok=True)
    for judge in config["judge_candidates"]:
        def check(case):
            memo, claim_id, kind, bad, ctx = case
            claim, calls = verify_claim(claim_id, bad, ctx, client, model=judge,
                                        reasoning_effort=config["reasoning_effort"]["judge"],
                                        max_tokens=config["max_completion_tokens"]["judge"])
            return {"writer": memo.model, "ticker": memo.ticker, "claim_id": claim_id, "corruption": kind,
                    "verdict": claim.verdict, "checked_by": claim.checked_by, "reason": claim.judge_reason,
                    "cost_usd": sum(call_cost(prices, judge, c.usage) for c in calls)}
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(check, cases))
        out = SEEDED_DIR / f"{short_name(judge)}.json"
        out.write_text(json.dumps({"judge": judge, "seed": SEED, "results": results}, indent=1))
        caught = sum(r["verdict"] != "supported" for r in results)
        print(f"{short_name(judge)}: {caught}/{len(results)} corrupted claims flagged; "
              f"${sum(r['cost_usd'] for r in results):.3f}; -> {out.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
