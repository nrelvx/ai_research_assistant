# Repository Guidance

## Current Project State

- Application code lives under `app/`.
- The current modules are `app/main.py`, `app/database.py`, `app/models.py`, and `app/schemas.py`.
- Route modules belong in `app/routers/`; service modules belong in `app/services/`.
- These modules and directories are currently empty. No framework or application behavior is established yet.
- Runtime dependencies are listed in `requirements.txt` (`fastapi` and `uvicorn[standard]`). No test suite or lint/type-check configuration is established yet.

## Working in This Repository

- Keep application code within `app/` and follow the existing module boundaries as they become defined.
- Create the environment with `python -m venv .venv`, activate it, then install dependencies with `pip install -r requirements.txt`.
- Prefer focused changes and add tests alongside new behavior once a test framework is established.
- Before reporting validation, run only checks that are configured in the repository and describe any unavailable checks.
- Update this guidance when project structure, setup commands, or development conventions are established.