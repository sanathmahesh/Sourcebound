"""Turn a filing's HTML into plain text: one paragraph (or table row) per line.

10-K and 10-Q documents are "inline XBRL": ordinary HTML with XBRL tags wrapped around the numbers, plus a
hidden block (<ix:header>, inside a display:none element) holding the machine-readable contexts. The reader
never sees that block, so it is dropped, as are scripts, styles and anything styled display:none.

Rules, kept deliberately simple:
- block elements (p, div, tr, li, headings, br, ...) end a line;
- table cells are separated by a space, so a table row becomes one line ("Long-term debt $ 34,624");
- runs of whitespace (including non-breaking spaces) collapse to one space; empty lines are dropped.

The output is the "source text" every passage's character offsets refer to, so this function must be
deterministic: the same HTML always gives the same text.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser

BLOCK_TAGS = {
    "p", "div", "br", "tr", "li", "ul", "ol", "table", "h1", "h2", "h3", "h4", "h5", "h6", "hr",
    "section", "article", "blockquote", "center", "dt", "dd", "header", "footer", "title",
}
CELL_TAGS = {"td", "th"}
SKIP_TAGS = {"script", "style", "head", "ix:header"}
VOID_TAGS = {"br", "hr", "img", "meta", "link", "input", "col", "area", "base", "wbr"}
WHITESPACE = re.compile(r"\s+")


def _is_hidden(tag: str, attrs: list[tuple[str, str | None]]) -> bool:
    if tag in SKIP_TAGS:
        return True
    style = next((value or "" for name, value in attrs if name == "style"), "")
    return "display:none" in style.replace(" ", "").lower()


class _TextBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.current: list[str] = []
        self.skip_depth = 0  # > 0 while inside a hidden element

    def handle_starttag(self, tag, attrs):
        if self.skip_depth:
            if tag not in VOID_TAGS:
                self.skip_depth += 1
            return
        if _is_hidden(tag, attrs) and tag not in VOID_TAGS:
            self.skip_depth = 1
            return
        if tag in BLOCK_TAGS:
            self._end_line()

    def handle_startendtag(self, tag, attrs):
        if not self.skip_depth and tag in BLOCK_TAGS:
            self._end_line()

    def handle_endtag(self, tag):
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in BLOCK_TAGS:
            self._end_line()
        elif tag in CELL_TAGS:
            self.current.append(" ")

    def handle_data(self, data):
        if not self.skip_depth:
            self.current.append(data)

    def _end_line(self) -> None:
        line = WHITESPACE.sub(" ", "".join(self.current).replace("\xa0", " ")).strip()
        if line:
            self.lines.append(line)
        self.current = []

    def text(self) -> str:
        self._end_line()
        return "\n".join(self.lines)


def html_to_text(html: str) -> str:
    builder = _TextBuilder()
    builder.feed(html)
    builder.close()
    return builder.text()
