test:
	python -m pytest -vv .

lint:
	pylint --disable=R,C application.py

run:
	python application.py

install:
	pip install --upgrade pip
	pip install -r requirements.txt

all: install lint test
