from django.conf.urls import url
from django.urls.conf import path, include

from dashboard import views

app_name = 'dashboard'

apipatterns = [
    url(r'^download-csv$', views.download_csv, name='csv'),
    url(r'^delete$', views.delete_products, name='delete'),
    url(r'^duplicate$', views.duplicate_products, name='duplicate')
]

settingspatterns = [
    url(r'^general$', views.SettingsGeneralView.as_view(), name='general'),
    url(r'^$', views.SettingsHomeView.as_view(), name='home'),
]

urlpatterns = [
    path('settings/', include((settingspatterns, app_name), namespace='settings')),
    path('api/', include((apipatterns, app_name), namespace='api')),

    url(r'^profile/id$', views.ProfileView.as_view(), name='profile'),
    url(r'^products/id$', views.ProductView.as_view(), name='product'),
    url(r'^products$', views.ProductsView.as_view(), name='products'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
