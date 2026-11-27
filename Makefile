.DEFAULT_GOAL := help
.PHONY: help setup lint test check clean

VENV := .venv
PY   := $(VENV)/bin/python

help: ## Vis alle targets
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-8s %s\n", $$1, $$2}'

# Det virtuelle miljø oprettes automatisk første gang, og igen hvis requirements ændres.
$(PY): requirements-dev.txt
	python3 -m venv $(VENV)
	$(PY) -m pip install --quiet -r requirements-dev.txt
	touch $(PY)

setup: $(PY) ## Opret virtuelt miljø og installér værktøjer

lint: $(PY) ## Tjek kodestil med ruff
	$(PY) -m ruff check .

test: $(PY) ## Kør tests med pytest
	$(PY) -m pytest -q

check: lint test ## Er det grønt? Kører lint og test

clean: ## Slet virtuelt miljø og cache
	rm -rf $(VENV) .pytest_cache .ruff_cache __pycache__
