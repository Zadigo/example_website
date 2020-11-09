from django.conf.urls import url
from django.urls.conf import path, include

from dashboard import views

app_name = 'dashboard'

apipatterns = [
    url(r'^download-csv$', views.download_csv, name='csv'),
    url(r'^delete$', views.delete_products, name='delete'),
    url(r'^duplicate$', views.duplicate_products, name='duplicate')
]

urlpatterns = [
    path('api/', include((apipatterns, app_name), namespace='api')),

    url(r'^products/id$', views.ProductView.as_view(), name='product'),
    url(r'^products$', views.ProductsView.as_view(), name='products'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
