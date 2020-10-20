import json

import graphene

from stemmer import ghughu
from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


def findDuplicateRecords(wordRecords):
    inputWords = [record.inflectionalWord for record in wordRecords]
    return WordRecord.objects.filter(
        inflectionalWord__in=inputWords
    )


def removeDuplicateRecords(wordRecords):
    duplicateWords = [record.inflectionalWord for record in findDuplicateRecords(wordRecords)]
    wordRecords = filter(lambda record: record.inflectionalWord not in duplicateWords, wordRecords)

    return wordRecords


class CreateWordRecordBatch(graphene.Mutation):
    Output = graphene.List(WordRecordType)

    class Arguments:
        records = graphene.String()

    @classmethod
    def mutate(cls, _root, _info, records):
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
        ) for word in json.loads(records)]

        wordRecords = list(removeDuplicateRecords(wordRecords))

        for record in wordRecords:
            if record.isVerb:
                record.stemWord = ghughu.stem(record.inflectionalWord)

        WordRecord.objects.bulk_create(wordRecords)
        print(wordRecords)

        return list(findDuplicateRecords(wordRecords))
