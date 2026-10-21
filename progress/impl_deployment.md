# Implementación: deployment

Estado: completada por Persona 2 (deployer).

Se implementó el empaquetado reproducible de la aplicación en Docker, la automatización de migraciones en arranque, los flujos de CI y Deploy en GitHub Actions integrando los secrets de EC2 (`EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY`), el endpoint y pruebas de health check (`/health`), y la documentación operativa completa.

Archivos creados / modificados:
- `Dockerfile`: Imagen reproducible basada en Python 3.12-slim con instalación de dependencias, código de app, Alembic y script de entrada.
- `.dockerignore`: Exclusión de entornos virtuales, cachés y archivos de configuración local.
- `entrypoint.sh`: Script de arranque que ejecuta `alembic upgrade head` y posteriormente `uvicorn app.main:app`.
- `.github/workflows/ci.yml`: Validación en CI con Ruff (lint y format check), mypy y pytest con cobertura.
- `.github/workflows/deploy.yml`: Validación previa obligatoria, compilación de imagen Docker y despliegue a instancia EC2 vía SSH con verificación de health check.
- `.env.example`: Plantilla de variables de entorno para desarrollo y producción sin secretos reales.
- `tests/test_health.py`: Pruebas unitarias y de integración HTTP para el endpoint `GET /health`.
- `docs/api-contract.md`: Registro del endpoint `GET /health` en el contrato de API.
- `docs/deployment.md`: Documentación completa de PostgreSQL de producción, secrets de GitHub Actions, health check, rollback y revisión de logs.
- `specs/deployment/tasks.md`: Marcado de las 10 tareas como completadas.

Trazabilidad:
- R1: Cubierto por `.env.example`, `.gitignore` y `docs/deployment.md` (T1).
- R2: Cubierto por `Dockerfile` y `.dockerignore` (T2).
- R3: Cubierto por `.github/workflows/ci.yml` (T3).
- R4: Cubierto por el job de build en `.github/workflows/ci.yml` y `deploy.yml` (T4).
- R5: Cubierto por `docs/deployment.md` (T5).
- R6: Cubierto por `entrypoint.sh` y `Dockerfile` (T6).
- R7: Cubierto por `app/api/health.py` y `tests/test_health.py` (T7).
- R8: Cubierto por el step de validación obligatoria en `.github/workflows/deploy.yml` (T8).
- R9: Cubierto por la comprobación post-despliegue en `deploy.yml` y `docs/deployment.md` (T9).
- R10: Cubierto por las secciones de rollback y consulta de logs en `docs/deployment.md` (T10).

Verificación: Ruff PASS, mypy PASS, pytest 29/29 PASS con 86.2% de cobertura.
