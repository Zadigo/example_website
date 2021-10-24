import json

from django.template import Library
from django.utils.html import format_html

register = Library()


@register.simple_tag(takes_context=True)
def organization_script(context):
    base = """
    <script type="application/ld+json">
        {content}
    </script>
    """

    content = {
        '@context': 'https://schema.org',
        '@type': 'Organization',
        'image': [],
        '@id': context['domain'],
        'name': context['company_name'],
        'description': context['company_description'],
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': f"{context['contact']['address']} {context['contact']['zip_code']}",
            'addressLocality': 'Lille',
            'addressRegion': 'Haut-de-France',
            'postalCode': '59000',
            'addressCountry': 'FR'
        },
        'ContactPoint': [
            {
                '@type': 'ContactPoint',
                'ContactType': 'Customer service',
                'url': context['domain']
            }
        ],
        'email': f"mailto:{context['contact']['emails']['main'] }",
        'url': context['domain'],
        'telephone': f"{context['contact']['telephone']['main']}",
        'founder': {
            '@type': 'Person',
            'givenName': 'John',
            'familyName': 'Pendenque',
            'brand': {
                '@type': 'Thing',
                'name': f"{context['company_name']}"
            },
            'jobTitle': 'Founder, CEO'
        }
    }

    script = format_html(base, content=content)
    return script
