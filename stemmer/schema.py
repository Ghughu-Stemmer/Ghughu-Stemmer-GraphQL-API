import graphene
from graphene_django import DjangoObjectType

from .models import WordRecord


class WordRecordType(DjangoObjectType):
    class Meta:
        model = WordRecord


class Query(graphene.ObjectType):
    wordRecords = graphene.List(WordRecordType)

    def resolve_wordRecords(self, info, **kwargs):
        return WordRecord.objects.all()