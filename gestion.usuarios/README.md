# 👤 Microservicio: Gestión de Usuarios

## 📌 Descripción

El microservicio **Gestión de Usuarios** permite la administración de usuarios dentro del sistema de reservas de aerolíneas. Se encarga del registro, autenticación y gestión de perfiles de usuarios.

### 📍 Funcionalidades principales

- ✍️ **Registro de usuarios**
- 🔐 **Autenticación con JWT**
- 🛠️ **Gestión de perfiles de usuario**
- 🔄 **Actualización de datos del usuario**

---

## 📥 **Clonar el repositorio**

Para obtener una copia local del proyecto, ejecuta el siguiente comando:

```bash
git clone https://github.com/Andy2691/airline-reservation-system.git
cd airline-reservation-system/gestion.usuarios
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

### 🔹 **4️⃣ Iniciar el microservicio** 🚀
```bash
uvicorn main:app --reload --port 8085
```

---

## 📂 **Estructura del Proyecto**
```bash
📦 gestion.usuarios
 ┣ 📂 app
 ┃ ┣ 📂 database
 ┃ ┣ 📂 models
 ┃ ┣ 📂 routes
 ┃ ┣ 📂 schemas
 ┣ 📜 config.py
 ┣ 📜 main.py
 ┣ 📜 requirements.txt
 ┣ 📜 .gitignore
 ┣ 📜 README.md
```

---

## 📜 **Swagger - Documentación de la API**
El microservicio expone su documentación en Swagger automáticamente.

📌 **Accede a Swagger en:** [http://127.0.0.1:8085/docs](http://127.0.0.1:8085/docs)


