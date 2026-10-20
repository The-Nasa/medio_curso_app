# Guía de despliegue

Esta carpeta contiene el contexto para que la persona encargada implemente el despliegue con GitHub Actions después de clonar el repositorio.

## Orden obligatorio

1. Leer `AGENTS.md`, `docs/architecture.md`, `docs/verification.md` y la feature `deployment` de `feature_list.json`.
2. Esperar a que el `spec_author` cree y se apruebe `specs/deployment/`.
3. Crear el `Dockerfile` de la API Python.
4. Revisar `.github/workflows/ci.yml` y `.github/workflows/deploy.yml`.
5. Configurar los GitHub Actions Secrets del proveedor cloud.
6. Ejecutar CI y revisar sus resultados.
7. Publicar la imagen Docker desde GitHub Actions.
8. Ejecutar migraciones Alembic de forma controlada.
9. Verificar `/health`, logs y rollback.

## Prohibiciones

- No guardar secretos en Git.
- No subir archivos con secretos reales.
- No desplegar sin revisar el workflow y sus permisos.
- No crear recursos destructivos sin aprobación.

## Entregables esperados

- `Dockerfile`.
- `.github/workflows/ci.yml` y `.github/workflows/deploy.yml`.
- `.env.example` sin secretos reales.
- Secrets y variables de GitHub Actions documentados sin exponer sus valores.
- Health check.
- Informe en `progress/deploy_deployment.md`.
