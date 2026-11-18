"""Per-company overrides from config/overrides.yaml.

The plan allows a company to be treated differently only through this file, each override with a written
reason and the author's approval, and each shown on that company's reviewer checklist. The only kind so far
is "cik": use a given CIK instead of the one SEC's ticker file returns (see the XOM entry).
"""

from dataclasses import dataclass
from pathlib import Path

import yaml

from sourcebound.edgar.tickers import CompanyId, find_company

KINDS = {"cik"}


@dataclass(frozen=True)
class Override:
    ticker: str
    kind: str
    reason: str
    approved_on: str
    cik: int | None = None


def load_overrides(path: Path) -> list[Override]:
    return parse_overrides(yaml.safe_load(path.read_text()) or {})


def parse_overrides(raw: dict) -> list[Override]:
    """Build overrides, refusing any without a known kind, a reason and an approval date."""
    result = []
    for entry in raw.get("overrides") or []:
        ticker = entry.get("ticker", "?")
        if entry.get("kind") not in KINDS:
            raise ValueError(f"override for {ticker}: kind must be one of {sorted(KINDS)}")
        if not str(entry.get("reason", "")).strip():
            raise ValueError(f"override for {ticker}: a written reason is required")
        if not str(entry.get("approved_on", "")).strip():
            raise ValueError(f"override for {ticker}: the author's approval date is required")
        result.append(
            Override(
                ticker=ticker.upper(),
                kind=entry["kind"],
                reason=" ".join(str(entry["reason"]).split()),
                approved_on=str(entry["approved_on"]),
                cik=int(entry["cik"]) if entry.get("cik") is not None else None,
            )
        )
    return result


def overrides_for(overrides: list[Override], ticker: str) -> list[Override]:
    return [o for o in overrides if o.ticker == ticker.upper()]


def company_for(ticker: str, tickers_json: dict, overrides: list[Override]) -> CompanyId:
    """The company to analyse: SEC's ticker lookup, unless a cik override says otherwise."""
    company = find_company(tickers_json, ticker)
    for o in overrides_for(overrides, ticker):
        if o.kind == "cik":
            company = CompanyId(ticker=company.ticker, cik=o.cik, name=company.name)
    return company
