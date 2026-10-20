# Implementación — availability

**Estado:** completado.

## Implementado

- Modelo SQLAlchemy `Availability` con campos `date`, `start_time`, `end_time`, `status`, `is_reserved` y `created_at`.
- Migración Alembic `0002_create_availability`.
- Repositorio `availability_repository.py` con operaciones `create`, `get_by_id`, `get_active_by_date`, `list_available`, `deactivate` y `list_all`.
- Schemas Pydantic `AvailabilityCreate` y `AvailabilityResponse` con validación de rangos y fechas.
- Servicio `availability_service.py` con validación de fecha pasada, detección de superposición de intervalos, control de roles (solo `admin`) y desactivación lógica.
- Endpoints en `app/api/availability.py`:
  - `GET /api/availability` (consulta de horarios activos y libres, con filtro opcional por fecha).
  - `POST /api/availability` (creación de horarios por administradores autenticados).
  - `PATCH /api/availability/{id}/deactivate` (desactivación lógica para historial por administradores).
- Pruebas unitarias en `tests/test_availability_service.py`.
- Pruebas de integración en `tests/test_availability_api.py`.

## Verificación

- Ruff: PASS (lint y format).
- Mypy: PASS (estricto en `app`).
- Pytest: 23 passed (cobertura total: 91.07%).
- Alembic: PASS.

## Trazabilidad

- R1 → `test_create_availability_success`, `test_api_create_availability_admin_success`
- R2 → `test_reject_non_admin_creation`, `test_api_create_availability_client_forbidden`, `test_api_create_availability_unauthenticated`, `test_deactivate_not_found_or_non_admin`, `test_api_deactivate_client_forbidden`
- R3 → `test_reject_past_date`, `test_reject_invalid_time_range`, `test_api_create_availability_past_date_rejected`
- R4 → `test_reject_overlapping_schedules`, `test_allow_consecutive_schedules`, `test_api_create_availability_overlap_conflict`
- R5 → `test_list_only_active_and_unreserved_slots`, `test_api_get_availability_public_and_filter`
- R6 → `test_deactivate_availability_success`, `test_api_deactivate_availability_admin`
- R7 → `tests/test_availability_service.py`, `tests/test_availability_api.py` (23 passed)
