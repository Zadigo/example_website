from django.urls import re_path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

urlpatterns = []

urlpatterns.extend(router.urls)
