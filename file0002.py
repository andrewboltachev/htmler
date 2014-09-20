EMPTY_TAGS = 'br img'
EMPTY_TAGS = EMPTY_TAGS.split(' ')


def render_attributes(**attributes):
    return ' '.join(['{k}="{v}"'.format(k=k, v=v) for k, v in attributes.iteritems()])


def tag(name, **attributes):
    start_tag_begin = '<{name}'
    rendered_attributes = render_attributes(**attributes)
    start_tag_end = '>'

    start_tag = start_tag_begin + rendered_attributes + start_tag_end
    end_tag = '' if name in EMPTY_TAGS else '</{name}>'

    return (start_tag + end_tag).format(name=name)
