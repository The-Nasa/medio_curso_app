# Requirements — integration

## R1 — Flujo autenticado de reserva

CUANDO un cliente se registre o inicie sesión y use su token válido, el sistema DEBE permitirle consultar horarios disponibles y crear una reserva para un horario libre.

## R2 — Protección de funciones administrativas

SI un cliente autenticado intenta ejecutar una operación exclusiva de administrador ENTONCES el sistema DEBE rechazarla con un código HTTP de autorización adecuado.

## R3 — Ocupación consistente

CUANDO se cree una reserva válida, el sistema DEBE marcar el horario correspondiente como ocupado y excluirlo de la disponibilidad pública.

## R4 — Liberación consistente

CUANDO el propietario cancele una reserva ENTONCES el sistema DEBE marcarla como cancelada y liberar el horario para futuras reservas.

## R5 — Flujo completo verificable

EL SISTEMA DEBE tener pruebas de integración que cubran autenticación, consulta de disponibilidad, creación, rechazo de duplicados, cancelación y liberación del horario.

## R6 — Calidad y ejecución

CUANDO se ejecuten las validaciones del proyecto, Ruff, mypy y pytest DEBEN finalizar correctamente sin depender de datos reales.

## R7 — Documentación operativa

EL SISTEMA DEBE documentar cómo configurar variables de entorno, iniciar PostgreSQL con Docker, ejecutar migraciones, levantar la API y ejecutar las pruebas.
