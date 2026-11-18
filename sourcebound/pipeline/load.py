"""Download (or read from the cache) everything the engine needs for one company, and analyse it."""

from dotenv import load_dotenv

from sourcebound.edgar.client import EdgarClient
from sourcebound.edgar.facts import companyfacts_url
from sourcebound.edgar.filings import submissions_url
from sourcebound.edgar.tickers import lookup_company
from sourcebound.engine.analysis import CompanyAnalysis, analyse_company
from sourcebound.engine.concepts import ConceptSpec
from sourcebound.paths import ENV_FILE


def make_client() -> EdgarClient:
    """An EDGAR client using EDGAR_USER_AGENT from the environment or .env. Refuses to run without it."""
    load_dotenv(ENV_FILE)
    return EdgarClient.from_env()


def load_and_analyse(client: EdgarClient, ticker: str, specs: dict[str, ConceptSpec]) -> CompanyAnalysis:
    """Three EDGAR requests at most (ticker list, filing list, company facts), each cached."""
    company = lookup_company(client, ticker)
    facts_url = companyfacts_url(company.cik)
    facts = client.get_json(facts_url)
    submissions = client.get_json(submissions_url(company.cik))
    return analyse_company(company.ticker, facts, submissions, specs, data_fetched_at=client.fetched_at(facts_url))
