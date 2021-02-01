test:
	python -m pytest -vv .

lint:
	pylint --disable=R,C application.py

run:
	python application.py

venv_fish:
	python3 -m venv .venv
	source .venv/bin/activate.fish

venv:
	python3 -m venv .venv
	source .venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt

all: venv_fish install lint
