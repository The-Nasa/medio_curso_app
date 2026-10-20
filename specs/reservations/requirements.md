# Requirements — reservations

## R1
CUANDO un cliente autenticado seleccione un horario activo y disponible, el sistema DEBE crear una reserva asociada a ese cliente.

## R2
SI una persona no está autenticada ENTONCES el sistema DEBE rechazar la creación de una reserva.

## R3
SI el horario seleccionado está ocupado, inactivo o no existe ENTONCES el sistema DEBE rechazar la reserva.

## R4
CUANDO un cliente consulte sus reservas, el sistema DEBE mostrar únicamente las reservas asociadas a ese cliente.

## R5
CUANDO un cliente cancele una reserva propia, el sistema DEBE cambiar su estado a `cancelled` y liberar el horario.

## R6
SI un cliente intenta cancelar una reserva de otra persona ENTONCES el sistema DEBE rechazar la operación.

## R7
CUANDO se cree una reserva válida, el sistema DEBE conservar la fecha, el horario, el cliente y el estado de la reserva.

## R8
CUANDO se implemente la gestión de reservas, el sistema DEBE tener pruebas unitarias y de integración para creación, permisos, duplicados, consulta y cancelación.
