# Tasks — deployment

## Tareas derivadas de `feature_list.json`

- [x] T1 — Configurar y documentar las variables de entorno necesarias con plantilla `.env.example`, garantizando que ningún secreto se guarde en el repositorio. Cubre R1.
- [x] T2 — Crear el `Dockerfile` reproducible y optimizado para la API junto con su archivo `.dockerignore`. Cubre R2.
- [x] T3 — Crear el workflow de GitHub Actions para CI que ejecute validaciones de Ruff, mypy y pytest. Cubre R3 y R8.
- [x] T4 — Crear el workflow de GitHub Actions para construir y verificar la imagen Docker de la API. Cubre R4.
- [x] T5 — Documentar la configuración y parámetros requeridos para la base de datos PostgreSQL de producción en `docs/deployment.md`. Cubre R5.
- [x] T6 — Implementar el script o comando de arranque para ejecutar automáticamente `alembic upgrade head` antes de iniciar la API. Cubre R6.
- [x] T7 — Implementar el endpoint de health check (`GET /health`) y añadir sus pruebas automatizadas en `tests/`. Cubre R7.
- [x] T8 — Configurar el workflow de despliegue para condicionar cualquier publicación a la aprobación previa de las pruebas automatizadas. Cubre R8.
- [x] T9 — Validar y documentar la verificación de disponibilidad a través de la URL desplegada mediante el health check. Cubre R9.
- [x] T10 — Redactar en `docs/deployment.md` los procedimientos operativos de rollback ante fallos y de consulta de logs. Cubre R10.
