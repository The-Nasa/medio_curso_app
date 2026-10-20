# Requirements — availability

## R1
CUANDO un administrador autenticado envíe fecha, hora de inicio y hora de fin válidas, el sistema DEBE crear un horario disponible.

## R2
SI una persona no tiene rol de administrador ENTONCES el sistema DEBE rechazar la creación de horarios.

## R3
SI la fecha u hora de inicio del horario está en el pasado ENTONCES el sistema DEBE rechazarlo.

## R4
SI el nuevo horario se superpone con otro horario activo ENTONCES el sistema DEBE rechazarlo.

## R5
CUANDO un cliente consulte disponibilidad, el sistema DEBE mostrar únicamente horarios activos y no reservados.

## R6
CUANDO un administrador desactive un horario, el sistema DEBE conservarlo para el historial y DEBE impedir nuevas reservas sobre él.

## R7
CUANDO se implemente la gestión de horarios, el sistema DEBE tener pruebas unitarias y de integración para permisos, fechas, solapamientos y consulta.
