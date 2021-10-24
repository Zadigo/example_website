from accounts import get_custom_site
from rest_framework.authtoken.models import Token

site = get_custom_site()

site.register(Token)
