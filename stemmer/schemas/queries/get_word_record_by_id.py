import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


class WordRecordById(graphene.ObjectType):
    wordRecordById = graphene.Field(WordRecordType, id=graphene.ID())

    def resolve_wordRecordById(self, _info, **kwargs):
        id_ = kwargs['id']
        return WordRecord.objects.get(id=id_)
