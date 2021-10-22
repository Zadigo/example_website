from django.urls import re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.views import todos, authentication

from api import views

router = DefaultRouter()

urlpatterns = [
    url(r'^profile/update', authentication.update_profile),
    url(r'^signup', authentication.signup),
    url(r'^logout', authentication.logout),
    url(r'^login', authentication.login),
    url(r'^todos', todos.get_todos)
]

urlpatterns.extend(router.urls)
