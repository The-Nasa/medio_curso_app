# Tasks — auth

## Modelo y persistencia

- [x] T1 — Crear el modelo SQLAlchemy `User` con id, nombre, correo, hash de contraseña, rol y fechas. Cubre R1, R3, R6.
- [x] T2 — Crear y ejecutar la migración Alembic de usuarios. Cubre R1, R2, R6.
- [x] T3 — Crear el repositorio para buscar usuarios por correo y guardar usuarios. Cubre R1, R2.

## Seguridad y lógica de negocio

- [x] T4 — Configurar hash y verificación de contraseñas con Argon2. Cubre R3, R5.
- [x] T5 — Implementar creación y validación de tokens JWT. Cubre R4, R6, R7.
- [x] T6 — Implementar el servicio de registro con validación de correo duplicado. Cubre R1, R2, R3.
- [x] T7 — Implementar el servicio de login sin revelar cuál credencial falló. Cubre R4, R5.

## API y autorización

- [x] T8 — Crear schemas Pydantic de registro, login y respuesta de autenticación. Cubre R1, R4, R5.
- [x] T9 — Crear `POST /api/auth/register` y `POST /api/auth/login`. Cubre R1, R2, R4, R5.
- [x] T10 — Crear dependencia para obtener el usuario autenticado y su rol. Cubre R6, R7.

## Pruebas y cierre

- [x] T11 — Crear pruebas unitarias de hash, JWT y servicios. Cubre R3, R4, R5, R6, R7.
- [x] T12 — Crear pruebas de integración de registro, login, duplicados y token inválido. Cubre R1, R2, R4, R5, R8.
- [x] T13 — Ejecutar migraciones, Ruff, mypy y pytest; documentar `R<n> → test` en `progress/impl_auth.md`. Cubre R8.
