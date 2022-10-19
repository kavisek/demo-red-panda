# DOCKER COMPOSE COMMANDS

shutdown:
	@echo "Shutting down..."
	docker-compose down

startup:
	docker-compose --profile kafka --profile db up -d


startup_kafka: shutdown
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