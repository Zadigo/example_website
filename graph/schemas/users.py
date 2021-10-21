import graphene
from accounts.models import MyUser, MyUserProfile
from django.core.exceptions import ValidationError
from graphene_django import DjangoObjectType
from django.contrib.auth.password_validation import validate_password


class UserSchema(DjangoObjectType):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'firstname', 'lastname')


class UserProfileSchema(DjangoObjectType):
    class Meta:
        model = MyUserProfile
        fields = ('address', 'city', 'myuser')


class UpdateProfile(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID()
        address = graphene.String(required=False)
        city = graphene.String(required=False)
        telephone = graphene.String(required=False)

    profile = graphene.Field(UserProfileSchema)

    def mutate(self, info, user_id, address=None, city=None, **kwargs):
        profile = MyUserProfile.objects.get(id=user_id)
        profile.address = address
        profile.city = city
        profile.save()
        return UpdateProfile(profile=profile)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserSchema)

    class Arguments:
        email = graphene.String()
        password1 = graphene.String()
        password2 = graphene.String()
        firstname = graphene.String()
        lastname = graphene.String()

    def mutate(self, info, email, password1, password2, firstname, lastname):
        if password1 != password2:
            raise ValidationError('Password do not match')

        validate_password(password2)

        attrs = {
            'email': email,
            'password': password2,
            'firstname': firstname,
            'lastname': lastname
        }
        try:
            user = MyUser.objects.create_user(**attrs)
        except:
            raise Exception('Account exists already')
        return CreateUser(user=user)
