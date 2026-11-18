"""The concept resolver: fallback chains, the fallback log, optional components, restatements and LTM."""

from sourcebound.engine.concepts import parse_concepts
from sourcebound.engine.periods import Period, PeriodPart, Window
from sourcebound.engine.resolver import FactIndex, Resolver
from tests.helpers import d, fact

SPECS = parse_concepts(
    {
        "interest_expense": {
            "label": "Interest expense",
            "kind": "flow",
            "required": True,
            "chain": [
                {"tag": "InterestExpense"},
                {"tag": "InterestExpenseNonoperating"},
                {"tag": "InterestPaidNet", "flag": "proxy: cash interest paid"},
            ],
        },
        "operating_income": {
            "label": "Operating income",
            "kind": "flow",
            "required": True,
            "chain": [
                {"tag": "OperatingIncomeLoss"},
                {
                    "sum": [{"tag": "PretaxIncome"}, {"concept": "interest_expense"}],
                    "flag": "derived",
                },
            ],
        },
        "short_term_debt": {
            "label": "Short-term debt",
            "kind": "instant",
            "required": True,
            "chain": [
                {"tag": "DebtCurrent"},
                {"sum": [{"tag": "LongTermDebtCurrent"}, {"tag": "ShortTermBorrowings", "optional": True}]},
            ],
        },
        "total_debt": {
            "label": "Total debt",
            "kind": "instant",
            "required": True,
            "chain": [
                {"tag": "DebtLongtermAndShorttermCombinedAmount"},
                {"sum": [{"tag": "LongTermDebtNoncurrent"}, {"concept": "short_term_debt"}]},
            ],
        },
        "short_term_investments": {
            "label": "Short-term investments",
            "kind": "instant",
            "required": False,
            "chain": [{"tag": "ShortTermInvestments"}],
        },
    }
)

FY0 = Window(d("2023-01-01"), d("2023-12-31"))
FY1 = Window(d("2022-01-01"), d("2022-12-31"))
YTD = Window(d("2024-01-01"), d("2024-06-30"))
PRIOR_YTD = Window(d("2023-01-01"), d("2023-06-30"))

P_FY0 = Period("FY0", end=FY0.end, parts=(PeriodPart(+1, FY0, "FY0"),))
P_FY1 = Period("FY-1", end=FY1.end, parts=(PeriodPart(+1, FY1, "FY-1"),))
P_LTM = Period(
    "LTM",
    end=YTD.end,
    parts=(
        PeriodPart(+1, FY0, "FY0"),
        PeriodPart(+1, YTD, "current year-to-date"),
        PeriodPart(-1, PRIOR_YTD, "prior-year year-to-date"),
    ),
)


def flow(tag, value, window, **kw):
    return fact(tag, value, start=window.start.isoformat(), end=window.end.isoformat(), **kw)


def resolver(facts) -> Resolver:
    return Resolver(SPECS, FactIndex(facts), cik=1)


def test_rank_one_used_when_reported_and_nothing_logged():
    r = resolver([flow("InterestExpense", 10, FY0), flow("InterestExpenseNonoperating", 11, FY0)])
    got = r.resolve("interest_expense", P_FY0)
    assert (got.status, got.value, got.fallback_rank) == ("ok", 10, 1)
    assert got.inputs[0].tag == "InterestExpense"
    assert r.log == []


def test_falls_back_and_logs_why():
    r = resolver([flow("InterestExpenseNonoperating", 11, FY0)])
    got = r.resolve("interest_expense", P_FY0)
    assert (got.value, got.fallback_rank, got.candidate) == (11, 2, "InterestExpenseNonoperating")
    [entry] = r.log
    assert entry.kind == "fallback"
    assert entry.concept == "interest_expense" and entry.period == "FY0"
    assert "InterestExpense" in entry.message and "rank 2" in entry.message


def test_flag_is_carried_on_proxy_fallback():
    r = resolver([flow("InterestPaidNet", 9, FY0)])
    got = r.resolve("interest_expense", P_FY0)
    assert got.fallback_rank == 3
    assert got.flags == ["proxy: cash interest paid"]


