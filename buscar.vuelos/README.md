# ✈️ Microservicio: Buscar Vuelos

## 📌 Descripción

El microservicio **Búsqueda de Vuelos** permite realizar consultas de vuelos disponibles según origen, destino y fecha del vuelo.

### 📍 Funcionalidades principales

- 🔍 **Búsqueda de vuelos por origen y destino**
- 📅 **Filtrado por fecha de vuelo**
- 📊 **Paginación de resultados**

---

## 📥 **Clonar el repositorio**

Para obtener una copia local del proyecto, ejecuta el siguiente comando:

```bash
git clone https://github.com/Andy2691/airline-reservation-system.git
cd airline-reservation-system/buscar.vuelos
```

---

## ⚙️ **Configuración y Ejecución**

### 🔹 **1️⃣ Configurar entorno virtual**
Cada microservicio debe ejecutarse en su propio entorno virtual.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 🔹 **2️⃣ Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 🔹 **3️⃣ Configurar la Base de Datos**
Si aún no se ha levantado el contenedor PostgreSQL en la configuración principal del proyecto, ejecuta:
```bash
docker run --name flights -e POSTGRES_PASSWORD=test -e POSTGRES_DB=flights -e POSTGRES_USER=test -p 5432:5432 timescale/timescaledb:latest-pg14
```

Los demás microservicios (`reservas.vuelos` y `gestion.usuarios`) **se conectarán a esta base de datos sin necesidad de levantar otro contenedor**.


### 🔹 **4️⃣ Ejecutar migraciones con Alembic**
```bash
alembic upgrade head
```

### 🔹 **5️⃣ Iniciar el microservicio** 🚀
```bash
uvicorn main:app --reload --port 8086
```

---

## 📂 **Estructura del Proyecto**
```bash
📦 buscar.vuelos
 ┣ 📂 app
 ┃ ┣ 📂 database
 ┃ ┣ 📂 models
 ┃ ┣ 📂 routes
 ┃ ┣ 📂 schemas
 ┣ 📜 config.py
 ┣ 📜 main.py
 ┣ 📜 requirements.txt
 ┣ 📜 alembic.ini
 ┣ 📂 alembic
 ┣ 📜 .gitignore
 ┣ 📜 README.md
```

---

## 📜 **Swagger - Documentación de la API**
El microservicio expone su documentación en Swagger automáticamente.

📌 **Accede a Swagger en:** [http://127.0.0.1:8086/docs](http://127.0.0.1:8086/docs)


