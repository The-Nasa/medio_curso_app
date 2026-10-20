# Tasks — reservations

## Modelo y persistencia

- [x] T1 — Crear el modelo SQLAlchemy `Reservation` con usuario, horario, estado y fechas. Cubre R1, R5, R7.
- [x] T2 — Crear y ejecutar la migración Alembic de reservas. Cubre R1, R7.
- [x] T3 — Crear el repositorio para crear, consultar y cancelar reservas. Cubre R1, R4, R5.

## Reglas y API

- [x] T4 — Crear schemas Pydantic de creación y respuesta de reserva. Cubre R1, R4, R7.
- [x] T5 — Implementar servicio de creación con validación de autenticación, horario activo y horario libre. Cubre R1, R2, R3.
- [x] T6 — Implementar consulta filtrada por usuario autenticado. Cubre R4.
- [x] T7 — Implementar cancelación lógica y liberación del horario. Cubre R5, R7.
- [x] T8 — Rechazar cancelación de reservas de otro usuario. Cubre R6.
- [x] T9 — Crear endpoints para crear, listar y cancelar reservas. Cubre R1–R6.

## Pruebas y cierre

- [x] T10 — Crear pruebas unitarias de creación, disponibilidad, duplicados y cancelación. Cubre R1, R3, R5, R7.
- [x] T11 — Crear pruebas de integración de autenticación, consulta propia y permisos. Cubre R2, R4, R6, R8.
- [x] T12 — Ejecutar migraciones, Ruff, mypy y pytest; documentar `R<n> → test` en `progress/impl_reservations.md`. Cubre R8.
