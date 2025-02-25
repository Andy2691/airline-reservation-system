# Microservicio: Reservas de Vuelos

## Descripción
Este microservicio permite gestionar las reservas de vuelos, permitiendo a los usuarios crear, consultar y cancelar sus reservas.

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
reservas.vuelos/
│── app/
│   ├── database/                # Configuración de la base de datos
│   │   ├── migrations/           # Migraciones de Alembic
│   │   ├── conn.py               # Conexión con PostgreSQL
│   │   ├── reservations.py       # CRUD de reservas en la BD
│   ├── models/                   # Modelos de datos (SQLAlchemy)
│   │   ├── schema/
│   │   │   ├── reservations.py   # Esquemas Pydantic para validación
│   ├── routes/                   # Endpoints del microservicio
│   │   ├── reservations.py       # Rutas de reservas
│   │   ├── dependencies.py       # Dependencias comunes
│── venv/                         # Entorno virtual de Python
│── alembic.ini                    # Configuración de migraciones
│── config.py                       # Variables de configuración
│── main.py                         # Punto de entrada de FastAPI
│── README.md                       # Documentación del proyecto
│── requirements.txt                 # Dependencias del proyecto
```

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/reservas-vuelos.git
cd reservas-vuelos
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
docker run --name reservas-db -e POSTGRES_PASSWORD=test -e POSTGRES_DB=reservas -e POSTGRES_USER=test -p 5434:5432 timescale/timescaledb:latest-pg14
```

### 5. Ejecutar Migraciones con Alembic
```bash
alembic upgrade head
```

### 6. Ejecutar el Servidor FastAPI
```bash
uvicorn main:app --host 0.0.0.0 --port 8088 --reload
```

El servicio estará disponible en: [http://localhost:8088/docs](http://localhost:8088/docs)

## Endpoints Principales
- `POST /reservations/`: Crear una nueva reserva.
- `GET /reservations/{reservation_id}`: Consultar una reserva por ID.
- `GET /reservations/`: Listar todas las reservas.
- `DELETE /reservations/{reservation_id}`: Cancelar una reserva.

## Pruebas
Para ejecutar las pruebas unitarias:
```bash
pytest
```

## Contribución
Si deseas contribuir, crea un *fork* del repositorio, realiza tus cambios en una rama y abre un *pull request*.

## Licencia
Este proyecto está bajo una licencia abierta. Puedes modificarlo y distribuirlo según tus necesidades.

