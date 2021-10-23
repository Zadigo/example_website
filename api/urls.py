from django.conf.urls import url
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import authentication, todos
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

urlpatterns = [
    url(r'^token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^profile/update', authentication.update_profile),
    url(r'^signup', authentication.signup),
    url(r'^logout', authentication.logout),
    url(r'^login', authentication.login),
    url(r'^todos', todos.get_todos)
]

urlpatterns.extend(router.urls)
