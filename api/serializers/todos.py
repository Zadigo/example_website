from rest_framework.serializers import Serializer
from rest_framework import fields

class TodoSerializer(Serializer):
    id = fields.IntegerField()
    title = fields.CharField()
    completed = fields.BooleanField(default=False)
