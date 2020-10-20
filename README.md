# Ghughu-Stemmer-GraphQL-API
This is a GraphQL API that handles data collection, accuracy testing and client interaction with Ghughu Stemmer


**Query and Mutations Example**

```graphql
# View All Words
query showAllWords {
  wordRecords {
    id
    inflectionalWord
    isVerb
    stemWord
    targetStemWord
  }
}

# Skip 1 record and take next 2
query showWordsInRange {
  wordRecords(skip: 1, take: 2) {
    id
    inflectionalWord
    isVerb
    stemWord
    targetStemWord
  }
}

# View Word Record By ID
query getWordById {
  wordRecordById(id: 37) {
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

# Create New Word Record
mutation addWord {
  createWordRecord(
    inflectionalWord: "নিয়ে"
    isLastWord: false
    isVerb: true
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
mutation addManyWords {
  createWordRecordBatch(
    records: "[{\"inflectionalWord\": \"দিয়েছি\", \"isLastWord\": false, \"isVerb\": true,\"targetStemWord\": \"দেওয়া\",\"isAmbiguous\": false }, {\"inflectionalWord\": \"দিচ্ছি\",\"isLastWord\": false,\"isVerb\": true,\"targetStemWord\": \"দেওয়া\",\"isAmbiguous\": false}]"
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
mutation updateWord {
  updateWordRecord(
    id: 37
    inflectionalWord: "নিয়া"
    isLastWord: false
    isVerb: true
    stemWord: "KJ"
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
  deleteWordRecord(id: 34) {
    rowsDeleted
  }
}

# Delete Multiple Word Records
mutation deleteWords {
  deleteWordRecordBatch(ids: [34, 35, 36]) {
    rowsDeleted
  }
}
```
