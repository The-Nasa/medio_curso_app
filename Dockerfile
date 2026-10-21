FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del proyecto
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copiar configuración de base de datos, migraciones y código de aplicación
COPY alembic.ini .
COPY alembic ./alembic
COPY app ./app
COPY entrypoint.sh .

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["sh", "/app/entrypoint.sh"]
