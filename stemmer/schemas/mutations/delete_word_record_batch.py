import graphene

from stemmer.models import WordRecord


class DeleteWordRecordBatch(graphene.Mutation):
    rowsDeleted = graphene.Int()

    class Arguments:
        ids = graphene.List(graphene.ID)

    @classmethod
    def mutate(cls, _root, _info, **kwargs):
        deleted, _rows_count = WordRecord.objects.filter(id__in=kwargs["ids"]).delete()
        return cls(rowsDeleted=deleted)
