# DOCKER COMPOSE COMMANDS

shutdown:
	@echo "Shutting down..."
	docker-compose down

startup:
	docker-compose --profile kafka --profile db up -d


startup_kafman: shutdown
	docker-compose up --profile kafka up


# POETRY COMMANDS

.PHONY: install
pinstall:
	poetry install

.PHONY: build
pbuild: install
	poetry build

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --without-hashes -o requirements.txt

.PHONY: black
black:
	poetry run black .

.PHONY: pytest
pytest:
	poetry run pytest --cov=./tests --black -rAP 

.PHONY:black
black:
	isort


# DOCKER COMMANDS


CONTAINER_NAME=alembic
PROJECT_ID=kavi-prod-data-lab-4943

.PHONY: build
build:
	docker build -f Dockerfile.alembic -t gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME) .

.PHONY: run
run:
	docker run -it --network="app_network" --name ${CONTAINER_NAME} gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME) upgrade head