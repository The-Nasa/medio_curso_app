# Spec-Driven Development

Cada feature sigue tres documentos:

```text
requirements.md → qué debe hacer
design.md       → cómo se construirá
tasks.md        → pasos ejecutables
```

Estados:

```text
pending → spec_ready → aprobación humana → in_progress → done
```

La spec se crea a partir de `description` y `acceptance` de `feature_list.json`; no se escribe manualmente antes de que el `spec_author` tome la feature. La persona responsable la revisa y la aprueba. Después se implementa y se verifica con pruebas.

Cada `requirements.md` debe usar IDs estables `R1`, `R2`, etc. Cada task debe indicar qué requisitos cubre y cada requisito debe tener al menos una prueba.
