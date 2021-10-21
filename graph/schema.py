import graphene
from api.schemas.base import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
