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

class DatosUbicacion(BaseModel):
    cuidad: str
    estado: str
    pais: str

class DatosExperiencia(BaseModel):
    nombre_empresa: str
    contacto: str
    tipo_cargo: int
    fecha_inicio: str
    fecha_finalizacion: str
    responsabilidades: str

class DatosHistorialAcademico(BaseModel):
    titulo_obtenido: str
    institucion: str
    area_de_estudio: str
    fecha_inicio: str
    fecha_finalizacion: str
    promedio_ponderado: int
    reconocimientos: str

class DatosEducacionPorPerfilPostulante(BaseModel):
    id_perfil_postulante: int
    id_historial_academico: int

class DatosExperienciaPorPerfilPostulante(BaseModel):
    id_perfil_postulante: int
    id_experiencia: int





