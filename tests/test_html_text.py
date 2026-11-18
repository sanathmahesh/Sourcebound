"""Filing HTML to plain text: one paragraph per line, hidden XBRL data dropped, tables flattened."""

from sourcebound.edgar.html_text import html_to_text


def test_paragraphs_become_lines_and_whitespace_collapses():
    html = "<html><body><p>Our   revolving\n credit facility</p><div>matures in <b>2029</b>.</div></body></html>"
    assert html_to_text(html) == "Our revolving credit facility\nmatures in 2029."


def test_hidden_inline_xbrl_header_and_display_none_are_dropped():
    html = (
        '<html><body><div style="display:none"><ix:header><ix:hidden>secret context</ix:hidden></ix:header></div>'
        "<p>Visible text</p><span style=\"display: none\">also hidden</span></body></html>"
    )
    assert html_to_text(html) == "Visible text"


def test_scripts_and_styles_are_dropped():
    assert html_to_text("<style>p{}</style><script>x=1</script><p>Text</p>") == "Text"


def test_table_rows_become_lines_with_cells_separated():
    html = "<table><tr><td>Long-term debt</td><td>$</td><td>34,624</td></tr><tr><td>Total</td><td>9</td></tr></table>"
    assert html_to_text(html) == "Long-term debt $ 34,624\nTotal 9"


def test_entities_and_non_breaking_spaces():
    assert html_to_text("<p>AT&amp;T&nbsp;&nbsp;Inc.&#8217;s</p>") == "AT&T Inc.’s"


def test_br_breaks_a_line():
    assert html_to_text("<p>Item 7.<br/>Management</p>") == "Item 7.\nManagement"


def test_inline_xbrl_facts_in_the_body_are_kept():
    html = '<p>Net sales were $<ix:nonFraction name="us-gaap:Revenues">706,413</ix:nonFraction> million.</p>'
    assert html_to_text(html) == "Net sales were $706,413 million."
