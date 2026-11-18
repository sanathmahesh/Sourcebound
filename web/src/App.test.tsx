import { describe, expect, it } from "vitest";
import { parseRoute } from "./App";

describe("parseRoute", () => {
  it("maps each screen's hash to its page", () => {
    expect(parseRoute("")).toEqual({ page: "portfolio" });
    expect(parseRoute("#/")).toEqual({ page: "portfolio" });
    expect(parseRoute("#/c/wmt")).toEqual({ page: "memo", ticker: "WMT" });
    expect(parseRoute("#/c/WMT/verification")).toEqual({ page: "verification", ticker: "WMT" });
    expect(parseRoute("#/watchlist")).toEqual({ page: "watchlist" });
    expect(parseRoute("#/results")).toEqual({ page: "results" });
    expect(parseRoute("#/about")).toEqual({ page: "about" });
    expect(parseRoute("#/about/04-risk-control-table")).toEqual({ page: "about", doc: "04-risk-control-table" });
  });

  it("does not turn arbitrary text into a data path", () => {
    expect(parseRoute("#/c/../../etc")).toEqual({ page: "missing" });
    expect(parseRoute("#/c/WMT/other")).toEqual({ page: "missing" });
    expect(parseRoute("#/nowhere")).toEqual({ page: "missing" });
  });
});
