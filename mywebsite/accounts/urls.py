from django.conf.urls import include, url
from django.urls import path

from accounts.views import profile, registration

app_name = 'accounts'

passwordpatterns = [
    url(r'^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>\w+\-\w+)$',
                registration.UnauthenticatedPasswordResetView.as_view(), name='reset'),
    url(r'^forgot-password$', registration.ForgotPasswordView.as_view(), name='forgot')
]

profilepatterns = [
    url(r'^change-password$', profile.ChangePasswordView.as_view(), name='change_password'),
    url(r'^contact-preferences$', profile.ContactPreferencesView.as_view(), name='contact'),
    url(r'^payment-methods$', profile.PaymentMethodsView.as_view(), name='payment'),
    url(r'^delete$', profile.ProfileDeleteView.as_view(), name='delete'),
    url(r'^data$', profile.ProfileDataView.as_view(), name='data'),
    url(r'^information$', profile.InformationView.as_view(), name='information'),
    url(r'^$', profile.IndexView.as_view(), name='home'),
]

urlpatterns = [
    path('profile/', include((profilepatterns, app_name), namespace='profile')),
    path('password/', include((passwordpatterns, app_name), namespace='password')),

    url(r'^login$', registration.LoginView.as_view(), name='login'),
    url(r'^logout$', registration.LogoutView.as_view(), name='logout'),
    url(r'^signup$', registration.SignupView.as_view(), name='signup'),
]
