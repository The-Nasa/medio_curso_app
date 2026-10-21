# Design — deployment

## Responsable

Persona 2 (con soporte y revisión de Persona 1).

## Alcance

Preparar, empaquetar, validar y desplegar la API FastAPI y la base de datos PostgreSQL utilizando contenedores Docker, workflows de GitHub Actions y migraciones automáticas con Alembic, garantizando la seguridad de secretos y la observabilidad básica mediante health checks y documentación operativa.

## Tecnologías y componentes

1. **Docker**:
   - `Dockerfile` con Python 3.12-slim, reproducible y de mínimos privilegios.
   - `.dockerignore` para excluir entornos virtuales (`.venv`), cachés (`__pycache__`, `.pytest_cache`, `.mypy_cache`), archivos locales (`.env`) y documentación innecesaria.
   - Script de entrada (`entrypoint.sh` o comando de ejecución) que aplica `alembic upgrade head` antes de iniciar `uvicorn`.

2. **GitHub Actions**:
   - `.github/workflows/ci.yml`: Ejecución automática en ramas y PRs de `ruff check`, `ruff format --check`, `mypy` y `pytest`.
   - `.github/workflows/deploy.yml` (o `docker-build.yml`): Construcción y validación de la imagen Docker condicionado a la aprobación de pruebas (CI verde). Uso estricto de GitHub Actions Secrets para credenciales.

3. **PostgreSQL de producción**:
   - Especificación de variables de entorno para la base de datos de producción (`DATABASE_URL`, pooling y timeouts).
   - Documentación de aprovisionamiento y conexión en `docs/deployment.md`.

4. **Health Check y Monitoreo**:
   - Endpoint `GET /health` en FastAPI sin requerimiento de autenticación, que valide el estado de la aplicación.
   - Documentación de pruebas post-despliegue consultando la URL desplegada.

5. **Documentación Operativa**:
   - `docs/deployment.md`: Guía de despliegue, configuración de secretos, procedimiento de rollback paso a paso e instrucciones para consulta de logs.

## Archivos previstos (para la fase de implementación)

```text
Dockerfile
.dockerignore
entrypoint.sh
app/api/health.py
.github/workflows/ci.yml
.github/workflows/docker-build.yml
docs/deployment.md
tests/test_health.py
```

## Decisiones técnicas

- **Gestión de Secretos**: No se almacena ninguna variable sensible en el repositorio ni en las imágenes Docker. Se utiliza `.env.example` como plantilla y GitHub Actions Secrets para entornos CI/CD.
- **Automatización de Migraciones**: Las migraciones de base de datos se ejecutan de manera determinista mediante `alembic upgrade head` en el paso de inicio previo al levantamiento del servidor HTTP.
- **Health Check ligero**: Endpoint `/health` expuesto en la raíz o router base para balanceadores y monitores de servicio, respondiendo código HTTP 200 con `{"status": "ok"}`.
- **Pipeline de Despliegue**: El flujo de despliegue depende obligatoriamente del éxito de la suite de pruebas unitarias y de integración.

## Alternativas descartadas

- **Terraform / IaC complejo**: Descartado de forma explícita para mantener la arquitectura ágil, estandarizada con Docker y GitHub Actions sin sobrecarga de infraestructura innecesaria.
- **Herramientas o scripts no estandarizados**: Descartado el uso de cualquier herramienta ajena al stack acordado (Docker, GitHub Actions, PostgreSQL, Alembic).
