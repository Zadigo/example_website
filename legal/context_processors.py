from django.template.context import Context
from django.conf import settings


LEGAL = {
    'host': None,
    'hosting_company_name': None,
    'hosting_company_address': None,
    'data_protection_bureau_website': 'https://www.cnil.fr/',
    'cookie_policy': 'https://www.cnil.fr/fr/cookies-traceurs-que-dit-la-loi'
}


def legal(request):
    attrs = LEGAL | getattr(settings, 'LEGAL', {})
    context = Context(attrs)
    return context.flatten()
