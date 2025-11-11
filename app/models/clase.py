from pydantic import BaseModel
class Clase(BaseModel):
    duracion: int
    maniobras: list[str]
    notas: str