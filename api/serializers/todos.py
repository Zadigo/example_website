from rest_framework.serializers import Serializer
from rest_framework import fields
from rest_framework.pagination import LimitOffsetPagination


class BasePaginator(LimitOffsetPagination):
    default_limit = 50


class TodoSerializer(Serializer):
    id = fields.IntegerField()
    title = fields.CharField()
    completed = fields.BooleanField(default=False)
