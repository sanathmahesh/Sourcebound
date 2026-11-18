import { readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { describe, expect, it } from "vitest";
import type { Memo } from "./contracts/types";
import { formatDate, formatMillions, formatRate, formatRaw, formatValue, toFixedPy } from "./format";

describe("formatValue", () => {
  it("formats like the Python engine (sourcebound/memo/render.py format_metric)", () => {
    expect(formatValue(1.208346, "x", "ok")).toBe("1.21x");
    expect(formatValue(23.59939, "%", "ok")).toBe("23.6%");
    expect(formatValue(51_512_000_000, "USD", "ok")).toBe("$51.5 billion");
    expect(formatValue(1_234_512_000_000, "USD", "ok")).toBe("$1,234.5 billion");
    expect(formatValue(-250_400_000, "USD", "ok")).toBe("-$250 million");
    expect(formatValue(12_345, "USD", "ok")).toBe("$12,345");
    expect(formatValue(null, "x", "not_available")).toBe("not available");
    expect(formatValue(3.2, "x", "not_meaningful")).toBe("not meaningful");
    expect(formatValue(null, "x", "net_cash")).toBe("net cash");
    expect(formatValue(-0.5, "x", "net_cash")).toBe("-0.50x (net cash)");
  });

  it("matches every metric chip in every published memo", () => {
    const dir = resolve(process.cwd(), "../data/published/companies");  // tests run from web/
    let checked = 0;
    for (const ticker of readdirSync(dir)) {
      const memo: Memo = JSON.parse(readFileSync(join(dir, ticker, "memo.json"), "utf8"));
      for (const section of memo.sections)
        for (const claim of section.claims)
          for (const seg of claim.segments) {
            const metric = seg.t === "metric" && seg.metric_id ? memo.metrics[seg.metric_id] : undefined;
            if (!metric || !["USD", "x", "%"].includes(metric.unit)) continue;
            expect(formatValue(metric.value, metric.unit, metric.status), `${ticker} ${seg.metric_id}`).toBe(seg.v);
            checked += 1;
          }
    }
    expect(checked).toBeGreaterThan(100);
  });
});

describe("toFixedPy", () => {
  it("rounds exact ties to even and everything else to nearest, as Python does", () => {
    // Expected values printed by Python 3.12: f"{x:.{d}f}"
    expect(toFixedPy(47.25, 1)).toBe("47.2");
    expect(toFixedPy(47.35, 1)).toBe("47.4");
    expect(toFixedPy(2.675, 2)).toBe("2.67");
    expect(toFixedPy(0.125, 2)).toBe("0.12");
    expect(toFixedPy(0.375, 2)).toBe("0.38");
    expect(toFixedPy(2.5, 0)).toBe("2");
    expect(toFixedPy(3.5, 0)).toBe("4");
    expect(toFixedPy(-1.005, 2)).toBe("-1.00");
    expect(toFixedPy(1234567.891, 0)).toBe("1234568");
  });
});

describe("formatRaw and formatRate", () => {
  it("shows XBRL inputs in full and rates with their sample size", () => {
    expect(formatRaw(34_624_000_000, "USD")).toBe("$34,624,000,000");
    expect(formatRaw(-1_500_000, "USD")).toBe("-$1,500,000");
    expect(formatRate({ value: 0.8593155, n: 526 })).toBe("85.9% (n = 526)");
    expect(formatRate({ value: null, n: 0 })).toBe("not measured (n = 0)");
  });
});

describe("formatDate and formatMillions", () => {
  it("shows dates as the design does and ladder amounts in whole millions", () => {
    expect(formatDate("2026-08-04")).toBe("4 Aug 2026");
    expect(formatDate("2026-11-18T07:56:41Z")).toBe("18 Nov 2026");
    expect(formatDate(null)).toBe("not available");
    expect(formatMillions(3_542_000_000)).toBe("3,542");
    expect(formatMillions(23_255_400_000)).toBe("23,255");
    expect(formatMillions(-2_500_000)).toBe("-2");
  });
});
