# AI Research Assistant

Starter scaffold for the AI Research Assistant API. The application is still under development.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Project Structure

- `app/` — application code, including the entry point, database, models, and schemas.
- `app/routers/` — API routes.
- `app/services/` — business logic.
- `tests/` — tests.

An ASGI application must be implemented in `app/main.py` before the project can be run.