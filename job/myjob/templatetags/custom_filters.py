from django import template

register = template.Library()

@register.filter
def remove(value, arg):
    return [item for item in value if item != arg]