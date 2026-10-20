# Design — reservations

## Responsable

Persona 1.

## Alcance

Permitir que clientes autenticados creen, consulten y cancelen reservas usando los horarios creados por `availability`.

## Archivos previstos

```text
app/models/reservation.py
app/schemas/reservation.py
app/repositories/reservation_repository.py
app/services/reservation_service.py
app/api/reservations.py
alembic/versions/<revision>_create_reservations.py
tests/test_reservations.py
```

## Decisiones técnicas

- La reserva tendrá estado `confirmed` o `cancelled`.
- La creación se hará dentro de una transacción.
- El servicio verificará que el horario esté activo y libre antes de reservar.
- La consulta filtrará siempre por el usuario autenticado.
- La cancelación será lógica para conservar el historial.
- Se reutilizarán `get_current_user` y los modelos de `availability`.

## Alternativa descartada

Se descarta eliminar reservas físicamente porque se perdería el historial y no se podría auditar una cancelación.
