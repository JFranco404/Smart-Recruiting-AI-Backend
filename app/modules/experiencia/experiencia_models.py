from pydantic import BaseModel
from datetime import date
from typing import Optional as TypingOptional

class DatosExperiencia(BaseModel):
    nombre_empresa:str
    contacto: str
    tipo_cargo: str
    fecha_inicio: date
    fecha_finalizacion: date
    responsabilidades: str

class ActualizarExperiencia(BaseModel):
    id: int
    nombre_empresa:str
    contacto: str
    tipo_cargo: str
    fecha_inicio: date
    fecha_finalizacion: date
    responsabilidades: str

class FiltrosExperiencia(BaseModel):
    nombre_empresa: TypingOptional[str] = None
    contacto: TypingOptional[str] = None
    tipo_cargo: TypingOptional[str] = None
    fecha_inicio: TypingOptional[date] = None
    fecha_finalizacion: TypingOptional[date] = None
    responsabilidades: TypingOptional[str] = None