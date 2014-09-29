from htmler.fun import html, head, meta, title, link, body, script, div


def bootstrap3(*contents, **kwargs):
    add_head = kwargs.get('add_head', ())
    add_body = kwargs.get('add_body', ())
    return '<!DOCTYPE html>' + html(
        head(
            meta(charset='utf-8'),
            meta(http_equiv="X-UA-Compatible", content="IE=edge"),
            meta(name_="viewport", content="width=device-width, initial-scale=1"),
            title('Bootstrap 101 Template'),
            link(href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css", rel="stylesheet"),
            *add_head
        ),
        body(*(contents + (
            script(src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"),
            script(src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js")
        ) + add_body))
    )


def _upd_class(kw, x):
    if not 'class_' in kw:
        kw['class_'] = x
    else:
        kw['class_'] += ' ' + x


def container(*a, **kw):
    _upd_class(kw, 'container')
    return div(*a, **kw)


def row(*a, **kw):
    _upd_class(kw, 'row')
    return div(*a, **kw)

def col6(*a, **kw):
    _upd_class(kw, 'col-md-6')
    return div(*a, **kw)
