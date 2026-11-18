"""Search a company's filings from the command line.

Run:  uv run python -m sourcebound.pipeline.search WMT "revolving credit facility"
      uv run python -m sourcebound.pipeline.search WMT "covenants" --section liquidity --section debt_note -k 5

Prints ranked passages with their score, section, filing and link. Needs data/index/<TICKER>.json
(built by sourcebound.pipeline.build_index).
"""

from __future__ import annotations

import argparse
import textwrap

from sourcebound.retrieval.index import load_index, search


def main() -> None:
    parser = argparse.ArgumentParser(description="Search a company's 10-K and 10-Q passages (BM25).")
    parser.add_argument("ticker")
    parser.add_argument("query")
    parser.add_argument("--section", action="append", help="only these sections (repeatable)")
    parser.add_argument("--form", action="append", help="only these forms, e.g. 10-K (repeatable)")
    parser.add_argument("-k", type=int, default=8, help="number of passages (default 8)")
    args = parser.parse_args()

    index = load_index(args.ticker)
    hits = search(index, args.query, k=args.k,
                  sections=set(args.section) if args.section else None,
                  forms=set(args.form) if args.form else None)
    scope = f" in {', '.join(args.section)}" if args.section else ""
    print(f'{index.ticker}: "{args.query}"{scope}: {len(hits)} passages from {len(index.chunks)}\n')
    for hit in hits:
        c = hit.chunk
        print(f"{hit.rank}. score {hit.score:.2f} | {c.section} | {c.form} for {c.period_end}, filed {c.filed} | {c.id}")
        print(f"   {c.url}  (characters {c.start}-{c.end})")
        snippet = " ".join(c.text.split())
        print(textwrap.indent(textwrap.fill(snippet[:500] + ("…" if len(snippet) > 500 else ""), 100), "   "))
        print()


if __name__ == "__main__":
    main()
