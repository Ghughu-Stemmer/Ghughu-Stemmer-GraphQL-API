import json

import graphene
import cytoolz

from stemmer import ghughu
from stemmer.models import WordRecord
from stemmer.schemas.types import WordRecordType


def findDuplicateRecords(wordRecords):
    inputWords = [record.inflectionalWord for record in wordRecords]
    return WordRecord.objects.filter(
        inflectionalWord__in=inputWords
    )


def removeDuplicateRecords(wordRecords):
    duplicateWords = [
        record.inflectionalWord
        for record in findDuplicateRecords(wordRecords)
    ]

    wordRecords = filter(
        lambda record: record.inflectionalWord not in duplicateWords,
        wordRecords
    )

    return wordRecords


class CreateWordRecordBatch(graphene.Mutation):
    Output = graphene.List(WordRecordType)

    class Arguments:
        records = graphene.String()

    @classmethod
    def mutate(cls, _root, _info, records):
        wordRecords = [WordRecord(
            inflectionalWord=word.get(
                "word", word.get('inflectionalWord', None)),
            isVerb=word.get("is-verb", word.get('isVerb', None)),
            isLastWord=word.get("last-word", word.get('islastWord', False)),
            prefix=word.get("prefix", None),
            suffix=word.get("suffix", None),
            stemWord=word.get("stem-word", word.get('stemWord', None)),
            targetStemWord=word.get(
                "target-stem-word", word.get('targetStemWord', None)),
            isAmbiguous=word.get(
                "is-ambiguous", word.get('isAmbiguous', False)),
            comment=word.get("comment", None)
        ) for word in json.loads(records)]

        wordRecords = list(removeDuplicateRecords(wordRecords))

        wordRecords = list(cytoolz.unique(
            wordRecords,
            key=lambda wordRecord: wordRecord.inflectionalWord
        ))

        for record in wordRecords:
            if record.isVerb:
                record.stemWord = ghughu.stem(record.inflectionalWord)

        WordRecord.objects.bulk_create(wordRecords)

        return list(findDuplicateRecords(wordRecords))
