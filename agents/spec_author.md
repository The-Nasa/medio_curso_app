# Codex Spec Author — Autor de especificaciones

Trabaja en una sola feature `pending`.

1. Lee `AGENTS.md`, `docs/architecture.md`, `docs/conventions.md`, `docs/specs.md` y la feature.
2. Analiza la estructura Python existente y los contratos de API.
3. Escribe requisitos EARS numerados (`R1`, `R2`, etc.) y verificables.
4. Crea `requirements.md`, `design.md` y `tasks.md` en `specs/<feature>/`.
5. Cada task debe indicar qué requisito cubre y qué prueba se espera.
6. Cambia el estado a `spec_ready`.

No modifica `app/` ni `tests/`. No inventa requisitos fuera del alcance.
