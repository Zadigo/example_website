import debug_toolbar
from accounts.admin import site
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from example_website.views import view

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # path('graphql', GraphQLView.as_view(graphiql=True)),
    path('api/v1/', include('api.urls')),
    
    path('legal/', include('legal.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', site.urls),
    # path('', include('hero.urls')),
    url(r'', view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