def test_required_concept_with_no_fact_is_not_available():
    r = resolver([flow("InterestExpense", 10, FY1)])  # only a different year is reported
    got = r.resolve("interest_expense", P_FY0)
    assert got.status == "not_available"
    assert got.value is None
    assert [e.kind for e in r.log] == ["not_available"]


def test_optional_concept_with_no_fact_is_assumed_zero_and_logged():
    r = resolver([])
    got = r.resolve("short_term_investments", P_FY0)
    assert (got.status, got.value) == ("assumed_zero", 0)
    assert [e.kind for e in r.log] == ["assumed_zero"]


def test_optional_component_missing_counts_as_zero_and_is_logged():
    r = resolver([fact("LongTermDebtCurrent", 5, end="2023-12-31")])
    got = r.resolve("short_term_debt", P_FY0)
    assert (got.status, got.value, got.fallback_rank) == ("ok", 5, 2)
    assert any(e.kind == "assumed_zero" and "ShortTermBorrowings" in e.message for e in r.log)


def test_required_component_missing_fails_the_candidate():
    r = resolver([fact("ShortTermBorrowings", 3, end="2023-12-31")])  # no LongTermDebtCurrent
    got = r.resolve("short_term_debt", P_FY0)
    assert got.status == "not_available"


def test_sum_with_concept_component():
    r = resolver(
        [
            fact("LongTermDebtNoncurrent", 100, end="2023-12-31"),
            fact("LongTermDebtCurrent", 5, end="2023-12-31"),
            fact("ShortTermBorrowings", 3, end="2023-12-31"),
        ]
    )
    got = r.resolve("total_debt", P_FY0)
    assert (got.value, got.fallback_rank) == (108, 2)
    assert sorted(i.tag for i in got.inputs) == ["LongTermDebtCurrent", "LongTermDebtNoncurrent", "ShortTermBorrowings"]


def test_instant_uses_balance_sheet_date():
    r = resolver([fact("DebtLongtermAndShorttermCombinedAmount", 50, end="2022-12-31")])
    assert r.resolve("total_debt", P_FY1).value == 50
    assert r.resolve("total_debt", P_FY0).status == "not_available"


def test_derived_operating_income_carries_flag_and_all_inputs():
    r = resolver([flow("PretaxIncome", -20, FY0), flow("InterestExpense", 30, FY0)])
    got = r.resolve("operating_income", P_FY0)
    assert (got.value, got.fallback_rank) == (10, 2)
    assert "derived" in got.flags
    assert {i.tag for i in got.inputs} == {"PretaxIncome", "InterestExpense"}


def test_most_recently_filed_value_wins_and_restatement_is_logged():
    original = flow("InterestExpense", 10, FY1, accession="0000000000-23-000001", filed="2023-02-01")
    restated = flow("InterestExpense", 12, FY1, accession="0000000000-24-000001", filed="2024-02-01")
    r = resolver([restated, original])
    got = r.resolve("interest_expense", P_FY1)
    assert got.value == 12
    assert got.inputs[0].accession == "0000000000-24-000001"
    [entry] = r.log
    assert entry.kind == "restated"
    assert "0000000000-23-000001" in entry.message and "10" in entry.message


def test_same_value_in_several_filings_is_not_a_restatement():
    a = flow("InterestExpense", 10, FY1, accession="0000000000-23-000001", filed="2023-02-01")
    b = flow("InterestExpense", 10, FY1, accession="0000000000-24-000001", filed="2024-02-01")
    r = resolver([a, b])
    got = r.resolve("interest_expense", P_FY1)
    assert got.inputs[0].accession == "0000000000-24-000001"
    assert r.log == []


def test_ltm_arithmetic_and_lineage():
    r = resolver(
        [
            flow("InterestExpense", 100, FY0),
            flow("InterestExpense", 30, YTD, form="10-Q"),
            flow("InterestExpense", 20, PRIOR_YTD, form="10-Q"),
        ]
    )
    got = r.resolve("interest_expense", P_LTM)
    assert got.value == 110  # 100 + 30 - 20
    assert [(i.sign, i.value) for i in got.inputs] == [(+1, 100), (+1, 30), (-1, 20)]
    assert [i.role for i in got.inputs] == ["FY0", "current year-to-date", "prior-year year-to-date"]


