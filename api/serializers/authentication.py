from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import Permission
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import fields, serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer

USER_MODEL = get_user_model()


class UsernameValidator(RegexValidator):
    message = 'Username is not valid. Allowed characters are a-z, A-Z, 0-9 and -_.'


class AuthenticationMixin(Serializer):
    email = fields.EmailField(required=True)
    username = fields.CharField(required=False)
    password = fields.CharField(required=True)

    def get_object(self):
        if not hasattr(self, '_errors'):
            raise ValueError('To retrieve the user call is_valid')
        if self.errors:
            raise ValueError('The serializer is not valid')
        return get_object_or_404(USER_MODEL, email=self.validated_data['email'])

    def save(self, request, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(request, self.instance, validated_data)
        else:
            self.instance = self.create(request, validated_data)

        if self.instance is None:
            raise serializers.ValidationError({'signup': 'Could not create account'})

        return self.instance


class SerializerMixin:
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field != 'email':
                setattr(instance, field, value)
                
        with transaction.atomic():
            instance.save()

        return instance


class UserSerializer(Serializer):
    email = fields.EmailField()
    lastname = fields.CharField()
    firstname = fields.CharField()
    is_active = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=True)


class LoginSerializer(AuthenticationMixin):
    def create(self, request, validated_data):
        user = authenticate(request, email=validated_data['email'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError({'account': 'Could not login user'})

        try:
            token = Token.objects.create(user=user)
        except IntegrityError:
            raise serializers.ValidationError({'email': 'User exists'})
        else:
            login(request, user, backend=None)
            return user, token


class LogoutSerializer(AuthenticationMixin):
    email = None
    username = None
    password = None

    def save(self, request, **kwargs):
        logout(request)


class SignupSerializer(AuthenticationMixin):
    password = None
    username = fields.CharField(
        required=False, 
        validators=[UsernameValidator(r'^[a-zA-Z0-9-_]+$'), MinLengthValidator(4)]
    )
    firstname = fields.CharField(required=True)
    lastname = fields.CharField(required=True)
    password1 = fields.CharField(required=True)
    password2 = fields.CharField(required=True)

    def create(self, request, validated_data, permissions=[]):
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password1': 'Passwords do not match'})

        validate_password(password2)

        attrs = {
            'email': validated_data['email'],
            'password': password2,
            'username': validated_data['username'],
            'lastname': validated_data['lastname'],
            'firstname': validated_data['firstname']
        }
        try:
            user = USER_MODEL.objects.create_user(**attrs)
        except IntegrityError:
            raise serializers.ValidationError({'account': 'Account exists already'})
        except Exception:
            raise serializers.ValidationError({'error': 'An error occured'})
        else:
            _permissions = {
                'view_myuser', 'change_myuser', 'delete_myuser', 
                'view_myuserprofile', 'change_myuserprofile'
            }
            _permissions = _permissions | set(permissions)
            queryset = Permission.objects.filter(codename__in=_permissions)
            user.user_permissions.add(*queryset)
            return user


class ProfileSerializer(SerializerMixin, Serializer):
    avatar = fields.ImageField(required=False)

    birthdate = fields.DateField(required=False)
    telephone = fields.CharField(required=False)

    address = fields.CharField(required=False)
    city = fields.CharField(required=False)
    zip_code = fields.CharField(required=False)

    def update(self, instance, validated_data):
        # Check if the user has the permission
        # to modify his user profile
        if not instance.myuser.has_perm('accounts.change_myuserprofile'):
            raise serializers.ValidationError('Permission denied', code='permission_denied')
        return super().update(self.instance, validated_data)
