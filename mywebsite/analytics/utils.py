from django.core.exceptions import ImproperlyConfigured
from django.apps import apps
from django.conf import settings
import secrets

def create_analytics_reference(prefix=None):
    token = secrets.token_hex(10)
    if prefix is not None:
        return f'{prefix}{token}'
    return token


def get_store_model():
    try:
        model = settings.STORE_MODEL
    except:
        raise ImproperlyConfigured(
            "You should configure the Store model to use in settings for the cart application")
    else:
        return apps.get_model(model, require_ready=False)
