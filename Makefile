.PHONY: setup run lint test clean help

help:
	@echo "Streamlit Quick App - Available command:"
	@echo "  make setup  - Install dependencies"
	@echo "  make run    - Launch app"
	@echo "  make lint   - Check the code"
	@echo "  make test   - Launch tests"
	@echo "  make clean  - Clean temporary files"

setup:
	uv sync
	@echo "✓ Dependencies installed"

run:
	uv run streamlit run src/app.py

run-port:
	uv run streamlit run src/app.py --server.port 8502

lint:
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/

lint-fix:
	uv run ruff check --fix src/ tests/
	uv run ruff format src/ tests/

test:
	uv run pytest tests/ -v

test-cov:
	uv run pytest tests/ -v --cov=src --cov-report=term-missing

refresh-data:
	uv run python scripts/refresh_data.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".streamlit" -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
