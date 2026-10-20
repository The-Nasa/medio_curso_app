# Design — availability

## Responsable

Persona 2.

## Alcance

Implementar la gestión de horarios que serán utilizados por la funcionalidad de reservas.

## Archivos previstos

```text
app/models/availability.py
app/schemas/availability.py
app/repositories/availability_repository.py
app/services/availability_service.py
app/api/availability.py
alembic/versions/<revision>_create_availability.py
tests/test_availability.py
```

## Decisiones técnicas

- El horario tendrá estado `active` o `inactive`.
- La validación de solapamientos vivirá en el servicio.
- La autorización usará la dependencia JWT existente y comprobará el rol `admin`.
- La consulta pública devolverá solo horarios activos y libres.
- La desactivación será lógica para conservar el historial.

## Dependencias

Usa `User`, JWT, `get_current_user` y la sesión SQLAlchemy implementados en `auth`.

## Alternativa descartada

Se descarta borrar horarios desactivados porque se perdería trazabilidad y se romperían las referencias de futuras reservas.
