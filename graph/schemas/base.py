import graphene
from accounts.models import MyUser, MyUserProfile
from api.schemas.users import CreateUser, UpdateProfile, UserProfileSchema, UserSchema
from graphene import relay
from graphql_auth import mutations
from graphene_django import DjangoListField


class Query(graphene.ObjectType):
    all_users = DjangoListField(UserSchema)
    user = graphene.Field(UserSchema, user_id=graphene.ID(required=True))
    user_profile = graphene.Field(UserProfileSchema, user_id=graphene.ID(required=True))

    def resolve_all_users(self, info):
        return MyUser.objects.all()

    def resolve_user(self, info, user_id):
        return MyUser.objects.get(id=user_id)

    def resolve_user_profile(self, info, user_id):
        return MyUserProfile.objects.prefetch_related('myuser').get(id=user_id)


class AuthenticationMutation(graphene.ObjectType):
    update_profile = UpdateProfile.Field()
    signup_user = CreateUser.Field()

    register = mutations.Register.Field()
    
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutation(AuthenticationMutation, graphene.ObjectType):
    pass
