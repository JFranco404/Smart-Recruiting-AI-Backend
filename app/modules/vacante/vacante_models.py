from pydantic import BaseModel


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
