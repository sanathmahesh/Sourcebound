"""The eval memo plan: which memos to generate, skipping any already on disk."""

from sourcebound.evals.run_memos import Job, plan_jobs, short_name


def test_plan_covers_all_companies_once_and_golden_three_times(tmp_path):
    jobs = plan_jobs(["org/A", "org/B"], ["WMT", "MSFT"], golden=["WMT"], runs=3, root=tmp_path)
    assert len(jobs) == 2 * (2 + 2)  # per writer: 2 companies in run 1, plus WMT in runs 2 and 3
    assert Job("org/A", "WMT", 3, tmp_path / "A" / "run3") in jobs
    assert not any(j.ticker == "MSFT" and j.run > 1 for j in jobs)


def test_golden_first_so_labelling_can_start_early(tmp_path):
    jobs = plan_jobs(["org/A"], ["MSFT", "WMT"], golden=["WMT"], runs=2, root=tmp_path)
    assert (jobs[0].ticker, jobs[0].run) == ("WMT", 1)


def test_existing_memos_are_skipped(tmp_path):
    done = tmp_path / "A" / "run1" / "companies" / "WMT"
    done.mkdir(parents=True)
    (done / "memo.json").write_text("{}")
    jobs = plan_jobs(["org/A"], ["WMT"], golden=["WMT"], runs=1, root=tmp_path)
    assert jobs == []


def test_short_name():
    assert short_name("deepseek-ai/DeepSeek-V4.1-Flash-1017") == "DeepSeek-V4.1-Flash-1017"
