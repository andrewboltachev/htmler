from htmler.tags import tag as tag1, render_attributes

def tag(*args, **kwargs):
    return tag1(*args, **kwargs).replace('\n', '').strip(' ')

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
