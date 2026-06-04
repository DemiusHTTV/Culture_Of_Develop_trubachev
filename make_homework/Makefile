.PHONY: all venv install run typecheck lint format check-requirements check clean

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

all: check

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

venv: $(VENV)/bin/activate

install: venv

run: install
	$(PYTHON) src/app.py

typecheck: install
	$(PYTHON) -m mypy src

lint: install
	$(PYTHON) -m black --check src

format: install
	$(PYTHON) -m black src

check-requirements: install
	$(PYTHON) check_reqs.py src requirements.txt

check: typecheck check-requirements lint

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.mypy_cache' -delete
