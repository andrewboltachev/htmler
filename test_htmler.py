from htmler.tags import tag, render_attributes, escape_child, SafeString, html_escape

def test_renders_basic_tags():
    assert tag('div') == '<div></div>'


def test_renders_empty_tags_without_closing_tag():
    assert tag('br') == '<br>'


def test_attributes_rendering_basic():
    assert render_attributes(href='myid') == 'href="myid"'


def test_renders_attributes():
    assert tag('div', href='myid') == '<div href="myid"></div>'


def test_renders_contents():
    assert tag('div', tag('br'), tag('div', tag('img'))) == '<div><br><div><img></div></div>'

def test_handles_attributes_underlines():
    assert render_attributes(id_='myid') == 'id="myid"'


def test_handles_attributes_underlines_2():
    assert render_attributes(http_equiv='myid') == 'http-equiv="myid"'


def test_escapes_attributes_values():
    assert render_attributes(http_equiv='\'\"&<>') == 'http-equiv="&apos;&quot;&amp;&lt;&gt;"'

def test_escapes_attributes_values_edge_case1():
    assert render_attributes(http_equiv='&amp;') == 'http-equiv="&amp;amp;"'


def test_escapes_strings_passed_to_tags():
    assert tag('div', 'this must be escaped: "&<>\'"', tag('div', tag('br'))) == '<div>this must be escaped: &quot;&amp;&lt;&gt;&apos;&quot;<div><br></div></div>'


def test_escape_child_escapes_if_not_safestring():
    assert escape_child('<div>') == '&lt;div&gt;'


def test_escape_child_doesnt_escape_if_safestring():
    assert escape_child(SafeString('<div>')) == '<div>'


def test_safestring_convertes_to_string_transpatently():
    assert str(SafeString('<div>')) == '<div>'

def test_html_escape_makes_anything_a_string():
    assert html_escape({}) == '{}'
