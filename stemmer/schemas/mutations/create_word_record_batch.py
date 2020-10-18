import json

import graphene

from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


class CreateWordRecordBatch(graphene.Mutation):
    Output = graphene.List(WordRecordType)

    class Arguments:
        words = graphene.String()

    def mutate(self, info, words):
        wordRecords = [WordRecord(
            inflectionalWord=word.get("inflectionalWord", None),
            isVerb=word.get("isVerb", None),
            isLastWord=word.get("isLastWord", None),
            prefix=word.get("prefix", None),
            suffix=word.get("suffix", None),
            stemWord=word.get("stemWord", None),
            targetStemWord=word.get("targetStemWord", None),
            isAmbiguous=word.get("isAmbiguous", False),
            comment=word.get("comment", None)
        ) for word in json.loads(words)]

        WordRecord.objects.bulk_create(wordRecords)

        inputWords = [record.inflectionalWord for record in wordRecords]

        savedWordRecords = WordRecord.objects.filter(
            inflectionalWord__in=inputWords
        )

        return savedWordRecords
