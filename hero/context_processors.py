from django.template import Context
from django.conf import settings

def hero(request):
    context = Context(getattr(settings, 'HERO', {}))
    return context.flatten()
