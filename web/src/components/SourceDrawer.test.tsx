import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { MemoClaim, Metric, Passage } from "../contracts/types";
import { SourceDrawer } from "./SourceDrawer";

const metric: Metric = {
  metric_id: "debt_to_ebitda", period: "LTM", label: "Debt / EBITDA", value: 1.2083, unit: "x", status: "ok",
  formula: "total debt / EBITDA", notes: [],
  inputs: [{ label: "Interest expense", concept: "interest_expense", tag: "us-gaap:InterestExpenseDebt", fallback_rank: 3,
    value: 2_249_000_000, unit: "USD", period: "2025-02-01 to 2026-01-31", role: "fiscal year", sign: 1, form: "10-K",
    accession: "0000104169-26-000055", filed: "2026-03-13", url: "https://www.sec.gov/a" }],
};
const passage = (text: string): Passage => ({ text, section: "liquidity", form: "10-K", filed: "2026-03-13",
  period_end: "2026-01-31", accession: "0000104169-26-000055", url: "https://www.sec.gov/p", start: 0, end: text.length });
const claim: MemoClaim = {
  id: "liq-2", kind: "qualitative", verdict: "supported", judge_reason: "Both passages state it.", evidence_quote: "",
  checked_by: "judge", flags: [], segments: [{ t: "text", v: "The revolver is undrawn.", metric_id: null, chunk_id: null }],
  citations: [{ chunk_id: "A", quote: "no amounts were outstanding", check: "ok" },
    { chunk_id: "B", quote: "the facility expires", check: "quote_not_found" }],
};
const passages = { A: passage("At year-end no amounts were outstanding under it."), B: passage("Other text.") };

describe("SourceDrawer", () => {
  it("shows a metric's formula and each XBRL input with its fallback rank", () => {
    render(<SourceDrawer source={{ kind: "metric", key: "debt_to_ebitda:LTM", metric }} onClose={() => {}} />);
    expect(screen.getByRole("dialog", { name: "Source" })).toBeTruthy();
    expect(screen.getByText("total debt / EBITDA")).toBeTruthy();
    expect(screen.getByText("$2,249,000,000")).toBeTruthy();
    expect(screen.getByText("fallback, rank 3")).toBeTruthy();
    expect(screen.getByText(/Fallback tag used/)).toBeTruthy();
  });

  it("shows every cited passage, the quote marked, and whether each quote was found", () => {
    const { container } = render(
      <SourceDrawer source={{ kind: "claim", claim, passages, judgeModel: "judge/m" }} onClose={() => {}} />);
    expect(container.querySelector("mark")!.textContent).toBe("no amounts were outstanding");
    expect(screen.getByText(/Checked by judge\/m, independent of the drafting model/)).toBeTruthy();
    expect(screen.getByText("Quote found in passage: yes")).toBeTruthy();
    expect(screen.getByText("Quote found in passage: no (quote not found)")).toBeTruthy();
    expect(container.querySelectorAll("blockquote")).toHaveLength(2);
  });

  it("takes focus, keeps it inside, and closes on Escape", () => {
    const onClose = vi.fn();
    render(<SourceDrawer source={{ kind: "metric", key: "k", metric }} onClose={onClose} />);
    const close = screen.getByRole("button", { name: /Close/ });
    expect(document.activeElement).toBe(close);
    fireEvent.keyDown(document, { key: "Tab", shiftKey: true });
    expect(document.activeElement).not.toBe(close);
    fireEvent.keyDown(document, { key: "Escape" });
    expect(onClose).toHaveBeenCalled();
  });
});
