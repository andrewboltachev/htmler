from file0002 import tag, render_attributes

def test_renders_basic_tags():
    assert tag('div') == '<div></div>'


def test_renders_empty_tags_without_closing_tag():
    assert tag('br') == '<br>'


def tes1t_renders_attributes():
    assert tag('div', id='myid') == '<div id="myid"></div>'


def test_attributes_rendering_basic():
    assert render_attributes(href='myid') == 'href="myid"'
