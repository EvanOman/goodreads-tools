## Goodreads CLI (unofficial)

This project aims to provide a modern, scriptable Goodreads command-line client powered by `uv` and Python. The official Goodreads API is no longer issuing keys, so the tool relies on scraping publicly available endpoints plus authenticated requests made with the user’s existing browser session.

### Current status

- Research on available endpoints, scraping strategies, and prior art lives in [`docs/RESEARCH.md`](docs/RESEARCH.md).
- The implementation roadmap (phased plan, architecture, and near-term tasks) is tracked in [`docs/PLAN.md`](docs/PLAN.md).
- Milestones and testable deliverables are listed in [`docs/MILESTONES.md`](docs/MILESTONES.md).
- A `typer`-based CLI and supporting modules will live under `src/goodreads_cli/`.

### Development

```bash
# create / activate the project environment
uv sync

# run the dev CLI (placeholder command for now)
uv run goodreads-cli

# search titles
uv run goodreads-cli search "Dune" -n 5

# fetch a book by id or url
uv run goodreads-cli book show 44767458

# list a public shelf via RSS
uv run goodreads-cli shelf list --user 1 --shelf all -n 5

# export a shelf to JSON or CSV
uv run goodreads-cli shelf export --user 1 --shelf all --format json

# store cookies from browser or manual cookie string
uv run goodreads-cli login --browser chrome
uv run goodreads-cli login --cookie-string "_session_id2=...; ccsid=...; locale=en"

# show the current authenticated user
uv run goodreads-cli whoami

# validate session + csrf extraction
uv run goodreads-cli auth check

# run unit tests
uv run pytest

# run live tests (network)
GOODREADS_LIVE=1 uv run pytest -m live

# run live auth test (requires a valid cookie string)
GOODREADS_LIVE=1 GOODREADS_COOKIE="_session_id2=...; ccsid=...; locale=en" uv run pytest -m live -k whoami

# run live csrf test (requires the same cookie string)
GOODREADS_LIVE=1 GOODREADS_COOKIE="_session_id2=...; ccsid=...; locale=en" uv run pytest -m live -k csrf

# justfile helpers (lint/type/test)
just lint
just type
just test
```

The project targets Python 3.13 (via `.python-version`). Use `uv` for dependency management and execution.
