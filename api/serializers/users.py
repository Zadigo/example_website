from rest_framework.serializers import Serializer
from rest_framework import fields

class UserProfileSerializer(Serializer):
    avatar = fields.URLField()
    zip_code = fields.IntegerField()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


class UserSerializer(Serializer):
    user_profile = UserProfileSerializer()
    username = fields.CharField(read_only=True)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)


