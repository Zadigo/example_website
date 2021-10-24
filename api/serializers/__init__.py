from rest_framework.serializers import Serializer


def validate_serializer(serializer, instance=None, data=None) -> Serializer:
    """Calls and returns an instance of a serializer"""
    if not type(serializer) == 'class' and serializer != Serializer:
        raise TypeError('Serializer should be a type.')
    instance = serializer(instance=instance, data=data)
    instance.is_valid(raise_exception=True)
    return instance
