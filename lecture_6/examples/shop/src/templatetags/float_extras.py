from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='fractional_part')
@stringfilter
def fractional_part(value, arg=2):
    """Get the fractional part of a float number in django template"""
    try:
        return value.split(".")[-1][:int(arg)]
    except Exception:
        return ""

