// A small Markdown renderer for the About documents: headings, paragraphs, lists, tables, code blocks and
// inline bold, italic, code and links. It builds React elements (never raw HTML), and only http(s), relative
// and #anchor links become links. The documents are the project's own, so this subset is all they use.
import type { ReactNode } from "react";

const INLINE = /(`[^`]+`|\*\*[^*]+\*\*|\*[^*\s][^*]*\*|\[[^\]]+\]\([^)\s]+\))/g;

function safeHref(href: string): string | null {
  return /^(https?:\/\/|#|\/|\.\.?\/|[\w-]+(\.md)?$)/.test(href) && !/^javascript:/i.test(href) ? href : null;
}

function inline(text: string): ReactNode[] {
  return text.split(INLINE).filter(Boolean).map((part, n) => {
    if (part.startsWith("`") && part.endsWith("`") && part.length > 1) return <code key={n}>{part.slice(1, -1)}</code>;
    if (part.startsWith("**") && part.endsWith("**")) return <strong key={n}>{inline(part.slice(2, -2))}</strong>;
    if (part.startsWith("*") && part.endsWith("*") && part.length > 2) return <em key={n}>{inline(part.slice(1, -1))}</em>;
    const link = /^\[([^\]]+)\]\(([^)\s]+)\)$/.exec(part);
    if (link) {
      const href = safeHref(link[2]);
      if (!href) return <span key={n}>{link[1]}</span>;
      const external = href.startsWith("http");
      return <a key={n} href={href} {...(external ? { target: "_blank", rel: "noreferrer" } : {})}>{inline(link[1])}</a>;
    }
    return part;
  });
}

const cells = (line: string) => line.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());

export function Markdown({ text }: { text: string }) {
  const lines = text.replace(/<!--[\s\S]*?-->/g, "").split("\n");
  const blocks: ReactNode[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const key = blocks.length;
    if (!line.trim()) { i += 1; continue; }
    const heading = /^(#{1,4}) (.*)$/.exec(line);
    if (heading) {
      const Tag = `h${heading[1].length}` as "h1" | "h2" | "h3" | "h4";
      blocks.push(<Tag key={key}>{inline(heading[2])}</Tag>);
      i += 1;
    } else if (line.startsWith("```")) {
      const body: string[] = [];
      for (i += 1; i < lines.length && !lines[i].startsWith("```"); i += 1) body.push(lines[i]);
      blocks.push(<pre key={key}>{body.join("\n")}</pre>);
      i += 1;
    } else if (line.trim().startsWith("|") && lines[i + 1]?.trim().startsWith("|---")) {
      const header = cells(line);
      const rows: string[][] = [];
      for (i += 2; i < lines.length && lines[i].trim().startsWith("|"); i += 1) rows.push(cells(lines[i]));
      blocks.push(
        <div key={key} className="table-wrap"><table>
          <thead><tr>{header.map((h, n) => <th key={n}>{inline(h)}</th>)}</tr></thead>
          <tbody>{rows.map((row, r) => <tr key={r}>{row.map((c, n) => <td key={n}>{inline(c)}</td>)}</tr>)}</tbody>
        </table></div>,
      );
    } else if (/^(- |\d+\. )/.test(line)) {
      const ordered = /^\d+\. /.test(line);
      const items: string[] = [];
      for (; i < lines.length && (/^(- |\d+\. )/.test(lines[i]) || /^ {2,}\S/.test(lines[i])); i += 1) {
        if (/^(- |\d+\. )/.test(lines[i])) items.push(lines[i].replace(/^(- |\d+\. )/, ""));
        else items[items.length - 1] += " " + lines[i].trim();
      }
      const children = items.map((item, n) => <li key={n}>{inline(item)}</li>);
      blocks.push(ordered ? <ol key={key}>{children}</ol> : <ul key={key}>{children}</ul>);
    } else {
      const para: string[] = [];
      for (; i < lines.length && lines[i].trim() && !/^(#{1,4} |```|\||- |\d+\. )/.test(lines[i]); i += 1) para.push(lines[i].trim());
      if (para.length === 0) { para.push(line.trim()); i += 1; }
      blocks.push(<p key={key}>{inline(para.join(" "))}</p>);
    }
  }
  return <div className="markdown">{blocks}</div>;
}
