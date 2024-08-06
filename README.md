## Set-Up

Requirements:
- python3
- pip3

1. Clone the repo
2. At the top-level directory, create a virtual environment, activate it, and install requirements needed.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
Useful commands:

List the packages installed in the virtual environment.
```
pip3 list
```

linting:
```
pylint cli.py
```

3. Start the CLI game.
```
python3 cli.py
```

4. To deactivate the virtual environment.
```
deactivate
```