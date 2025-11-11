# 🚗 RideTracker API

API REST para trackear clases de conducir, construida con FastAPI y MongoDB.

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)

---

## 🎯 Problema que Resuelve

Cuando estás aprendiendo a conducir, es difícil recordar:
- Qué maniobras has practicado en cada clase
- Cuántas horas de práctica llevas
- Qué necesitas mejorar antes del examen

**RideTracker** te permite registrar cada clase con maniobras, notas y estadísticas de progreso.

---

## 🚀 Características

- ✅ **CRUD completo** de clases de conducir
- ✅ **Estadísticas** de progreso (horas totales, maniobras más practicadas)
- ✅ **Validación** con Pydantic
- ✅ **Documentación automática** (Swagger UI)
- ✅ **Containerizado** con Docker
- ✅ **Manejo robusto de errores** (400, 404, 503)

---

## 🛠️ Stack Técnico

- **Backend:** FastAPI 0.104
- **Base de Datos:** MongoDB 7.0
- **ODM:** PyMongo
- **Validación:** Pydantic
- **Containerización:** Docker + Docker Compose

---

## 📦 Instalación y Uso

### Requisitos Previos
- Docker
- Docker Compose

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/TU_USUARIO/ride-tracker.git
cd ride-tracker
```

2. **Levantar servicios con Docker**
```bash
docker-compose up --build
```

3. **Acceder a la API**
- API: http://localhost:8000
- Documentación interactiva: http://localhost:8000/docs
- Health check: http://localhost:8000/health

---

## 📚 Endpoints

### **Información**
- `GET /` - Información de la API
- `GET /health` - Estado de salud de la API y BD
- `GET /stats` - Estadísticas globales

### **CRUD Clases**
- `POST /clases` - Crear nueva clase
- `GET /clases` - Listar todas las clases
- `GET /clases/{id}` - Obtener clase específica
- `PUT /clases/{id}` - Actualizar clase
- `DELETE /clases/{id}` - Eliminar clase

---

## 🧪 Ejemplos de Uso

### Crear una clase
```bash
curl -X POST "http://localhost:8000/clases" \
  -H "Content-Type: application/json" \
  -d '{
    "duracion": 60,
    "maniobras": ["paralelo", "rotonda", "incorporacion"],
    "notas": "Primera clase, todo bien"
  }'
```

### Ver estadísticas
```bash
curl http://localhost:8000/stats
```

**Respuesta:**
```json
{
  "total_clases": 12,
  "total_horas": 24.5,
  "total_minutos": 1470,
  "promedio_duracion_min": 122.5,
  "top_maniobras": [
    {"maniobra": "paralelo", "veces": 10},
    {"maniobra": "rotonda", "veces": 8}
  ]
}
```

---

## 🗂️ Estructura del Proyecto

```
ride-tracker/
├── main.py                 # Aplicación principal
├── config.py               # Configuración con Pydantic Settings
├── requirements.txt        # Dependencias Python
├── Dockerfile              # Imagen Docker
├── docker-compose.yml      # Orquestación de servicios
├── .env                    # Variables de entorno (no en Git)
├── .env.example            # Ejemplo de variables
├── models/
│   └── clase.py            # Modelo Pydantic
├── db/
│   ├── client.py           # Cliente MongoDB
│   └── schema/
│       └── clase.py        # Schemas de serialización
└── tests/
    └── test_endpoints.sh   # Script de pruebas
```

---

## 🔧 Desarrollo Local (sin Docker)

### 1. Instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Iniciar MongoDB local
```bash
# Mac
brew services start mongodb-community

# Linux
sudo systemctl start mongod
```

### 3. Configurar .env
```bash
cp .env.example .env
# Editar MONGODB_URL=mongodb://localhost:27017
```

### 4. Ejecutar API
```bash
uvicorn main:app --reload
# o
fastapi dev main.py
```

---

## 🧪 Testing

### Script automatizado
```bash
chmod +x tests/test_endpoints.sh
./tests/test_endpoints.sh
```

### Swagger UI
Navega a http://localhost:8000/docs y prueba los endpoints interactivamente.

---

## 🚀 Despliegue a Producción

### Railway.app
```bash
# 1. Crear cuenta en railway.app
# 2. Instalar CLI
npm i -g @railway/cli

# 3. Login
railway login

# 4. Deploy
railway up
```

### Render.com
1. Conectar repositorio GitHub
2. Crear Web Service
3. Añadir MongoDB Atlas
4. Configurar variables de entorno

---

## 🎯 Roadmap Futuro

- [ ] Autenticación JWT
- [ ] Filtros por fecha y maniobra
- [ ] Dashboard web con HTML/Tailwind
- [ ] Tests unitarios con pytest
- [ ] CI/CD con GitHub Actions
- [ ] Exportar datos a CSV/PDF
- [ ] Notificaciones de próximas clases
- [ ] Comparación con otros alumnos

---

## 🐛 Problemas Conocidos

- MongoDB debe estar corriendo antes de iniciar la API
- En Windows, asegurar que Docker Desktop está activo
- Si puerto 8000 ocupado, cambiar en docker-compose.yml

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto es de código abierto bajo la licencia MIT.

---

## 👤 Autor

**[Tu Nombre]**
- GitHub: [@Rochadev14](https://github.com/Rochadev14)
- LinkedIn: [Tu Perfil](https://linkedin.com/in/daniel-rocha-piqueras-08275636a)
- Email: danielrochadev14@gmail.com

---

## 🙏 Agradecimientos

- FastAPI por su excelente framework
- MongoDB por la base de datos flexible
- Comunidad de Python por el soporte

---

**⭐ Si te gustó el proyecto, dale una estrella en GitHub!**