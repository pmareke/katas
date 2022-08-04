.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test: ## run tests
	pytest tests/

.PHONY: fixtures
fixtures: ## run fixtures
	python3 fixtures/texttest_fixture.py

.PHONY: check-typing
check-typing: ## check types
	mypy .

.PHONY: check-format
check-format: ## check format
	black --check .

.PHONY: format
format: ## format
	black .