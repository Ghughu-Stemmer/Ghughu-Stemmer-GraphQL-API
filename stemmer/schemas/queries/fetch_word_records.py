import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


class FetchWordRecords(graphene.ObjectType):
    wordRecords = graphene.Field(
        graphene.List(WordRecordType),
        skip=graphene.Argument(graphene.Int, required=False),
        take=graphene.Argument(graphene.Int, required=False)
    )

    def resolve_wordRecords(self, _info, **kwargs):
        skip = kwargs.get('skip', 0)
        print(skip)

        result = None
        if 'take' in kwargs.keys():
            start, end = skip, skip + kwargs['take']
            result = WordRecord.objects.all()[start: end]
        else:
            start = skip
            result = WordRecord.objects.all()[start:]

        return result
