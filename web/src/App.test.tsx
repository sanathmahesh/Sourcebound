import { describe, expect, it } from "vitest";
import { parseRoute } from "./App";

describe("parseRoute", () => {
  it("maps each screen's hash to its page", () => {
    expect(parseRoute("")).toEqual({ page: "portfolio" });
    expect(parseRoute("#/")).toEqual({ page: "portfolio" });
    expect(parseRoute("#/memo/wmt")).toEqual({ page: "memo", ticker: "WMT" });
    expect(parseRoute("#/memo/WMT/verification")).toEqual({ page: "verification", ticker: "WMT" });
    expect(parseRoute("#/watchlist")).toEqual({ page: "watchlist" });
    expect(parseRoute("#/results")).toEqual({ page: "results" });
    expect(parseRoute("#/about")).toEqual({ page: "about" });
    expect(parseRoute("#/about/04-risk-control-table")).toEqual({ page: "about", doc: "04-risk-control-table" });
  });

  it("does not turn arbitrary text into a data path", () => {
    expect(parseRoute("#/memo/../../etc")).toEqual({ page: "missing" });
    expect(parseRoute("#/memo/WMT/other")).toEqual({ page: "missing" });
    expect(parseRoute("#/c/WMT")).toEqual({ page: "missing" });
    expect(parseRoute("#/nowhere")).toEqual({ page: "missing" });
  });
});
