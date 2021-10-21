from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = 'graph'

urlpatterns = [
    url(r'^$', GraphQLView.as_view(graphiql=True)),
]
