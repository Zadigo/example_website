from accounts import admin, get_custom_site
# from rest_framework.authtoken.models import Token
from api import register_graphql_models
from graphql_jwt.refresh_token.models import RefreshToken

site = get_custom_site()


# class TokenAdmin(admin.ModelAdmin):
#     list_display = ('key', 'user', 'created')
#     fields = ('user',)
#     ordering = ('-created',)


site.register(RefreshToken)
# site.register(Token, TokenAdmin)
register_graphql_models(site)
