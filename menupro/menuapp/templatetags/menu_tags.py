from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def draw_menu(menu_items):
    """
    Recursively draw the menu tree.
    """
    if menu_items:
        result = '<ul>'
        for item in menu_items:
            result += '<li><a href="%s">%s</a>' % (item.url, item.name)
            result += draw_menu(item.children.all())
            result += '</li>'
        result += '</ul>'
        return mark_safe(result)
    return ''
