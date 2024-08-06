## Description

This is a CLI version of Tic-Tac-Toe written in Python. 

Future tasks:
- unit tests
- reorganize classes to separate files
- update game to accept either two human users or one human and one computer
- add ability to play game repeatedly
- add computer levels that are smarter
- build backend game and front end UI with websockets
- cache number of wins/losses in current session and show on UI
- create backend database for storing all users and their
number of wins and loses over time to show a leadboard on the UI

## Requirements
- python3
- pip3

## Set-Up

### 1. Clone the repo
### 2. At the top-level directory, create a virtual environment, activate it, and install requirements needed.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

### 3. Start the CLI game.
```
python3 cli.py
```

### 4. To deactivate the virtual environment.
```
deactivate
```

## Useful commands

List the packages installed in the virtual environment.
```
pip3 list
```

linting:
```
pylint cli.py
```