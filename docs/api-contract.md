# Contrato inicial de API — FastAPI

## Autenticación

- `POST /api/auth/register`
- `POST /api/auth/login`

## Reservas

- `GET /api/availability`
- `POST /api/reservations`
- `GET /api/reservations/me`
- `DELETE /api/reservations/{reservation_id}`

## Health Check y Diagnóstico

- `GET /health` (Retorna `{"status": "ok"}` con código 200 para balanceadores y monitoreo)

Las respuestas deben usar esquemas Pydantic. Los errores deben devolver códigos HTTP coherentes y mensajes seguros. Los nombres y respuestas de estas rutas deben acordarse antes de integrar las ramas.
