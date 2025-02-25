# Microservicio: Búsqueda de Vuelos

## Descripción
Este microservicio permite realizar la consulta de vuelos disponibles según origen, destino y fecha del vuelo.

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
Buscar.Vuelos/
│── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schema/
│   ├── flights.py
│── alembic/
│── venv/
│── main.py
│── config.py
│── requirements.txt
│── alembic.ini
│── README.md
```

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/buscar_vuelos.git
cd buscar_vuelos
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
docker run --name flights -e POSTGRES_PASSWORD=test -e POSTGRES_DB=flights -e POSTGRES_USER=test -p 5432:5432 timescale/timescaledb:latest-pg14
```

### 5. Ejecutar Migraciones con Alembic
```bash
alembic upgrade head
```

### 6. Ejecutar el Servidor FastAPI
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

El servicio estará disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints Principales
- `GET /flights/search`: Búsqueda de vuelos según origen, destino y fecha.

## Pruebas
Para ejecutar las pruebas unitarias:
```bash
pytest
```

## Contribución
Si deseas contribuir, crea un *fork* del repositorio, realiza tus cambios en una rama y abre un *pull request*.

## Licencia
Este proyecto está bajo una licencia abierta. Puedes modificarlo y distribuirlo según tus necesidades.

