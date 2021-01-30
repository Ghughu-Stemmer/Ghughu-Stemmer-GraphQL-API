# Ghughu-Stemmer-GraphQL-API

This is a GraphQL API that handles data collection, accuracy testing and client interaction with Ghughu Stemmer

## How to Use

The project is created using Django and Graphene. All the necessary dependencies have been listed in the requirements.txt file. To start this project for the first time, you should create a virtual environment.

> Prerequisites
>
>- Python 3
>- MongoDB

### 1. Install the Python development environment on your system

Check if your Python environment is already configured:

```bash
python3 --version
pip3 --version
```

If these packages are already installed, skip to the next step. Otherwise, install [Python](https://www.python.org/), the [pip package manager](https://pip.pypa.io/en/stable/installing/), and [venv](https://docs.python.org/3/library/venv.html):

> The following snippet shows the installation commands for Ubuntu. You can install these in a similar way on windows or mac devices.

```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-venv
```

### 2. Create a virtual environment (recommended)

Python virtual environments are used to isolate package installation from the system. Open the terminal in the project directory and create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:

```bash
python3 -m venv --system-site-packages ./venv #Do this only once
```

Activate the virtual environment using a shell-specific command:

```bash
source ./venv/bin/activate  # sh, bash, or zsh

. ./venv/bin/activate.fish  # fish

source ./venv/bin/activate.csh  # csh or tcsh
```

When the virtual environment is active, your shell prompt is prefixed with (venv).

Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:

```bash
pip install --upgrade pip

pip list  # show packages installed within the virtual environment
```

And to exit the virtual environment later, use the `deactivate` command.

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment Variables

Setup the following environment Variables. They are quite self explanatory and you should have these info after you setup a mongodb cluster:

- MONGO_DB_CONNECTION_URL
- MONGO_DB_NAME (collection name)
- MONGO_DB_PORT
- MONGO_DB_USER
- MONGO_DB_PASSWORD

### 5. Run the server

```bash
python manage.py runserver
```

## Query and Mutations Example

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
