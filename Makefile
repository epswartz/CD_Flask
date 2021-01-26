run:
	python main.py

venv_fish:
	python -m venv .venv
	source .venv/bin/activate.fish

venv:
	python -m venv .venv
	source .venv/bin/activate

install: venv
	pip install -r requirements.txt
