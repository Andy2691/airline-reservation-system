# Microservicio: Gestión de Usuarios

## Descripción
Este microservicio maneja la gestión de usuarios, incluyendo autenticación, registro y administración de cuentas de usuario. También gestiona la asignación de reservas de vuelos a usuarios.

## Tecnologías Utilizadas
- **Lenguaje**: Python 3.10+
- **Framework**: FastAPI
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy
- **Autenticación**: OAuth2 con JWT
- **Gestión de Dependencias**: Pydantic
- **Migraciones**: Alembic
- **Versionado**: Git + GitHub
- **Pruebas**: Pytest

## Estructura del Proyecto
```
gestion.usuarios/
│── app/
│   ├── auth/                    # Módulo de autenticación
│   ├── database/                # Configuración de la base de datos
│   ├── models/                  # Modelos de datos (SQLAlchemy)
│   │   ├── schema/
│   │   │   ├── users.py
│   │   │   ├── reservations.py
│   ├── routes/                  # Endpoints del microservicio
│   │   ├── users.py
│   │   ├── dependencies.py
│── venv/                        # Entorno virtual de Python
│── alembic.ini                   # Configuración de migraciones
│── config.py                      # Variables de configuración
│── main.py                        # Punto de entrada de FastAPI
│── README.md                      # Documentación del proyecto
│── requirements.txt                # Dependencias del proyecto
```

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/gestion-usuarios.git
cd gestion-usuarios
```

### 2. Crear y Activar un Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
Levantar un contenedor PostgreSQL con Docker:
```bash
docker run --name users-db -e POSTGRES_PASSWORD=test -e POSTGRES_DB=users -e POSTGRES_USER=test -p 5433:5432 timescale/timescaledb:latest-pg14
```

### 5. Ejecutar Migraciones con Alembic
```bash
alembic upgrade head
```

### 6. Ejecutar el Servidor FastAPI
```bash
uvicorn main:app --host 0.0.0.0 --port 8087 --reload
```

El servicio estará disponible en: [http://localhost:8087/docs](http://localhost:8087/docs)

## Endpoints Principales
- `POST /users/register`: Registro de un nuevo usuario.
- `POST /users/login`: Autenticación de usuario.
- `GET /users/me`: Obtiene información del usuario autenticado.
- `GET /users/{user_id}/reservations`: Obtiene las reservas de un usuario.

## Pruebas
Para ejecutar las pruebas unitarias:
```bash
pytest
```

## Contribución
Si deseas contribuir, crea un *fork* del repositorio, realiza tus cambios en una rama y abre un *pull request*.

## Licencia
Este proyecto está bajo una licencia abierta. Puedes modificarlo y distribuirlo según tus necesidades.

