# Tasks — project_setup

## Implementación

- [ ] T1 — Crear la estructura Python `app/` con las capas definidas. Cubre R5.
- [ ] T2 — Crear `pyproject.toml` con FastAPI, SQLAlchemy, Pydantic Settings, pytest, Ruff y mypy. Cubre R1, R6.
- [ ] T3 — Implementar configuración por variables de entorno y `.env.example`. Cubre R2.
- [ ] T4 — Crear `docker-compose.yml` con PostgreSQL, volumen y health check. Cubre R4.
- [ ] T5 — Configurar sesión SQLAlchemy y `DATABASE_URL` sin ejecutar conexiones durante la importación. Cubre R3.
- [ ] T6 — Crear endpoint `GET /health`. Cubre R1, R7.
- [ ] T7 — Crear prueba de health check y prueba de configuración. Cubre R2, R7.
- [ ] T8 — Configurar Alembic y crear una migración inicial reproducible. Cubre R9.
- [ ] T9 — Crear configuración aislada para pruebas y validar conexión a PostgreSQL de Docker. Cubre R8, R10.
- [ ] T10 — Documentar los comandos de Docker, migraciones, instalación, ejecución y verificación. Cubre R1, R4, R6, R9.

## Verificación

- [ ] T11 — Ejecutar Docker Compose, migraciones, Ruff, mypy y pytest y guardar la evidencia en `progress/impl_project_setup.md`. Cubre R4, R6, R7, R8, R9, R10.
