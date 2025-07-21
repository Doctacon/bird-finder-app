# Bird Finder App - Development Makefile

.PHONY: help install install-dev test lint format clean docs

help: ## Show this help message
	@echo "Bird Finder App - Development Commands"
	@echo "======================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies
	uv sync

install-dev: ## Install project with development dependencies
	uv sync --dev
	uv run pre-commit install

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=bird_finder --cov-report=term-missing --cov-report=html

lint: ## Run all linting tools
	uv run ruff check

format: ## Format code with ruff
	uv run ruff check --fix
	uv run ruff format

pre-commit: ## Run pre-commit hooks
	uv run pre-commit run --all-files

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	uv build

dagster: ## Run Dagster
	uv run dagster dev

docs: ## Generate documentation
	@echo "Documentation generation not yet implemented"

pipeline-full: pipeline-ingest pipeline-staging pipeline-transform ## Run full data pipeline

# Development workflow
dev-setup: install-dev ## Complete development setup
	@echo "Development environment setup complete!"
	@echo "Run 'make help' to see available commands"

check: lint test ## Run all checks (lint + test) 