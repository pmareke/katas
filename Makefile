.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: install
install: ## Install all dependencies
	poetry install

.PHONY: update
update: ## Update dependencies
	poetry update

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-format
check-format:
	poetry run yapf --recursive **/*.py

.PHONY: check-style
check-style:
	poetry run flake8 .
	poetry run pylint ./*

.PHONY: reformat
reformat:  ## Format python code
	poetry run yapf --in-place --recursive **/*.py

.PHONY: test
test: ## Run all available tests
	PYTHONPATH=. poetry run pytest -n auto
	PYTHONPATH=. poetry run mamba .

.PHONY: watch
watch: ## Run all available tests
	PYTHONPATH=. poetry run ptw --onpass "notify-send 'All tests passed, keep working!'" --onfail "notify-send -u critical 'Some test failed, please take a look.'" -p -- --testmon

.PHONY: bank
bank: ## Run bank kata
	PYTHONPATH=. poetry run python bank/main.py

.PHONY: ohce
ohce: ## Run ohce kata
	PYTHONPATH=. poetry run python ohce/main.py Pedro

.PHONY: coffee-machine
coffee-machine: ## Run coffee machine
	PYTHONPATH=. poetry run python coffee_machine/main.py

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test
