"""Ticker to CIK lookup, from SEC's company_tickers.json (never from memory).

A CIK (Central Index Key) is the number EDGAR uses to identify a filer. URLs need it zero-padded to ten
digits, e.g. Walmart's CIK 104169 becomes CIK0000104169.
"""

from dataclasses import dataclass

from sourcebound.edgar.client import EdgarClient

TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"


@dataclass(frozen=True)
class CompanyId:
    ticker: str
    cik: int
    name: str


def cik10(cik: int) -> str:
    """The ten-digit zero-padded CIK used in data.sec.gov URLs."""
    return f"{int(cik):010d}"


def find_company(tickers_json: dict, ticker: str) -> CompanyId:
    """Find a ticker in the parsed company_tickers.json ({"0": {"cik_str", "ticker", "title"}, ...})."""
    wanted = ticker.upper()
    for row in tickers_json.values():
        if row["ticker"].upper() == wanted:
            return CompanyId(ticker=wanted, cik=int(row["cik_str"]), name=row["title"])
    raise KeyError(f"Ticker {wanted} is not in SEC company_tickers.json")


def lookup_company(client: EdgarClient, ticker: str) -> CompanyId:
    """Download (or read from cache) company_tickers.json and find the ticker."""
    return find_company(client.get_json(TICKERS_URL), ticker)
