from pydantic import BaseModel
from datetime import date
from typing import Optional as TypingOptional


class DatosVacante(BaseModel):
    titulo: str
    descripcion: str
    usuario_reclutador: int
    fecha_publicacion: str
    fecha_cierre: str
    salario: float
    remoto: bool
    modalidad: str
    ubicacion: int
    area_trabajo: str
    annos_experiencia: int

class ActualizarVacante(BaseModel):
    id: int
    titulo: str
    descripcion: str
    usuario_reclutador: int
    fecha_publicacion: str
    fecha_cierre: str
    salario: float
    remoto: bool
    modalidad: str
    ubicacion: int
    area_trabajo: str
    annos_experiencia: int

class FiltrosVacante(BaseModel):
    titulo: TypingOptional[str] = None
    fecha_publicacion: TypingOptional[date] = None
    fecha_cierre: TypingOptional[date] = None
    salario: TypingOptional[float] = None
    remoto: TypingOptional[bool] = None
    modalidad: TypingOptional[str] = None
    ubicacion: TypingOptional[int] = None
    area_trabajo: TypingOptional[str] = None
    annos_experiencia: TypingOptional[int] = None