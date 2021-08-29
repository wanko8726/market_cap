from django import template


register = template.Library()


@register.filter(name="division")
def division(value, args):
    if args == 0:
        return None
    return value / args
