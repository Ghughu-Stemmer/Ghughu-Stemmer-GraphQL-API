import graphene

from stemmer.models import WordRecord


class DeleteWordRecord(graphene.Mutation):
    rowsDeleted = graphene.Int()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, _root, _info, **kwargs):
        deleted, _rows_count = WordRecord.objects.get(pk=kwargs["id"]).delete()

        return cls(rowsDeleted=deleted)
