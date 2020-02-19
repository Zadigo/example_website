from django.conf.urls import url
from django.conf.urls import re_path
from dashboard.views import IndexView, CreateNewView, ListItemsView, SettingsView, UpdateItemView, ItemDetailsView, DashboardLoginView

urlpatterns = [
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
    url(r'^login/$', DashboardLoginView.as_view(), name='dashboard_login'),
    url(r'^create/$', CreateNewView.as_view(), name='create'),
    url(r'list/(?P<pk>\d+)/update/$', UpdateItemView.as_view(), name='update'),
    url(r'list/(?P<pk>\d+)$', ItemDetailsView.as_view(), name='details'),
    url(r'list/$', ListItemsView.as_view(), name='list_items'),
    url(r'^index/$', IndexView.as_view(), name='index')
]