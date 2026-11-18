"""Layers (a) and (b) deterministic checks: placeholders, raw digits, quoted figures, quotes. Plus seeded errors."""

import pytest

from sourcebound.memo.render import TableEntry, render_claim
from sourcebound.verify.numbers import check_claim_numbers
from sourcebound.verify.quotes import check_quote, normalise

TABLE = {
    "net_leverage:LTM": TableEntry("net_leverage:LTM", "Net leverage, LTM", "0.96x"),
    "total_debt:FY0": TableEntry("total_debt:FY0", "Total debt, FY0", "$51.5 billion"),
}
PERIODS = {"LTM": "the twelve months to 31 July 2026", "FY0": "the fiscal year ended 31 January 2026"}
PASSAGE = ("In April 2026, the Company renewed and extended its existing 364-day revolving credit facility of "
           "$10.0 billion as well as its five-year credit facility of $5.0 billion. In total, the Company had "
           "committed lines of credit in the U.S. of $15.0 billion, all undrawn.")
CITED = {"WMT-1": PASSAGE}


# ----- numbers ----------------------------------------------------------------------------------------


def test_placeholders_render_to_engine_values():
    rendered = render_claim("Net leverage was {{m:net_leverage:LTM}} for {{p:LTM}}.", CITED, TABLE, PERIODS)
    assert rendered.problems == []
    assert rendered.text == "Net leverage was 0.96x for the twelve months to 31 July 2026."
    metric = [s for s in rendered.segments if s.t == "metric"]
    assert [(s.v, s.metric_id) for s in metric] == [("0.96x", "net_leverage:LTM")]


def test_raw_digits_are_rejected():
    problems = check_claim_numbers("Net leverage was 0.96x.", CITED, TABLE, PERIODS)
    assert problems == ["number not from a placeholder or a cited passage: 0.96"]


def test_quoted_figure_present_in_the_cited_passage_is_accepted():
    text = "The company has $15.0 billion of committed credit lines, all undrawn."
    assert check_claim_numbers(text, CITED, TABLE, PERIODS) == []
    rendered = render_claim(text, CITED, TABLE, PERIODS)
    [quoted] = [s for s in rendered.segments if s.t == "quoted"]
    assert (quoted.v, quoted.chunk_id) == ("15.0", "WMT-1")


def test_figure_in_an_uncited_passage_is_rejected():
    assert check_claim_numbers("Lines total $15.0 billion.", {}, TABLE, PERIODS) == [
        "number not from a placeholder or a cited passage: 15.0"
    ]


def test_unknown_placeholders_are_rejected():
    problems = check_claim_numbers("Leverage was {{m:made_up_ratio:LTM}} in {{p:FY9}}.", CITED, TABLE, PERIODS)
    assert problems == ["unknown metric placeholder: made_up_ratio:LTM", "unknown period placeholder: FY9"]


def test_segments_rebuild_the_rendered_text():
    rendered = render_claim("Debt was {{m:total_debt:FY0}}; lines of $15.0 billion are undrawn.", CITED, TABLE, PERIODS)
    assert "".join(s.v for s in rendered.segments) == rendered.text
    assert [s.t for s in rendered.segments] == ["text", "metric", "text", "quoted", "text"]


# ----- quotes -----------------------------------------------------------------------------------------


def test_quote_normalisation_ignores_case_whitespace_and_curly_punctuation():
    assert normalise("  The Company’s   “five-year”  facility ") == "the company's \"five-year\" facility"
    assert check_quote("the company had  committed lines of credit", PASSAGE) == "ok"


@pytest.mark.parametrize(
    "quote,passage,expected",
    [
        ("committed lines of credit in Canada", PASSAGE, "quote_not_found"),
        ("credit facility", PASSAGE, "quote_too_short"),
        ("committed lines of credit", None, "chunk_not_found"),
    ],
)
def test_quote_failures(quote, passage, expected):
    assert check_quote(quote, passage) == expected


# ----- seeded errors: a corrupted claim is caught before any model sees it ----------------------------


GOOD_TEXT = "Walmart has {{m:total_debt:FY0}} of debt and $15.0 billion of undrawn committed credit lines."
GOOD_QUOTE = "committed lines of credit in the U.S. of $15.0 billion"


def test_good_claim_passes_both_layers():
    assert check_claim_numbers(GOOD_TEXT, CITED, TABLE, PERIODS) == []
    assert check_quote(GOOD_QUOTE, CITED["WMT-1"]) == "ok"


@pytest.mark.parametrize(
    "corrupt",
    [
        GOOD_TEXT.replace("{{m:total_debt:FY0}}", "$51.5 billion"),  # number copied instead of placeholder
        GOOD_TEXT.replace("$15.0 billion", "$16.0 billion"),  # quoted figure changed
        GOOD_TEXT.replace("{{m:total_debt:FY0}}", "{{m:total_debt:FY9}}"),  # placeholder for a missing period
    ],
)
def test_corrupted_numbers_are_caught(corrupt):
    assert check_claim_numbers(corrupt, CITED, TABLE, PERIODS)


@pytest.mark.parametrize(
    "quote,chunk",
    [
        ("committed lines of credit in the U.S. of $16.0 billion", "WMT-1"),  # altered quote
        ("the Company has no committed lines of credit", "WMT-1"),  # negated quote
        (GOOD_QUOTE, "WMT-999"),  # citation swapped to a passage that was not given
    ],
)
def test_corrupted_citations_are_caught(quote, chunk):
    assert check_quote(quote, CITED.get(chunk)) != "ok"
