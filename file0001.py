EMPTY_TAGS = 'br img'
EMPTY_TAGS = EMPTY_TAGS.split(' ')

def tag(name, *children, **attributes):
    attributes_str = ' ' + ' '.join([k.replace('_', '-') + '=' + v for k, v in attributes.iteritems()])
    if name in EMPTY_TAGS:
        return '<%s%s>%s</%s>'
    return '<%s%s>%s</%s>'
