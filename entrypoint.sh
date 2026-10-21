#!/bin/sh
echo "==> Aplicando migraciones de Alembic..."
alembic upgrade head || echo "==> [AVISO] Base de datos no disponible en este momento. Continuando con el inicio de la API..."

echo "==> Iniciando API con Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
