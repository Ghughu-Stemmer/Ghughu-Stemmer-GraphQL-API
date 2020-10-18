from graphene_django import DjangoObjectType

from stemmer.models import WordRecord


class WordRecordType(DjangoObjectType):
    class Meta:
        model = WordRecord
