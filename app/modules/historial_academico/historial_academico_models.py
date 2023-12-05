from pydantic import BaseModel
from datetime import date

class DatosHistorialAcademico(BaseModel):
    titulo_obtenido: str
    institucion: str
    area_de_estudio: str
    fecha_inicio: date
    fecha_finalizacion: date
    promedio_ponderado: float
    reconocimientos: str

class ActualizarHistorialAcademico(BaseModel):
    id: int
    titulo_obtenido: str
    institucion: str
    area_de_estudio: str
    fecha_inicio: date
    fecha_finalizacion: date
    promedio_ponderado: float
    reconocimientos: str
    