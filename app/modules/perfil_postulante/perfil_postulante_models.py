from pydantic import BaseModel

class DatosPostulante(BaseModel):
    id_usuario: int
    resumen: str
    habilidades: str
    idiomas: str
    link: str
    referencias: str

class ActualizarPerfilPostulante(BaseModel):
    id: int
    id_usuario: int
    resumen: str
    habilidades: str
    idiomas: str
    link: str
    referencias: str