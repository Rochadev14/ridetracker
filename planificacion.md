Mañana (2-3h): Carnet teórico
Tarde (1.5h): Proyecto código
Noche: Descanso o test carnet
```

### **Fin de semana:**
```
Sábado: 
- Mañana: Test simulacros carnet
- Tarde: Sesión código extendida (2-3h)

Domingo: 
- Flex (más carnet si vas mal, más código si vas bien)
```

**Total código semanal:** ~10-12h (suficiente para avanzar sólido)

---

## 🚗 + 💻 Cronograma Híbrido Noviembre

### **Semana 1 (4-10 Nov) - Setup + Fundamentos**

#### **Carnet:**
- Temas 1-5 del manual
- 10 tests por día
- **Meta:** 80% de acierto en tests básicos

#### **Código:**
**Proyecto:** **"RideTracker"** - App para trackear tus clases de conducir
(Irónico y útil para ti ahora mismo)

**Esta semana haces:**
- ✅ Setup: Docker + FastAPI + MongoDB
- ✅ Modelo base: `DrivingLesson` (fecha, duración, maniobras practicadas, notas)
- ✅ Endpoints CRUD básicos
- ✅ Docker Compose funcional

**Sesiones diarias (1.5h):**
```
Lun: Setup proyecto + Docker
Mar: Conectar FastAPI con MongoDB (motor/beanie)
Mié: Modelo DrivingLesson + primer endpoint POST
Jue: Endpoints GET (all, by id)
Vie: Endpoints PUT/DELETE
Sáb: Testing manual + documentación Swagger
Dom: Subir a GitHub + escribir README
```

**Recursos concentrados:**
- FastAPI + MongoDB: [Tutorial oficial Beanie](https://beanie-odm.dev/)
- Docker compose con Mongo: Ejemplo básico

---

### **Semana 2 (11-17 Nov) - Afianzar + Extender**

#### **Carnet:**
- Temas 6-10
- 15 tests por día
- **Meta:** 85% acierto + repasar fallos

#### **Código:**
**Nuevas features:**
- ✅ Autenticación JWT (usuarios instructor/alumno)
- ✅ Filtros y búsquedas (por fecha, tipo de maniobra)
- ✅ Validaciones con Pydantic

**Sesiones:**
```
Lun: Modelo User + hash passwords (bcrypt)
Mar: Login endpoint + generación JWT
Mié: Middleware de autenticación
Jue: Proteger endpoints + roles
Vie: Filtros en GET lessons
Sáb: Paginación + sorting
Dom: Testing endpoints con Postman/Thunder Client
```

---

### **Semana 3 (18-24 Nov) - Consolidar + Deploy**

#### **Carnet:**
- Temas 11-15 + repaso general
- 20 tests por día
- **Meta:** 90% acierto consistente
- **Simulacros completos** fin de semana

#### **Código:**
**Profesionalizar:**
- ✅ Logging estructurado
- ✅ Variables de entorno (pydantic-settings)
- ✅ Health check endpoint
- ✅ Deploy en servidor/cloud

**Sesiones:**
```
Lun: Configurar logging (loguru)
Mar: Refactor config con .env
Mié: Endpoint /health + métricas básicas
Jue: Preparar deploy (railway.app o render.com)
Vie: Deploy a producción
Sáb: Testing en prod + fix bugs
Dom: Documentación técnica
```

---

### **Semana 4 (25-30 Nov) - Pulir + Examen**

#### **Carnet:**
- **Repaso intensivo**
- 3-4 simulacros completos por día
- Identificar puntos débiles y machacar
- **Meta:** Reservar examen si estás 90%+ consistente

#### **Código:**
**Cerrar proyecto:**
- ✅ Frontend mínimo (HTML+Tailwind) o dashboard simple
- ✅ Escribir post técnico sobre el proyecto
- ✅ Video demo 3-5 min

**Sesiones:**
```
Lun-Mar: Dashboard básico (ver lecciones, stats simples)
Mié: Escribir post "Cómo construí RideTracker con FastAPI+MongoDB"
Jue: Grabar video demo
Vie: Publicar en LinkedIn/Twitter + GitHub polish
Sáb-Dom: SOLO CARNET (examen cerca)

Backend:
  - FastAPI (async)
  - MongoDB con Motor o Beanie (ODM)
  - JWT para auth (python-jose)
  - Bcrypt para passwords
  - Pydantic para validación

DevOps:
  - Docker + Docker Compose
  - MongoDB en container
  - Railway/Render para deploy (free tier)

Opcional Semana 3-4:
  - Traefik (si quieres practicar reverse proxy)
  - Frontend: HTML + Tailwind CSS (vía CDN, sin build)
  - Logging: Loguru
```

---

## 📊 Métricas de Éxito

### **Carnet (fin de mes):**
- ✅ 90%+ acierto en simulacros
- ✅ Examen reservado o aprobado
- ✅ 600+ preguntas practicadas

### **Código (fin de mes):**
- ✅ API completa desplegada y funcionando
- ✅ Auth + CRUD + Filtros
- ✅ Código en GitHub con buen README
- ✅ Post técnico publicado
- ✅ Dashboard básico (aunque sea feo)

---

## 🎮 Reglas del Juego

### **No Negociables:**
1. **Carnet tiene prioridad SIEMPRE**
2. **Si un día no puedes codear, OK** (pero mínimo 4 días/semana)
3. **Código máximo 2h en días de carnet** (para no quemarte)

### **Hackers Psicológicos:**
- **"Regla de los 15 min":** Si no tienes ganas de codear, comprométete solo 15 min. Casi siempre seguirás.
- **Playlist específica:** Misma música para carnet, otra para código (tu cerebro asociará)
- **Wins visibles:** Checkmarks en papel, no solo digital

### **Válvula de Escape:**
Si en Semana 2 ves que vas MUY justo con el carnet:
- Reduce código a 3 días/semana
- Solo features críticas (CRUD + auth)
- Deja deploy para diciembre

---

## 🚨 Plan B - Si el Carnet se Complica

**Semana 3 mal? Activa "Modo Examen":**
```
Carnet: 5-6h diarias
Código: PAUSA completa o max 30min/día mantenimiento