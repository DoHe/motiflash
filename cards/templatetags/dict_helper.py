from django import template

register = template.Library()


@register.simple_tag
def get_value(d, k):
    return d.get(k)
