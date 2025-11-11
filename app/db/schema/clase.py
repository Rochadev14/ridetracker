def clase_schema(clase) -> dict:
    return {
        "id": str(clase["_id"]),
        "duracion": clase["duracion"],
        "maniobras": clase["maniobras"],
        "notas": clase["notas"]
    }

def clases_schema(clases) -> list:
    return [clase_schema(clase) for clase in clases]