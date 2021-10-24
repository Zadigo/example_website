from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import MyUserProfile
from api.serializers.authentication import (LoginSerializer, LogoutSerializer,
                                            ProfileSerializer,
                                            SignupSerializer, UserSerializer)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class CustomPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s']
    }


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
    attrs = {'data': {'state': False, 'status': status.HTTP_400_BAD_REQUEST}}
    if request.user.is_authenticated:
        serializer = ProfileSerializer(instance=request.user.myuserprofile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        attrs.update(data=serializer.data, status=status.HTTP_200_OK)
    return Response(**attrs)


class ProfileView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = MyUserProfile.objects.filter(myuser__is_active=True)
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # HACK: To be able to get the authenticated user.
        # Unfortunately the self.user, is not set on the
        # __init__ of the serializer so just get it on
        # the body of the class
        user = getattr(serializer, 'user', None)
        validated_data = serializer.validated_data.copy()
        if user is not None:
            validated_data['user_id'] = user.id
        return Response(validated_data, status=status.HTTP_200_OK)
