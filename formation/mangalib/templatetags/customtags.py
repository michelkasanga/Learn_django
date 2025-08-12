from django import template
from django.template.defaultfilters import stringfilter 


register = template.Library()

#filtre
@register.filter
@stringfilter
def first_char(value):
    return value[8]

@register.filter(name= 'fact')
def factor(value):
    if value == 1:
        return 1
    return value * factor(value-1)

@register.filter
def lenghtis(value, size):
    return len(value) == size

#balise 

@register.simple_tag
def test_code(value):
    return f"Hello {value}"