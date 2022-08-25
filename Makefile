.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	mypy .

.PHONY: check-format
check-format:
	black --check .

.PHONY: check-style
check-style:
	flake8 .

.PHONY: reformat
reformat:  ## Format python code
	black .

.PHONY: test
test: ## Run all available tests
	pytest .

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test
