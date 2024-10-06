ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

# Manually define main variables

ifndef APP_PORT
override APP_PORT = 8080
endif

ifndef APP_HOST
override APP_HOST = 127.0.0.1
endif

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
MESSAGE = "Done"
endif

ROOT=`echo $(PWD)`

TEST = poetry run python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG
CODE = $(APPLICATION_NAME) tests
DOCKER_RUN = docker run -p 8000:8000 -it --env-file .env $(APPLICATION_NAME)

HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \

# Commands
env:  ##@Environment Create .env file with variables
	@$(eval SHELL:=/bin/bash)
	@cp .env.example .env
	@echo "SECRET_KEY=$$(openssl rand -hex 32)" >> .env



run:
	python -m bot

lint:
	mypy ./bot
	isort ./bot
	ruff check ./bot --fix


# DOCKER

db:
	docker compose -f docker-compose.yml up db -d

#docker-build:
#	docker compose -f docker-compose.prod.yml build $(args)
#
#docker-dev:
#	docker compose -f docker-compose.dev.yml up -d --remove-orphans
#
#docker-run:
#	docker compose -f docker-compose.prod.yml up -d --remove-orphans

revision:
	alembic revision --autogenerate -m $(args)

migrate:
	alembic upgrade $(args)

migrate-downgrade:
	alembic downgrade -1
