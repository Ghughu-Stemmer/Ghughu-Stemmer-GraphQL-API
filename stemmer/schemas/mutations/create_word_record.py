import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


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

    def mutate(self,
               _info,
               **kwargs
               ):
        if "inflectionalWord" not in kwargs:
            raise Exception("Inflectional word must be provided")

        inflectionalWord = kwargs["inflectionalWord"]

        wordRecord = WordRecord(
            **kwargs
        )

        duplicateWordRecord = WordRecord.objects.filter(
            inflectionalWord=inflectionalWord
        )

        if duplicateWordRecord.count() > 0:
            raise Exception(f"Duplicate word found for {inflectionalWord}!!!")
        else:
            wordRecord.save()

        return wordRecord
