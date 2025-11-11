from fastapi import FastAPI , HTTPException, status
from models.clase import Clase 
from db.client import client
from db.schema.clase import clase_schema,clases_schema
from bson import ObjectId
app = FastAPI()

clases = []  # Lista vacía por ahora
# TODO 1: POST /clases
# Recibe: duracion (int), maniobras (lista), notas (str)
# Guarda en la lista 'clases'
# Devuelve: la clase guardada + su índice

@app.post("/clases")
async def crear_clase(clase: Clase):
    #Formateamos el objeto a diccionario y sacamos la id que nos da mongo a la vez que lo guardamos
    #No hace falta verificacion de doble clase 
    clase_mongo = clase.model_dump()
    id=client.local.clases.insert_one(clase_mongo).inserted_id
    return {"id":str(id),
            "clase":clase_schema(client.local.clases.find_one({"_id":id}))}


# TODO 2: GET /clases
# Devuelve: todas las clases
@app.get("/clases")
async def obtener_clases():
    return clases_schema(client.local.clases.find())


# TODO 3: GET /clases/{clase_id}
# Recibe: clase_id en la URL
# Devuelve: la clase en esa posición
# (Ignora errores por ahora, eso viene después)
@app.get("/clases/{clase_id}")
async def obtener_clase(clase_id: str): 
    try:
        clase=client.local.clases.find_one({"_id": ObjectId(clase_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clase no encontrada"))
    return clase_schema(client.local.clases.find_one({"_id": ObjectId(clase_id)}))



@app.delete("/clases/{clase_id}")
async def borrar_clase(clase_id: str):
    try:
        clase=client.local.clases.find_one({"_id": ObjectId(clase_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clase no encontrada")

    return client.local.clases.find_one_and_delete({"_id": ObjectId(clase_id)})

@app.put("/clases/{clase_id}")
async def actualizar_clase(clase_id: str, clase: Clase):
    try:
        clase=client.local.clases.find_one({"_id": ObjectId(clase_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clase no encontrada")
    
    return clase_schema(client.local.clases.find_one_and_update({"_id": ObjectId(clase_id)}, {"$set": clase.model_dump()}))