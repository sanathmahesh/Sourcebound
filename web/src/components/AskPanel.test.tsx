import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { AskResponse } from "../contracts/types";
import { AskPanel } from "./AskPanel";

const answer: AskResponse = {
  schema_version: "1", ticker: "WMT", question: "How levered?", status: "ok", model: "m", judge_model: "j",
  seconds: 12.3, data_to: "2026-07-31", disclaimer: "d",
  claims: [{ id: "ask-1", kind: "quantitative", verdict: "supported", judge_reason: "ok", evidence_quote: "",
    checked_by: "judge", flags: [], citations: [],
    segments: [{ t: "text", v: "Leverage is low.", metric_id: null, chunk_id: null }] }],
  removed: [{ text: "Leverage is 9.9x.", verdict: "unsupported", reason: "unsupported: number check failed" }],
  metrics: {}, passages: {},
  trace: [{ round: 1, tool: "get_metric", arguments: { metric_id: "debt_to_ebitda", period: "LTM" }, result: "debt_to_ebitda:LTM = 1.21x" }],
};

function reply(status: number, body: unknown) {
  return vi.fn().mockResolvedValue({ ok: status === 200, status, json: async () => body });
}

function ask(question: string) {
  fireEvent.change(screen.getByRole("textbox", { name: "Question" }), { target: { value: question } });
  fireEvent.click(screen.getByRole("button", { name: "Ask" }));
}

afterEach(() => { cleanup(); vi.unstubAllGlobals(); });

describe("AskPanel", () => {
  it("allows at most 500 characters and no empty question", () => {
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    expect((screen.getByRole("button", { name: "Ask" }) as HTMLButtonElement).disabled).toBe(true);
    expect((screen.getByRole("textbox", { name: "Question" }) as HTMLInputElement).maxLength).toBe(500);
  });

  it("shows kept claims, the lookups and the removed claims with reasons", async () => {
    const fetch = reply(200, answer);
    vi.stubGlobal("fetch", fetch);
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    ask("How levered?");
    expect(await screen.findByText("Leverage is low.")).toBeTruthy();
    expect(screen.getByText("Q. How levered?")).toBeTruthy();
    const trace = screen.getByRole("button", { name: /What was looked up \(1\)/ });
    expect(trace.getAttribute("aria-expanded")).toBe("false");
    fireEvent.click(trace);
    expect(screen.getByText(/get_metric/)).toBeTruthy();
    expect(screen.getByText(/Removed: could not be verified \(1\)/)).toBeTruthy();
    expect(screen.getByText(/number check failed/)).toBeTruthy();
    expect(JSON.parse(fetch.mock.calls[0][1].body)).toEqual({ ticker: "WMT", question: "How levered?" });
  });

  it.each([
    [429, { detail: "busy" }, "! Rate limited."],
    [503, { detail: "down" }, "✕ Model provider unavailable."],
    [400, { detail: "Questions are limited to 500 characters." }, "Questions are limited to 500 characters."],
  ])("says plainly what happened on HTTP %i", async (status, body, text) => {
    vi.stubGlobal("fetch", reply(status, body));
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    ask("Leverage?");
    expect(await screen.findByText(text)).toBeTruthy();
  });

  it("says when a question is out of scope", async () => {
    vi.stubGlobal("fetch", reply(200, { ...answer, status: "out_of_scope", claims: [], removed: [], trace: [] }));
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    ask("Write a poem");
    expect(await screen.findByText("○ Out of scope.")).toBeTruthy();
  });
});
