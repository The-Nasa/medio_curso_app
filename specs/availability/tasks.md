# Tasks — availability

## Modelo y persistencia

- [ ] T1 — Crear el modelo SQLAlchemy `Availability` con fecha, hora de inicio, hora de fin y estado. Cubre R1, R5, R6.
- [ ] T2 — Crear y ejecutar la migración Alembic de horarios. Cubre R1, R4, R6.
- [ ] T3 — Crear el repositorio para consultar, crear y desactivar horarios. Cubre R1, R5, R6.

## Reglas y API

- [ ] T4 — Crear schemas Pydantic de horario y disponibilidad. Cubre R1, R5.
- [ ] T5 — Implementar validación de fechas pasadas y rangos inválidos. Cubre R3.
- [ ] T6 — Implementar validación de horarios superpuestos. Cubre R4.
- [ ] T7 — Implementar servicio de creación y desactivación con autorización de administrador. Cubre R1, R2, R6.
- [ ] T8 — Implementar consulta de horarios activos y libres para clientes. Cubre R5.
- [ ] T9 — Crear endpoints de administración y consulta pública. Cubre R1, R2, R5, R6.

## Pruebas y cierre

- [ ] T10 — Crear pruebas unitarias de fechas, solapamientos y estados. Cubre R3, R4, R6.
- [ ] T11 — Crear pruebas de integración de permisos, creación, consulta y desactivación. Cubre R1, R2, R5, R6, R7.
- [ ] T12 — Ejecutar migraciones, Ruff, mypy y pytest; documentar `R<n> → test` en `progress/impl_availability.md`. Cubre R7.
