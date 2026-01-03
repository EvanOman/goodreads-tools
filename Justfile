set shell := ["zsh", "-cu"]

fmt:
    uv run ruff format .

lint:
    uv run ruff check .

lint-fix:
    uv run ruff check . --fix

type:
    uv run ty check .

test:
    uv run pytest

test-live:
    GOODREADS_LIVE=1 uv run pytest -m live

ci: lint type test
