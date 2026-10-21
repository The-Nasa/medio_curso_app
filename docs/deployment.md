# Guía de despliegue y operaciones — Tingo Reservas

Esta guía documenta la infraestructura, configuración, flujos de CI/CD, procedimientos de verificación, rollback y consulta de logs para el despliegue de la API y la base de datos PostgreSQL.

---

## 1. Configuración de PostgreSQL de producción

La aplicación utiliza PostgreSQL como motor de persistencia relacional a través de SQLAlchemy 2 y Alembic.

### Variables de entorno requeridas
En el entorno de producción (o en el archivo `.env` del host en EC2), se deben configurar las siguientes variables:

```ini
APP_ENV=production
LOG_LEVEL=INFO
JWT_SECRET=super_secret_jwt_key_minimo_32_caracteres_aleatorios!
DATABASE_URL=postgresql+psycopg://usuario_prod:password_seguro@host_o_ip_privada:5432/tingo_reservas_prod
```

### Recomendaciones de seguridad y red
- **Aislamiento de red:** La base de datos PostgreSQL (ya sea en AWS RDS o en una instancia EC2) debe estar en una subred privada o restringida mediante grupos de seguridad (Security Groups), permitiendo tráfico en el puerto 5432 únicamente desde la IP interna de la instancia donde corre la API.
- **Sin secretos en Git:** NUNCA almacenar contraseñas ni la cadena `DATABASE_URL` en archivos versionados. Se provee [`.env.example`](file:///.env.example) como referencia no sensible.
- **Migraciones automáticas:** El contenedor ejecuta automáticamente `alembic upgrade head` mediante su script de arranque [entrypoint.sh](file:///entrypoint.sh) antes de habilitar el servicio HTTP.

---

## 2. GitHub Actions y Secrets de despliegue

La canalización de CI/CD está compuesta por dos workflows en [`.github/workflows/`](file:///.github/workflows/):

1. **CI ([`.github/workflows/ci.yml`](file:///.github/workflows/ci.yml)):**
   - Se dispara en cada `push` o `pull_request` a `main`.
   - Ejecuta validaciones estáticas (`ruff check`, `ruff format --check`), tipado (`mypy`) y la suite completa de pruebas (`pytest -q --cov=app`).
   - Construye la imagen Docker para verificar su reproducibilidad.

2. **Deploy ([`.github/workflows/deploy.yml`](file:///.github/workflows/deploy.yml)):**
   - Se ejecuta automáticamente tras merges a `main` o manualmente mediante `workflow_dispatch`.
   - Ejecuta las pruebas unitarias y de integración como condición previa obligatoria antes de autorizar el despliegue.
   - Despliega en la instancia AWS EC2 conectándose vía SSH seguro.

### Secrets requeridos en GitHub Actions
En el repositorio (Settings -> Secrets and variables -> Actions) se configuran los siguientes secretos:

| Secret | Descripción |
|---|---|
| `EC2_HOST` | Dirección IP pública o nombre DNS de la instancia AWS EC2. |
| `EC2_USER` | Usuario SSH del sistema operativo en EC2 (ej. `ubuntu` o `ec2-user`). |
| `EC2_SSH_KEY` | Clave privada SSH (`id_rsa` / archivo `.pem`) para autenticación. |

---

## 3. Verificación de salud y disponibilidad (Health Check)

La API dispone de un endpoint dedicado para balanceadores, monitoreo y comprobación post-despliegue:

- **Ruta:** `GET /health`
- **Código de respuesta esperado:** `200 OK`
- **Cuerpo de respuesta:** `{"status": "ok"}`

### Comprobación local en la instancia EC2
```bash
curl -s http://localhost:8000/health
```

### Comprobación remota pública
```bash
curl -s http://<EC2_HOST>:8000/health
```

El pipeline de despliegue en GitHub Actions realiza automáticamente esta comprobación al finalizar el lanzamiento y falla si el endpoint no responde con `status: ok`.

---

## 4. Procedimiento de Rollback

En caso de detectarse anomalías o fallos en una versión desplegada:

### Paso 1: Reversión del código en Git
Si el error se debió a un cambio de código:
```bash
git revert HEAD --no-edit
git push origin main
```
Esto dispara automáticamente el workflow de CI y despliega la versión previa funcional.

### Paso 2: Rollback manual inmediato en EC2
Si se requiere restablecer el servicio de inmediato sin esperar al pipeline:
1. Conectarse a la instancia:
   ```bash
   ssh -i clave.pem usuario@<EC2_HOST>
   ```
2. Desplazar el repositorio al commit o release anterior:
   ```bash
   cd ~/medio_curso_app
   git checkout <hash_commit_estable>
   docker build -t tingo-reservas:latest .
   docker stop tingo-reservas && docker rm tingo-reservas
   docker run -d --name tingo-reservas --restart unless-stopped -p 8000:8000 --env-file .env tingo-reservas:latest
   ```

### Paso 3: Rollback de esquema en base de datos (Alembic)
Si la versión introdujo una migración de esquema que requiere revertirse:
```bash
docker exec -it tingo-reservas alembic downgrade -1
```

---

## 5. Revisión y monitoreo de logs

Para inspeccionar la actividad del servidor y diagnosticar errores:

- **Ver logs en tiempo real:**
  ```bash
  docker logs -f --tail 100 tingo-reservas
  ```
- **Verificar estado del contenedor:**
  ```bash
  docker ps -a --filter name=tingo-reservas
  ```
- **Monitorear consumo de CPU y memoria:**
  ```bash
  docker stats tingo-reservas
  ```
- **Inspeccionar ejecuciones de CI/CD:**
  Consultar la pestaña **Actions** en el repositorio GitHub (`https://github.com/The-Nasa/medio_curso_app/actions`) para auditar la traza completa de validaciones y despliegues.
