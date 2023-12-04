from pydantic import BaseModel
from datetime import date
from typing import Optional as TypingOptional

class DatosExperienciaPorPerfilPostulante(BaseModel):
    id_perfil_postulante: int
    id_experiencia: int

class FiltrosExperienciaPerfilPostulante(BaseModel):
    id_perfil_postulante: TypingOptional[int] = None
    id_experiencia: TypingOptional[int] = None