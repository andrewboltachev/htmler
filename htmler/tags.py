EMPTY_TAGS = 'br img meta link'
EMPTY_TAGS = EMPTY_TAGS.split(' ')


ESCAPE_REPLACEMENTS = [
    ('&', '&amp;'),
    ('\'', '&apos;'),
    ('"', '&quot;'),
    ('<', '&lt;'),
    ('>', '&gt;')
]

def render_attributes(**attributes):
    def val(v):
        return reduce(lambda a, b: a.replace(b[0], b[1]), ESCAPE_REPLACEMENTS, v)
    def key(k):
        return k.rstrip('_').replace('_', '-')
    return ' '.join(['{k}="{v}"'.format(k=key(k), v=val(v)) for k, v in attributes.iteritems()])


def tag(name, *children, **attributes):
    rendered_attributes = render_attributes(**attributes)
    attributes_str = ' ' + rendered_attributes if len(rendered_attributes) else ''

    start_tag_begin = '<' + name
    start_tag_end = '>'

    start_tag = start_tag_begin + attributes_str + start_tag_end
    end_tag = '' if name in EMPTY_TAGS else ('</' + name + '>')

    contents = ''.join(children)

    return start_tag + contents + end_tag + '\n'
