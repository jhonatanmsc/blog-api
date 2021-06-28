up:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload --no-use-colors

migrate:
	alembic upgrade head

migrations:
	alembic revision --autogenerate -m "$(m)"
