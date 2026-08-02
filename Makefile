.PHONY: install test test-coverage lint

install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

lint:
	uv run ruff check