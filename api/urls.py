from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from api.views import authentication, todos
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('profile', authentication.ProfileView)

urlpatterns = [
    url(r'^token', authentication.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^profile/update', authentication.update_profile),
    url(r'^signup', authentication.signup),
    url(r'^logout', authentication.logout),
    url(r'^login', authentication.login),
    url(r'^todos', todos.get_todos)
]

urlpatterns.extend(router.urls)
