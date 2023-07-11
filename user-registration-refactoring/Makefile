.PHONY: default docker-tests

default:
	@printf "$$HELP"

docker-build:
	docker build -t django-docker-bootstrap .

docker-tests:
	docker run --rm -v "${PWD}:/opt/project" django-docker-bootstrap python manage.py test test

define HELP
# Docker commands
        - make docker-build\tGenerate the docker image with Django installed
        - make docker-tests\t\tRun the tests
 Please execute "make <command>". Example make help

endef

export HELP