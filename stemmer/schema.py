import graphene

from .schemas.mutations import CreateWordRecord, CreateWordRecordBatch, UpdateWordRecord, DeleteWordRecord
from .schemas.queries import AllWordRecords


class Query(AllWordRecords, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_word_record = CreateWordRecord.Field()
    create_word_record_batch = CreateWordRecordBatch.Field()
    update_word_record = UpdateWordRecord.Field()
    delete_word_record = DeleteWordRecord.Field()