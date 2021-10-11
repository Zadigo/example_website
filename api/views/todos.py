import requests
from api.serializers.todos import BasePaginator
from api.serializers.todos import TodoSerializer
from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def get_todos(request, **kwargs):
    queryset = cache.get('todos', [])
    if not queryset:
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        queryset = response.json()
        cache.set('todos', queryset, 3600)
    serializer = TodoSerializer(data=queryset, many=True)
    serializer.is_valid(raise_exception=True)

    paginator = BasePaginator()
    data = paginator.paginate_queryset(queryset, request)
    return paginator.get_paginated_response(data)

    # return Response(data=serializer.data, status=status.HTTP_200_OK)

