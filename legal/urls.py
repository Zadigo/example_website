from django.conf.urls import url

from legal import views

app_name = 'legal'

urlpatterns = [
    url(r'^who-we-are$', views.AboutView.as_view(), name='about_us'),
    url(r'^terms-of-service$', views.CGU.as_view(), name='terms_of_service'),
    url(r'^terms-of-sale$', views.CGV.as_view(), name='terms_of_sale'),
    url(r'^privacy$', views.PrivacyView.as_view(), name='privacy'),
]
