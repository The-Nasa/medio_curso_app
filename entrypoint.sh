#!/bin/sh
set -e

echo "==> Aplicando migraciones de Alembic..."
alembic upgrade head

echo "==> Iniciando API con Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
