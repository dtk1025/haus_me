setup:
	python3 -m venv ~/.haus_me

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=haus_me tests/*.py
	python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C haus_me

all: install lint test
