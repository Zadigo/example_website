from django.apps import apps as django_apps


def register_graphql_models(custom_site):
    app = django_apps.get_app_config('graphql_auth')
    for _, model in app.models.items():
        custom_site.register(model)
