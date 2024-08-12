## Description

This is a CLI version of Tic-Tac-Toe written in Python. 

Future tasks:
- increase test coverage, add test for GameDriver
- update game to accept either two human users or one human and one computer
- terminate game early when no one can win
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
python3 cli/game_driver.py
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

testing, from home directory:
```
python3 -m unittest discover
python3 -m unittest tests/test_user.py
coverage run -m unittest discover
coverage report
coverage html
```
