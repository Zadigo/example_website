import graphql_jwt
import graphene
from graphene import relay
from graphene.relay import mutation
from graphene.types.objecttype import ObjectType
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene_django.fields import DjangoListField
from accounts.models import MyUser, MyUserProfile


USER_MODEL = get_user_model()


class MyUsers(DjangoObjectType):
    class Meta:
        model = USER_MODEL
        fields = ('id', 'firstname', 'lastname', 'email')


class MyUserProfiles(DjangoObjectType):
    class Meta:
        model = MyUserProfile
        fields = ('id', 'address', 'city', 'myuser')


class TestUser(ObjectType):
    lastname = graphene.String()

    class Meta:
        interfaces = [relay.Node]


class MyUserConnection(relay.Connection):
    class Meta:
        node = TestUser


class UpdateProfile(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID()
        address = graphene.String(required=True)

    user_profile = graphene.Field(MyUserProfiles)

    @classmethod
    def mutate(cls, root, info, user_id, address):
        profile = MyUserProfile.objects.get(id=user_id)
        profile.address = address
        profile.save()
        return UpdateProfile(user_profile=profile) 



class Query(graphene.ObjectType):
    user = graphene.Field(MyUsers, user_id=graphene.ID(required=True))
    user_profile = graphene.Field(MyUserProfiles, user_id=graphene.String(required=True))
    # user_profiles = DjangoListField(MyUserProfiles)
    # user_profiles = graphene.List(MyUserProfiles)

    # Pagination
    # user_profiles = relay.ConnectionField(MyUserConnection)
    test_user = relay.ConnectionField(MyUserConnection)

    is_authenticated = graphene.Boolean()

    def resolve_users(self, info):
        return USER_MODEL.objects.all()

    def resolve_user(self, info, user_id):
        return USER_MODEL.objects.get(id=user_id)

    def resolve_user_profiles(self, info):
        return MyUserProfile.objects.prefetch_related('myuser').all()

    def resolve_user_profile(self, info, user_id):
        return MyUserProfile.objects.prefetch_related('myuser').get(pk=user_id)

    def resolve_is_authenticated(self, info):
        return info.context.user.is_authenticated


class Mutation(graphene.ObjectType):
    # update_profile = UpdateProfile.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
