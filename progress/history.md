# Historial

- Entorno inicial creado para dos personas: autenticación y reservas.
- `project_setup` implementado, verificado y aprobado. PostgreSQL funciona con Docker en el puerto local 5433.
- `auth` implementado, verificado y aprobado. Registro, login, Argon2 y JWT funcionan.
- `availability` implementado, verificado y aprobado. Gestión de horarios por administradores, validaciones de solapamiento/fechas, endpoints y pruebas completadas.
- `reservations` implementado, verificado y aprobado. Creación, consulta de reservas por cliente y cancelación con liberación de horarios.
- `integration` implementado, verificado y aprobado. Flujo integral cliente-administrador verificado sin errores.
- `deployment` implementado, verificado y aprobado. Contenedorización reproducible con Docker, migraciones automáticas en arranque con Alembic, workflows de CI y Deploy en GitHub Actions con secrets de AWS EC2 (`EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY`), endpoint y pruebas de health check (`/health`), y documentación operativa completa.
