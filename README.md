# Identity Service
A simple identity service written in python (3.7 compatible) which keeps its state in the memory and is able to save/load its state to/from a file and a Command Line Interface (CLI) that can be used to register a new user and authenticate an existing user.

## Installation
from source using setuptools:
```
pip3 install .
```

## CLI
Basic usage:
```
# identityservice --version
identityservice, version 0.1

# identityservice --help
Usage: identityservice [OPTIONS] COMMAND [ARGS]...

  Simple CLI for registering and authenticating users

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  authenticate  Registers users.
  register      Registers users.
```

Register and authenticate:
```
# identityservice register marek parek '{ "greeting": "cusky fusky", "hobbies": ["bike", "kubernetes", "cloud native"]}'
User registered. Database stored in users.json

# cat users.json| jq '.'
{
  "identities": [
    {
      "username": "marek",
      "password": "parek",
      "properties": {
        "greeting": "cusky fusky",
        "hobbies": [
          "bike",
          "kubernetes",
          "cloud native"
        ]
      }
    }
  ]
}

# identityservice authenticate marek klobasa
User verification failed.

# identityservice authenticate marek parek
User verified.

# identityservice authenticate --file newdb.json marek parek
User verification failed.

# identityservice register --file newdb.json michal 12345
User registered. Database stored in newdb.json
```