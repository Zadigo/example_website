from django.conf.urls import re_path, url

from dashboard.views import (CreateNewView, DashboardLoginView, IndexView,
                             ItemDetailsView, ListItemsCardsView,
                             ListItemsView, SettingsView, UpdateItemView,
                             UserDetailsView)

urlpatterns = [
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
    url(r'^login/$', DashboardLoginView.as_view(), name='dashboard_login'),
    url(r'^create/$', CreateNewView.as_view(), name='create'),
    url(r'^list/cards/$', ListItemsCardsView.as_view(), name='list_items_cards'),
    
    url(r'list/(?P<pk>\d+)/update/$', UpdateItemView.as_view(), name='update'),
    url(r'list/users/(?P<pk>\d+)$', UserDetailsView.as_view(), name='user_details'),
    url(r'list/(?P<pk>\d+)$', ItemDetailsView.as_view(), name='details'),

    url(r'list/$', ListItemsView.as_view(), name='list_items'),
    url(r'^index/$', IndexView.as_view(), name='index')
]
