from django import template
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.inclusion_tag('components/tables/headers.html')
def header(*headers):
    context = {}
    context.update({'headers': [header for header in headers]})
    return context
