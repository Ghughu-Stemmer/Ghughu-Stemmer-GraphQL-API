import graphene

import stemmer.schema


class Query(stemmer.schema.Query, graphene.ObjectType):
    pass

class Mutation(stemmer.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
