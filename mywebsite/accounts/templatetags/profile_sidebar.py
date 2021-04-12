from django.shortcuts import resolve_url
from django.template import Library
from django.utils.translation import gettext_lazy as _

register = Library()


LINKS = [
    ['home', {'name': _('Aperçu du compte')}],
    ['information', {'name': _('Informations')}],
    ['payment', {'name': _('Mode de paiement')}],
    ['change_password', {'name': _('Mot de passe')}],
    ['contact', {'name': _('Préférences de contact')}],
    ['data', {'name': _('Mes données')}],
]


@register.inclusion_tag('includes/profile/sidebar.html')
def sidebar():
    def resolve(values):
        name, params = values
        link = f'accounts:profile:{name}'
        params.update({'href': resolve_url(link)})
        return link, params

    resolved_links = map(resolve, LINKS)
    return dict(links=list(resolved_links))
