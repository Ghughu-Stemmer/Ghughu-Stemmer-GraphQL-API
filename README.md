# Ghughu-Stemmer-GraphQL-API
This is a GraphQL API that handles data collection, accuracy testing and client interaction with Ghughu Stemmer


**Query and Mutations Example**

```graphql
#View All Words
query {
  allWordRecords {
    id
    inflectionalWord
    isVerb
    stemWord
    targetStemWord
  }
}

#Create New Word Record
mutation {
  addWord: createWordRecord(
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

#Create A Bunch of Word Records
mutation {
  addWords: createWordRecordBatch(
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

#Update Word Record
mutation {
  updateWord: updateWordRecord(
    id: 15
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

```
