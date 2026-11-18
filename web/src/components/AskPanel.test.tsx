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

afterEach(() => { cleanup(); vi.unstubAllGlobals(); });

describe("AskPanel", () => {
  it("allows at most 500 characters and no empty question", () => {
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    expect((screen.getByRole("button", { name: "Ask" }) as HTMLButtonElement).disabled).toBe(true);
    expect((screen.getByRole("textbox") as HTMLTextAreaElement).maxLength).toBe(500);
    expect(screen.getByText("0 / 500")).toBeTruthy();
  });

  it("shows kept claims, the lookups and the removed claims with reasons", async () => {
    const fetch = reply(200, answer);
    vi.stubGlobal("fetch", fetch);
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    fireEvent.change(screen.getByRole("textbox"), { target: { value: "How levered?" } });
    fireEvent.click(screen.getByRole("button", { name: "Ask" }));
    expect(await screen.findByText("Leverage is low.")).toBeTruthy();
    expect(screen.getByText(/What was looked up \(1\)/)).toBeTruthy();
    expect(screen.getByText(/Removed: could not be verified \(1\)/)).toBeTruthy();
    expect(screen.getByText(/number check failed/)).toBeTruthy();
    expect(JSON.parse(fetch.mock.calls[0][1].body)).toEqual({ ticker: "WMT", question: "How levered?" });
  });

  it("says plainly when the service is busy", async () => {
    vi.stubGlobal("fetch", reply(429, { detail: "The model service is busy. Try again in a few minutes." }));
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    fireEvent.change(screen.getByRole("textbox"), { target: { value: "Leverage?" } });
    fireEvent.click(screen.getByRole("button", { name: "Ask" }));
    expect(await screen.findByText(/try again in a few minutes/i)).toBeTruthy();
  });

  it("says when a question is out of scope", async () => {
    vi.stubGlobal("fetch", reply(200, { ...answer, status: "out_of_scope", claims: [], removed: [], trace: [] }));
    render(<AskPanel ticker="WMT" onOpen={() => {}} />);
    fireEvent.change(screen.getByRole("textbox"), { target: { value: "Write a poem" } });
    fireEvent.click(screen.getByRole("button", { name: "Ask" }));
    expect(await screen.findByText(/outside what this tool answers/)).toBeTruthy();
  });
});
