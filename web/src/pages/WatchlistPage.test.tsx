import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fireEvent, render, screen, within } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { Watchlist } from "../contracts/types";
import { WatchlistPage } from "./WatchlistPage";

// The real published file, so no figure is typed into this test.
const watchlist: Watchlist = JSON.parse(readFileSync(resolve(process.cwd(), "../data/published/watchlist.json"), "utf8"));

afterEach(() => vi.unstubAllGlobals());

describe("WatchlistPage on the published watchlist", () => {
  it("shows each company's change since the prior year-end, marking ratios a flag fired on", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, status: 200, json: async () => watchlist }));
    render(<WatchlistPage />);
    await screen.findByRole("heading", { name: "Watchlist" });
    for (const item of watchlist.items) {
      const row = screen.getByTestId(`watch-${item.ticker}`);
      for (const change of item.changes) {
        const cell = within(row).getByText(change.display, { selector: `[data-metric="${change.metric_id}"]` });
        expect(cell.className.includes("delta-flagged"), `${item.ticker} ${change.metric_id}`).toBe(change.flagged);
      }
      if (item.flags.length === 0) expect(within(row).getByText("No deterioration flags.")).toBeTruthy();
    }
    const flagged = watchlist.items.find((i) => i.flags.length > 0)!;
    fireEvent.click(within(screen.getByTestId(`watch-${flagged.ticker}`)).getByRole("button", { name: /flag detail/ }));
    expect(screen.getAllByText(`Rule: ${flagged.flags[0].rule}`).length).toBeGreaterThan(0);
  });
});
