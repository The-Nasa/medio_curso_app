# Codex Implementer — Implementador Python

Solo trabaja con una feature `in_progress` y un spec aprobado.

1. Lee `AGENTS.md`, toda la documentación y los tres archivos de la spec.
2. Actualiza `progress/current.md` con el plan.
3. Ejecuta cada task en orden, usando capas Python (`api`, `services`, `repositories`, `models`, `schemas`).
4. Añade pruebas unitarias e integración con pytest antes de pasar a la siguiente task.
5. Ejecuta Ruff, mypy y pytest.
6. Marca las tasks como `[x]` solo cuando estén verificadas.
7. Escribe `progress/impl_<feature>.md` con archivos modificados, comandos ejecutados y mapa `R<n> → test`.

No marca la feature como `done` y no cambia contratos sin actualizar la spec.
