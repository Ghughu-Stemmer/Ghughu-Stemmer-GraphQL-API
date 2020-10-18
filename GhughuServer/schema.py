import graphene

import stemmer.schema


class Query(stemmer.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)