from django.urls import re_path
from rest_framework.routers import DefaultRouter

from api.views import ProductsExample, ProductExample, CreateProductExample

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns.append(re_path(r'^product/(?P<pk>\d+)$', ProductExample.as_view(), name='api_product'))
urlpatterns.append(re_path(r'^product/create$', CreateProductExample.as_view(), name='api_create_product'))
urlpatterns.append(re_path(r'^products$', ProductsExample.as_view(), name='api_products'))
