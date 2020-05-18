from django.conf.urls import re_path, url

from dashboard import views

urlpatterns = [
    # url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    # url(r'^login/$', views.DashboardLoginView.as_view(), name='dashboard_login'),
    # url(r'^create/$', views.CreateNewView.as_view(), name='create'),
    # url(r'^list/cards/$', views.ListItemsCardsView.as_view(), name='list_items_cards'),
    
    # url(r'list/(?P<pk>\d+)/update/$', views.UpdateItemView.as_view(), name='update'),
    # url(r'list/users/(?P<pk>\d+)$', views.UserDetailsView.as_view(), name='user_details'),
    url(r'list/(?P<pk>\d+)$', views.ItemDetailsView.as_view(), name='dashboard_details'),
    url(r'list/$', views.ListItemsView.as_view(), name='dashboard_products'),
    url(r'^index/$', views.IndexView.as_view(), name='index')
]
