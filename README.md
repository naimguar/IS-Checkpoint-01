# TeamBoard — IS-2026 Checkpoint 01

Aplicación web **TeamBoard**: página con integrantes del equipo, feature asignada y estado del servicio. El frontend obtiene los datos vía **HTTP** al backend **Flask**; el backend lee **PostgreSQL**. Todo se orquesta con **Docker Compose**; **Portainer** permite ver el estado de los contenedores desde el navegador.

## Integrantes y features


| Integrante       | Legajo | Feature(s) | Servicio |
| ---------------- | ------ | ---------- | -------- |
| Ignacio Benitez  | 33507  | 4          | database |
| Matias Dieguez   | 33080  | 2          | frontend |
| Naim Guarino     | 32683  | 1, 5       | infra    |
| Agustín Manrique | 31976  | 3          | backend  |


- **Feature 01:** coordinación, `docker-compose`, `.env` / `.env.example`, `.gitignore`, README.  
- **Feature 02:** frontend (HTML/JS, `http.server`).  
- **Feature 03:** backend (Flask, API REST).  
- **Feature 04:** base de datos (`init.sql`, Postgres en compose).  
- **Feature 05:** Portainer en compose (socket Docker, volumen de datos).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/) (v2, `docker compose`)

## Cómo clonar y ejecutar

```bash
git clone https://github.com/naimguar/is-2026-checkpoint-01.git
cd is-2026-checkpoint-01
cp .env.example .env
```

Editá `.env` y definí usuario, contraseña y nombre de base (los valores de ejemplo sirven para desarrollo local). **No subas** `.env` **a Git** (está en `.gitignore`).

Levantar el stack:

```bash
docker compose up -d --build
```

Comprobar estado:

```bash
docker compose ps
```

Todos los servicios deberían figurar en ejecución (y `database` / `backend` como **healthy** cuando corresponda).

Bajar contenedores (sin borrar volúmenes de datos):

```bash
docker compose down
```

## URLs locales


| Qué              | URL                                                                  |
| ---------------- | -------------------------------------------------------------------- |
| TeamBoard (UI)   | [http://localhost:8080](http://localhost:8080)                       |
| API (ej. equipo) | [http://localhost:5000/api/team](http://localhost:5000/api/team)     |
| Health backend   | [http://localhost:5000/api/health](http://localhost:5000/api/health) |
| Portainer        | [http://localhost:9000](http://localhost:9000)                       |


## Servicios del compose


| Servicio      | Descripción breve                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **frontend**  | Imagen propia (`frontend/Dockerfile`), Python `http.server` en el puerto **8080**, sirve HTML/JS estático. Depende del backend **healthy**.                       |
| **backend**   | API **Flask** + Gunicorn en **5000**. Endpoints: `/api/health`, `/api/team`, `/api/info`. Conecta a Postgres con variables `DB_`*. Depende de **db** **healthy**. |
| **db**        | **PostgreSQL 16** (Alpine). Datos en volumen `datos_db`; script `database/init.sql` en el arranque inicial. Healthcheck con `pg_isready`.                         |
| **portainer** | **Portainer CE** en **9000**. Monta el socket de Docker y el volumen `portainer_data` en `/data` para persistir la configuración.                                 |


Límites de **CPU** y **memoria** (`deploy.resources`) están definidos en cada servicio, según buenas prácticas del checkpoint.

## Portainer (Feature 05)

1. Abrí **[http://localhost:9000](http://localhost:9000)** con el stack levantado.
2. La **primera vez**, creá el usuario administrador que pide el asistente.
3. En el entorno local, elegí **“Get Started”** / conexión al socket **Docker** si te lo ofrece.
4. Revisá la lista de **contenedores** y confirmá que aparecen `frontend`, `backend`, `database`, `portainer`.

### Capturas para la entrega

Capturas incluidas en `docs/`:

- Login de Portainer: `docs/login portainer.png`

![Login de Portainer](docs/login%20portainer.png)

- Contenedores del proyecto en Portainer: `docs/contenedores funcionando.png`

![Contenedores del proyecto en Portainer](docs/contenedores%20funcionando.png)

## Estructura del repositorio

```
is-2026-checkpoint-01/
├── docker-compose.yml
├── .env.example
├── frontend/
├── backend/
├── database/
└── docs/          ← capturas de Portainer
```

## Materia

**Ingeniería y Calidad de Software** — UTN — Checkpoint 01 (Docker, Compose, Git, GitHub).