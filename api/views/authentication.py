from accounts.views import authentication_token_validity
from api.serializers.authentication import (LoginSerializer, LogoutSerializer,
                                            ProfileSerializer,
                                            SignupSerializer, UserSerializer)
from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def get_permissions(request):
    data = {'state': False, 'permissions': []}

    if request.user.is_authenticated:
        if request.user.is_superuser:
            permissions = {'state': True}
        else:
            permissions = request.user.get_all_permissions()
            data['permissions'] = list(permissions)
    return Response(data=data)


@api_view(['post'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save(request)

    serializer = UserSerializer(instance=user)
    data = serializer.data
    data['permissions'] = user.get_all_permissions()
    data['token'] = token.key
    return Response(data=data)


@api_view(['post'])
def logout(request):
    serializer = LogoutSerializer(data=request.data)
    serializer.save(request)
    return Response(data={'state': True})


@api_view(['post'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(request)
    return Response(data={'state': True})


@api_view(['post'])
def update_profile(request):
    attrs = {'data': {'state': False}}
    is_authenticated = authentication_token_validity(request)
    if is_authenticated:
        serializer = ProfileSerializer(instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
    attrs['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**attrs)
