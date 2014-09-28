from htmler.fun import html, head, meta, title, link, body, script, div


def bootstrap3(*contents):
    return '<!DOCTYPE html>' + html(
        head(
            meta(charset='utf-8'),
            meta(http_equiv="X-UA-Compatible", content="IE=edge"),
            meta(name_="viewport", content="width=device-width, initial-scale=1"),
            title('Bootstrap 101 Template'),
            link(href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css", rel="stylesheet")
        ),
        body(*(contents + (
            script(src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"),
            script(src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js")
        )))
    )


def container(*a, **kw):
    return div(*a, class_='container', **kw)
