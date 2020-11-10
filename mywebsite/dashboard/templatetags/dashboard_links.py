from django.template import Library

register = Library()

SIDEBAR_LINKS = [
    ('dashboard:home', {'icon': 'fas fa-chart-pie', 'title': 'Dashboard'})
]

@register.inclusion_tag('components/navs/sidebar_link.html')
def sidebar():
    return SIDEBAR_LINKS
