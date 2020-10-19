# Ghughu-Stemmer-GraphQL-API
This is a GraphQL API that handles data collection, accuracy testing and client interaction with Ghughu Stemmer


**Query and Mutations Example**

```graphql
# View All Words
query showAllWords{
  allWordRecords {
    id
    inflectionalWord
    isVerb
    stemWord
    targetStemWord
  }
}

# Create New Word Record
mutation addWord{
  createWordRecord(
    inflectionalWord: "নিয়ে"
    isLastWord: false
    isVerb: true
    stemWord: "নেওয়া"
    targetStemWord: "নেওয়া"
  ) {
    id
    inflectionalWord
    isLastWord
    isVerb
    prefix
    suffix
    stemWord
    targetStemWord
    isAmbiguous
    comment
  }
}

# Create A Bunch of Word Records
mutation addManyWords{
  createWordRecordBatch(
    records: "[{\"inflectionalWord\": \"দিয়েছি\", \"isLastWord\": false, \"isVerb\": true,\"stemWord\": \"দেওয়া\",\"targetStemWord\": \"দেওয়া\",\"isAmbiguous\": false }, {\"inflectionalWord\": \"দিচ্ছি\",\"isLastWord\": false,\"isVerb\": true,\"stemWord\": \"দেওয়া\",\"targetStemWord\": \"দেওয়া\",\"isAmbiguous\": false}]"
  ) {
    id
    inflectionalWord
    isLastWord
    isVerb
    prefix
    suffix
    stemWord
    targetStemWord
    isAmbiguous
    comment
  }
}

# Update Word Record
mutation updateWordRecord {
  updateWordRecord(
    id: 20
    inflectionalWord: "নিয়া"
    isLastWord: false
    # isVerb: true
    # stemWord: "নেওয়া"
    # targetStemWord: "নেওয়া"
  ) {
    id
    inflectionalWord
    isLastWord
    isVerb
    prefix
    suffix
    stemWord
    targetStemWord
    isAmbiguous
    comment
  }
}

# Delete Word Record
mutation deleteWord {
  deleteWordRecord(id:31) {
    rowsDeleted
  }
}

# Delete Multiple Word Records
mutation deleteWords {
  deleteWordRecordBatch(ids:[32, 33]) {
    rowsDeleted
  }
}
```
