from django.apps import apps as django_apps

def get_custom_site():
    from accounts.admin import site
    return site
