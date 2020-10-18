import graphene
from graphene_django import DjangoObjectType

from .models import WordRecord


class WordRecordType(DjangoObjectType):
    class Meta:
        model = WordRecord


class Query(graphene.ObjectType):
    allWordRecords = graphene.List(WordRecordType)

    def resolve_allWordRecords(self, _info, **kwargs):
        return WordRecord.objects.all()


class CreateWordRecord(graphene.Mutation):
    Output = WordRecordType

    class Arguments:
        inflectionalWord = graphene.Argument(graphene.String, required=True)
        isVerb = graphene.Boolean()
        isLastWord = graphene.Boolean()
        prefix = graphene.String()
        suffix = graphene.String()
        stemWord = graphene.String()
        targetStemWord = graphene.String()
        isAmbiguous = graphene.Boolean()
        comment = graphene.String()

    def mutate(self, info, inflectionalWord, isVerb=None, isLastWord=False, prefix=None, suffix=None, stemWord=None,
               targetStemWord=None, isAmbiguous=False, comment=None):
        user = info.context.user
        print(user)

        wordRecord = WordRecord(
            inflectionalWord=inflectionalWord,
            isVerb=isVerb,
            isLastWord=isLastWord,
            prefix=prefix,
            suffix=suffix,
            stemWord=stemWord,
            targetStemWord=targetStemWord,
            isAmbiguous=isAmbiguous,
            comment=comment
        )

        duplicateWordRecord = WordRecord.objects.filter(
            inflectionalWord=inflectionalWord
        )

        if duplicateWordRecord.count() > 0:
            raise Exception("Duplicate Word Found!!!")
        else:
            wordRecord.save()

        return wordRecord


class Mutation(graphene.ObjectType):
    create_word_record = CreateWordRecord.Field()
