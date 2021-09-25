import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('hero.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