def test_ltm_uses_one_tag_for_all_three_windows():
    """If rank 1 lacks one window, LTM falls back to a tag that has all three, never mixes tags."""
    r = resolver(
        [
            flow("InterestExpense", 100, FY0),
            flow("InterestExpense", 30, YTD),  # no prior-year YTD under rank 1
            flow("InterestExpenseNonoperating", 101, FY0),
            flow("InterestExpenseNonoperating", 31, YTD),
            flow("InterestExpenseNonoperating", 21, PRIOR_YTD),
        ]
    )
    got = r.resolve("interest_expense", P_LTM)
    assert (got.value, got.fallback_rank) == (111, 2)
    assert {i.tag for i in got.inputs} == {"InterestExpenseNonoperating"}


def test_resolving_twice_logs_once():
    r = resolver([flow("InterestExpenseNonoperating", 11, FY0)])
    r.resolve("interest_expense", P_FY0)
    r.resolve("interest_expense", P_FY0)
    assert len(r.log) == 1


def test_lineage_has_edgar_link():
    r = resolver([flow("InterestExpense", 10, FY0, accession="0000000000-24-000009")])
    source = r.resolve("interest_expense", P_FY0).inputs[0]
    assert source.url == "https://www.sec.gov/Archives/edgar/data/1/000000000024000009/0000000000-24-000009-index.htm"
    assert source.fallback_rank == 1
    assert source.concept == "interest_expense"


# ----- chain revision 2 (D19): sign-flipped components and optional concepts --------------------------

NET_SPECS = parse_concepts(
    {
        "interest_expense": {
            "label": "Interest expense",
            "kind": "flow",
            "required": True,
            "chain": [
                {"tag": "InterestExpense"},
                {"tag": "InterestIncomeExpenseNonoperatingNet", "negate": True, "flag": "net of interest income"},
            ],
        },
        "short_term_debt": {
            "label": "Short-term debt",
            "kind": "instant",
            "required": False,
            "chain": [{"tag": "DebtCurrent"}],
        },
    }
)


def test_negated_component_flips_sign_but_lineage_keeps_filed_value():
    r = Resolver(NET_SPECS, FactIndex([flow("InterestIncomeExpenseNonoperatingNet", -594, FY0)]), cik=1)
    got = r.resolve("interest_expense", P_FY0)
    assert (got.value, got.fallback_rank, got.candidate) == (594, 2, "−InterestIncomeExpenseNonoperatingNet")
    assert got.flags == ["net of interest income"]
    [source] = got.inputs
    assert (source.value, source.sign) == (-594, -1)  # the filed value, used with a minus sign


def test_negated_component_in_ltm():
    facts = [
        flow("InterestIncomeExpenseNonoperatingNet", -100, FY0),
        flow("InterestIncomeExpenseNonoperatingNet", -30, YTD),
        flow("InterestIncomeExpenseNonoperatingNet", -20, PRIOR_YTD),
    ]
    got = Resolver(NET_SPECS, FactIndex(facts), cik=1).resolve("interest_expense", P_LTM)
    assert got.value == 110  # -(-100 + -30 - -20)
    assert [i.sign for i in got.inputs] == [-1, -1, +1]


def test_optional_concept_assumed_zero_when_nothing_reported():
    r = Resolver(NET_SPECS, FactIndex([]), cik=1)
    got = r.resolve("short_term_debt", P_FY0)
    assert (got.status, got.value) == ("assumed_zero", 0)
    assert [(e.kind, e.subject) for e in r.log] == [("assumed_zero", "short_term_debt")]


def test_log_entries_carry_a_subject_for_grouping():
    r = resolver([flow("InterestExpenseNonoperating", 11, FY0)])
    r.resolve("interest_expense", P_FY0)
    assert r.log[0].subject == "InterestExpenseNonoperating"
