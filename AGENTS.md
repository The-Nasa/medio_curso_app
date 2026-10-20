# AGENTS.md — Mapa del proyecto

Este archivo es el punto de entrada de Codex. Es un mapa, no una biblia: lee la documentación específica solo cuando la tarea lo requiera.

## Antes de comenzar

1. Ejecutar `bash ./init.sh`; si falla, detenerse.
2. Leer `progress/current.md` y `feature_list.json`.
3. Leer `docs/specs.md` antes de tocar una feature SDD.
4. Trabajar solo en una feature a la vez.
5. No escribir código hasta que la feature tenga su spec aprobada.

## Mapa del repositorio

| Ruta | Propósito |
|---|---|
| `feature_list.json` | Alcance, acceptance, responsables y estados |
| `agents/` | Roles de Codex: leader, spec_author, implementer, reviewer y deployer |
| `specs/<feature>/` | Requirements, design y tasks de una feature |
| `docs/` | Arquitectura, convenciones, SDD, API y verificación |
| `progress/` | Estado vivo, historial e informes de implementación/revisión |
| `CHECKPOINTS.md` | Criterios objetivos para cerrar una feature |
| `app/` | Código Python de la aplicación |
| `tests/` | Pruebas automatizadas |

## Reglas

- Toda feature con `sdd: true` comienza sin spec; el `spec_author` crea `requirements.md`, `design.md` y `tasks.md` después de leer su `acceptance` del JSON.
- Cada requisito `R<n>` debe tener al menos una prueba.
- No modificar el contrato de API sin actualizar `docs/api-contract.md`.
- La Persona 1 es responsable de `auth` y `users`.
- La Persona 2 es responsable de `availability` y `reservations`.
- El código de aplicación se escribe en Python siguiendo `docs/architecture.md` y `docs/conventions.md`.
- Nadie marca una feature como `done` sin pruebas y revisión.

## Reglas duras

- No mezclar funcionalidades en una misma sesión.
- No saltar la aprobación humana en `spec_ready`.
- No declarar `done` con tests rojos o tasks sin marcar.
- Documentar el trabajo en `progress/current.md` mientras se realiza.
- Si existe un bloqueo, marcar la feature como `blocked`, explicar la causa y detenerse.

## Flujo de Codex

`leader → spec_author → aprobación humana → implementer → reviewer`

Las instrucciones de cada rol están en `agents/`. Codex usa este protocolo; no se requieren archivos de Claude Code.

El leader coordina; el spec_author redacta specs; el implementer programa; el reviewer verifica.

El `deployer` solo trabaja con `deployment` después de que la aplicación esté aprobada. No modifica funcionalidades de negocio ni maneja secretos.

## Cierre

1. Ejecutar `bash ./init.sh`.
2. El reviewer debe dejar `progress/review_<feature>.md`.
3. Solo después de `APPROVED` se cambia el estado a `done`.
4. Pasar el resumen de `progress/current.md` a `progress/history.md`.
