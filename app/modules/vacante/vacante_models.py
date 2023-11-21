from pydantic import BaseModel


class CrearVacante(BaseModel):
    titulo: str
    descripcion: str
    usuario_reclutador: int
    fecha_publicacion: str
    fecha_cierre: str
    salario: float
    remoto: int
    modalidad: str
    ubicacion: str
    area_trabajo: str
    annos_experiencia: int
