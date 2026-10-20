# Design — project_setup

## Alcance

Feature compartida por ambas personas. Prepara la base sobre la que se implementarán autenticación, horarios y reservas.

## Archivos previstos

```text
app/main.py
app/core/config.py
app/db/session.py
app/api/health.py
tests/test_health.py
pyproject.toml
.env.example
```

## Decisiones

- FastAPI será el punto de entrada HTTP.
- Pydantic Settings leerá la configuración desde el entorno.
- SQLAlchemy 2 será la capa de persistencia.
- La prueba inicial usará una aplicación de prueba y no datos reales.
- Ruff y mypy se configurarán en `pyproject.toml`.

## Alternativa descartada

Se descarta empezar con acceso directo a PostgreSQL desde los endpoints porque mezclaría transporte, configuración y persistencia, dificultando las pruebas y las futuras features.
