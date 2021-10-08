from rest_framework.serializers import Serializer
from rest_framework import fields

class GetToken(Serializer):
    email = fields.EmailField(required=True)
    username = fields.CharField(required=False)
    password = fields.CharField(max_length=50, required=True)
