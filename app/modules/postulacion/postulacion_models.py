from pydantic import BaseModel

class DatosPostulacion(BaseModel):
    id_vacante: int
    id_perfil_postulante: int