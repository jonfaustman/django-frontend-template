from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def h5bp_html(lang):
    """ Returns HTML tag according to chosen language.
    """
    output=[
        '<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="%s"> <![endif]-->' % lang,
        '<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="%s"> <![endif]-->' % lang,
        '<!--[if IE 8]>    <html class="no-js lt-ie9" lang="%s"> <![endif]-->' % lang,
        '<!--[if gt IE 8]><!--> <html class="no-js" lang="%s"> <!--<![endif]-->' % lang,
    ]
    return '\n'.join(output)