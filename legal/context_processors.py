from django.template.context import Context
from django.conf import settings


LEGAL = {
    'company_name': None,
    'urls': {
        'customer_service': None,
        'main': None
    },
    'emails': {
        'customer_service': None,
        'main': None
    }
}


def company_details(request):
    attrs = LEGAL | getattr(settings, 'LEGAL', {})
    context = Context(**attrs)
    return context.flatten()
