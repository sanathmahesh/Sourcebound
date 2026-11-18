"""Capture trimmed test fixtures from real EDGAR responses already in the cache (data/raw/).

Run:  uv run python tests/fixtures/edgar/capture_fixtures.py WMT VZ GT

What is kept, unmodified:
- company facts: only the us-gaap tags named in config/concepts.yaml (plus a few used in tests), only facts
  whose period ends on or after 2021-01-01. Every kept fact keeps its accession number (accn), form and
  filing date exactly as EDGAR returned them.
- submissions: top-level identity fields, and the 10-K / 10-Q rows of filings.recent.
- company_tickers: the rows for the requested tickers.
Each file records the source URL and the time the cached response was fetched.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "data" / "raw"
OUT = Path(__file__).resolve().parent
MIN_END = "2021-01-01"
EXTRA_TAGS = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"]


def chain_tags() -> list[str]:
    """Every us-gaap tag mentioned in config/concepts.yaml."""
    specs = yaml.safe_load((ROOT / "config" / "concepts.yaml").read_text())
    tags: list[str] = []
    for spec in specs.values():
        for entry in spec["chain"]:
            components = entry["sum"] if "sum" in entry else [entry]
            tags += [c["tag"] for c in components if "tag" in c]
    return sorted(set(tags + EXTRA_TAGS))


def fetched_at(path: Path) -> str:
    return json.loads(path.with_name(path.name + ".meta.json").read_text())["fetched_at"]


def capture(ticker: str, tickers: dict) -> None:
    row = next(r for r in tickers.values() if r["ticker"] == ticker)
    cik10 = f"{int(row['cik_str']):010d}"

    facts_path = RAW / "data.sec.gov/api/xbrl/companyfacts" / f"CIK{cik10}.json"
    facts = json.loads(facts_path.read_text())
    us_gaap = facts["facts"]["us-gaap"]
    kept = {}
    for tag in chain_tags():
        if tag not in us_gaap:
            continue
        units = {
            unit: [f for f in rows if f["end"] >= MIN_END]
            for unit, rows in us_gaap[tag]["units"].items()
        }
        kept[tag] = {**{k: v for k, v in us_gaap[tag].items() if k != "units"}, "units": units}
    trimmed_facts = {
        "_capture": {
            "source_url": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json",
            "fetched_at": fetched_at(facts_path),
            "trimmed": f"us-gaap tags in config/concepts.yaml only; facts ending on or after {MIN_END}",
        },
        "cik": facts["cik"],
        "entityName": facts["entityName"],
        "facts": {"us-gaap": kept},
    }
    (OUT / f"companyfacts_{ticker}.json").write_text(json.dumps(trimmed_facts, indent=1))

    subs_path = RAW / "data.sec.gov/submissions" / f"CIK{cik10}.json"
    subs = json.loads(subs_path.read_text())
    recent = subs["filings"]["recent"]
    keep_rows = [i for i, form in enumerate(recent["form"]) if form in ("10-K", "10-Q", "10-K/A", "10-Q/A")]
    columns = ["accessionNumber", "filingDate", "reportDate", "form", "primaryDocument"]
    trimmed_subs = {
        "_capture": {
            "source_url": f"https://data.sec.gov/submissions/CIK{cik10}.json",
            "fetched_at": fetched_at(subs_path),
            "trimmed": "identity fields and the 10-K/10-Q rows of filings.recent",
        },
        **{k: subs[k] for k in ("cik", "name", "tickers", "sic", "sicDescription", "fiscalYearEnd")},
        "filings": {"recent": {c: [recent[c][i] for i in keep_rows] for c in columns}},
    }
    (OUT / f"submissions_{ticker}.json").write_text(json.dumps(trimmed_subs, indent=1))
    print(ticker, cik10, len(kept), "tags,", len(keep_rows), "periodic filings")


def main(tickers_wanted: list[str]) -> None:
    tickers_path = RAW / "www.sec.gov/files/company_tickers.json"
    tickers = json.loads(tickers_path.read_text())
    subset = {k: v for k, v in tickers.items() if v["ticker"] in tickers_wanted}
    (OUT / "company_tickers_subset.json").write_text(
        json.dumps(
            {
                "_capture": {
                    "source_url": "https://www.sec.gov/files/company_tickers.json",
                    "fetched_at": fetched_at(tickers_path),
                    "trimmed": "rows for " + ", ".join(tickers_wanted),
                },
                "rows": subset,
            },
            indent=1,
        )
    )
    for ticker in tickers_wanted:
        capture(ticker, tickers)


if __name__ == "__main__":
    main(sys.argv[1:] or ["WMT", "VZ", "GT"])
