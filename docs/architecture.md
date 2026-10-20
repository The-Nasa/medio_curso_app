# Arquitectura

- Lenguaje: Python 3.12+.
- API: FastAPI.
- Persistencia: PostgreSQL.
- ORM: SQLAlchemy 2 + Alembic.
- Validación: Pydantic.
- Autenticación: JWT y `pwdlib`/Argon2.
- Pruebas: pytest, pytest-cov y httpx.
- Calidad: Ruff, mypy y pre-commit.
- Automatización: GitHub Actions.

## Capas

```text
app/api          → endpoints HTTP
app/services     → reglas de negocio
app/repositories → acceso a datos
app/models       → modelos SQLAlchemy
app/schemas      → contratos Pydantic
tests/           → pruebas unitarias e integración
```

Los endpoints no acceden directamente a la base de datos. Las reglas de negocio viven en `services/`. Cada feature debe incluir pruebas y type hints.
