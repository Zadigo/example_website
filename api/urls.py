from django.urls import re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.views import todos

from api import views

router = DefaultRouter()

urlpatterns = [
    url(r'^todos', todos.get_todos)
]

urlpatterns.extend(router.urls)
