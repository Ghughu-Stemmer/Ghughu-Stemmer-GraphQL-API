import graphene

from stemmer.models import WordRecord


class DeleteWordRecord(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, _root, _info, **kwargs):
        obj = WordRecord.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)
