import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


def findDuplicateRecords(wordRecords):
    inputWords = [record.inflectionalWord for record in wordRecords]
    return WordRecord.objects.filter(
        inflectionalWord__in=inputWords
    )


class UpdateWordRecord(graphene.Mutation):
    Output = WordRecordType

    class Arguments:
        id = graphene.Argument(graphene.Int, required=True)
        inflectionalWord = graphene.Argument(graphene.String, required=True)
        isVerb = graphene.Boolean()
        isLastWord = graphene.Boolean()
        prefix = graphene.String()
        suffix = graphene.String()
        stemWord = graphene.String()
        targetStemWord = graphene.String()
        isAmbiguous = graphene.Boolean()
        comment = graphene.String()

    @classmethod
    def mutate(cls, _root, _info, **kwargs):
        id_ = kwargs['id']

        inflectionalWord = kwargs["inflectionalWord"]
        conflictingDuplicateCount = WordRecord.objects.filter(inflectionalWord=inflectionalWord).exclude(id=id_).count()

        if conflictingDuplicateCount > 0:
            raise Exception("There is another record in the database with same inflectional word but different ID")
        else:
            WordRecord.objects.filter(id=id_).update(
                **kwargs
            )

        return WordRecord.objects.get(id=id_)
