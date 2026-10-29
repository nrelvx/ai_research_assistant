# AI Research Assistant

Начальный каркас API-сервиса для AI Research Assistant. Приложение пока находится в разработке.

## Установка

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Структура

- `app/` — код приложения: точка входа, работа с базой данных, модели и схемы.
- `app/routers/` — API-маршруты.
- `app/services/` — бизнес-логика.
- `tests/` — тесты.

Для запуска приложения потребуется реализовать ASGI-приложение в `app/main.py`.