from fastapi import FastAPI, HTTPException, status
from models.clase import Clase 
from db.client import db
from db.schema.clase import clase_schema, clases_schema
from bson import ObjectId

app = FastAPI(
    title="RideTracker API",
    description="API para trackear clases de conducir",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Información básica de la API"""
    return {
        "app": "RideTracker API",
        "version": "1.0.0",
        "description": "API para trackear clases de conducir",
        "endpoints": {
            "docs": "/docs",
            "clases": "/clases",
            "stats": "/stats",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Verificar estado de la API y base de datos"""
    try:
        db.client.admin.command('ping')
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database unavailable: {str(e)}"
        )


@app.get("/stats")
async def obtener_estadisticas():
    """Obtener estadísticas globales de clases"""
    total_clases = db.clases.count_documents({})
    
    if total_clases == 0:
        return {
            "total_clases": 0,
            "total_horas": 0,
            "total_minutos": 0,
            "promedio_duracion_min": 0,
            "top_maniobras": []
        }
    
    # Agregación para calcular total de minutos
    pipeline_duracion = [
        {
            "$group": {
                "_id": None,
                "total_minutos": {"$sum": "$duracion"},
                "promedio_duracion": {"$avg": "$duracion"}
            }
        }
    ]
    
    result = list(db.clases.aggregate(pipeline_duracion))
    total_minutos = result[0]["total_minutos"]
    promedio = result[0]["promedio_duracion"]
    
    # Maniobras más practicadas
    pipeline_maniobras = [
        {"$unwind": "$maniobras"},
        {"$group": {"_id": "$maniobras", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]
    
    top_maniobras = list(db.clases.aggregate(pipeline_maniobras))
    
    return {
        "total_clases": total_clases,
        "total_horas": round(total_minutos / 60, 1),
        "total_minutos": total_minutos,
        "promedio_duracion_min": round(promedio, 1),
        "top_maniobras": [
            {"maniobra": m["_id"], "veces": m["count"]} 
            for m in top_maniobras
        ]
    }


@app.post("/clases", status_code=status.HTTP_201_CREATED)
async def crear_clase(clase: Clase):
    """Crear una nueva clase de conducir"""
    clase_dict = clase.model_dump()
    result = db.clases.insert_one(clase_dict)
    
    # Recuperar el documento insertado con su ID
    clase_creada = db.clases.find_one({"_id": result.inserted_id})
    
    return {
        "id": str(result.inserted_id),
        "clase": clase_schema(clase_creada)
    }

@app.get("/clases")
async def obtener_clases():
    """Obtener todas las clases"""
    clases = db.clases.find()
    return clases_schema(clases)

@app.get("/clases/{clase_id}")
async def obtener_clase(clase_id: str):
    # Validar formato de ObjectId
    try:
        object_id = ObjectId(clase_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )
    
    # Buscar la clase
    clase = db.clases.find_one({"_id": object_id})
    
    if clase is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    
    return clase_schema(clase)

@app.put("/clases/{clase_id}")
async def actualizar_clase(clase_id: str, clase: Clase):
    """Actualizar una clase existente"""
    # Validar formato de ObjectId
    try:
        object_id = ObjectId(clase_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )
    
    # Actualizar
    result = db.clases.update_one(
        {"_id": object_id},
        {"$set": clase.model_dump()}
    )
    
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    
    # Devolver documento actualizado
    clase_actualizada = db.clases.find_one({"_id": object_id})
    return clase_schema(clase_actualizada)

@app.delete("/clases/{clase_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_clase(clase_id: str):
    """Eliminar una clase"""
    # Validar formato de ObjectId
    try:
        object_id = ObjectId(clase_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )
    
    # Eliminar
    result = db.clases.delete_one({"_id": object_id})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    
    return None