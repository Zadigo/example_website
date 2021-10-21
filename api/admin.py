from accounts import get_custom_site
from django.contrib import admin
from graphql_jwt.refresh_token.models import RefreshToken
# from rest_framework.authtoken.models import Token
from api import register_graphql_models

site = get_custom_site()


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

site.register(RefreshToken)
# site.register(Token, TokenAdmin)
register_graphql_models(site)
