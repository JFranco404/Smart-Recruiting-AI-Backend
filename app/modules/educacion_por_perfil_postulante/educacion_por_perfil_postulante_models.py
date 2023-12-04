from pydantic import BaseModel
from datetime import date
from typing import Optional as TypingOptional

class DatosEducacionPorPerfilPostulante(BaseModel):
    id_perfil_postulante: int
    id_historial_academico: int

class FiltrosEducacionPerfilPostulante(BaseModel):
    id_perfil_postulante: TypingOptional[int] = None
    id_historial_academico: TypingOptional[int] = None