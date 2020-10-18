import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


class AllWordRecords(graphene.ObjectType):
    allWordRecords = graphene.List(WordRecordType)

    def resolve_allWordRecords(self, _info, **kwargs):
        return WordRecord.objects.all()
