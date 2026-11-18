import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { MemoClaim, Metric, Passage } from "../contracts/types";
import { ClaimText } from "./ClaimText";

const metric: Metric = { metric_id: "net_leverage", period: "LTM", label: "Net leverage", value: 0.96, unit: "x",
  status: "ok", formula: "(debt - cash) / EBITDA", notes: [], inputs: [] };
const passage: Passage = { text: "We have a $15.0 billion revolving credit facility.", section: "liquidity", form: "10-K",
  filed: "2026-03-13", period_end: "2026-01-31", accession: "0000104169-26-000055", url: "https://www.sec.gov/x", start: 0, end: 50 };
const claim: MemoClaim = {
  id: "liq-1", kind: "qualitative", verdict: "partially_supported", judge_reason: "Size stated; expiry not.",
  evidence_quote: "", checked_by: "judge", flags: [],
  segments: [{ t: "text", v: "Net leverage is ", metric_id: null, chunk_id: null },
    { t: "metric", v: "0.96x", metric_id: "net_leverage:LTM", chunk_id: null },
    { t: "text", v: " and the revolver is ", metric_id: null, chunk_id: null },
    { t: "quoted", v: "$15.0 billion", metric_id: null, chunk_id: "WMT-1" }],
  citations: [{ chunk_id: "WMT-1", quote: "a $15.0 billion revolving credit facility", check: "ok" }],
};

describe("ClaimText", () => {
  it("shows the two kinds of figure differently, in words as well as style", () => {
    render(<ClaimText claim={claim} metrics={{ "net_leverage:LTM": metric }} passages={{ "WMT-1": passage }} onOpen={() => {}} />);
    expect(screen.getByRole("button", { name: /0\.96x.*computed from XBRL/ })).toBeTruthy();
    expect(screen.getByRole("button", { name: /\$15\.0 billion.*quoted from the filing/ })).toBeTruthy();
    expect(screen.getByText("Partly supported")).toBeTruthy();
  });

  it("opens the metric's lineage or the cited passage", () => {
    const onOpen = vi.fn();
    render(<ClaimText claim={claim} metrics={{ "net_leverage:LTM": metric }} passages={{ "WMT-1": passage }} onOpen={onOpen} />);
    fireEvent.click(screen.getByRole("button", { name: /0\.96x/ }));
    expect(onOpen).toHaveBeenLastCalledWith({ kind: "metric", key: "net_leverage:LTM", metric });
    fireEvent.click(screen.getByRole("button", { name: /citation 1/ }));
    expect(onOpen).toHaveBeenLastCalledWith(expect.objectContaining({ kind: "passage", chunkId: "WMT-1", passage,
      quote: "a $15.0 billion revolving credit facility", verdict: "partially_supported" }));
  });
});
