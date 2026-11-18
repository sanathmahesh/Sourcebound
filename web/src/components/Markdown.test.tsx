import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Markdown } from "./Markdown";

const DOC = `<!-- Generated: do not edit -->

# Title

A paragraph that runs
onto a second line, with **bold**, *italic*, \`code\` and a [link](https://www.sec.gov/x).

- First item
  continues here
- Second item

1. One
2. Two

| Measure | Value |
|---|---|
| Cost | $0.107 |

\`\`\`
date,company
\`\`\`

[bad](javascript:alert(1))`;

describe("Markdown", () => {
  it("renders the subset the documents use", () => {
    const { container } = render(<Markdown text={DOC} />);
    expect(screen.getByRole("heading", { level: 1, name: "Title" })).toBeTruthy();
    expect(container.querySelector("p")!.textContent).toBe(
      "A paragraph that runs onto a second line, with bold, italic, code and a link.");
    expect(container.querySelector("strong")!.textContent).toBe("bold");
    expect(container.querySelector("em")!.textContent).toBe("italic");
    expect(screen.getByRole("link", { name: "link" }).getAttribute("href")).toBe("https://www.sec.gov/x");
    expect([...container.querySelectorAll("ul > li")].map((li) => li.textContent)).toEqual(["First item continues here", "Second item"]);
    expect(container.querySelectorAll("ol > li")).toHaveLength(2);
    expect(screen.getByRole("columnheader", { name: "Measure" })).toBeTruthy();
    expect(screen.getByRole("cell", { name: "$0.107" })).toBeTruthy();
    expect(container.querySelector("pre")!.textContent).toBe("date,company");
    expect(container.textContent).not.toContain("Generated");
  });

  it("never turns a javascript: URL into a link", () => {
    render(<Markdown text={DOC} />);
    expect(screen.queryByRole("link", { name: "bad" })).toBeNull();
  });
});

describe("Markdown on the published About documents", () => {
  it("renders each one with its title and no stray Markdown syntax", async () => {
    const { readFileSync } = await import("node:fs");
    const { resolve } = await import("node:path");
    const about = JSON.parse(readFileSync(resolve(process.cwd(), "../data/published/about.json"), "utf8"));
    for (const doc of about.documents as { title: string; markdown: string }[]) {
      const { container, unmount } = render(<Markdown text={doc.markdown} />);
      expect(container.querySelector("h1")?.textContent, doc.title).toBe(doc.title);
      expect(container.textContent, doc.title).not.toMatch(/\*\*|^#|\|---/m);
      unmount();
    }
  });
});
