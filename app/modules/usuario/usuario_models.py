from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    cedula: int
    nombres: str
    apellidos: str
    fecha_nacimiento: str
    lugar_residencia: int
    correo: str
    rol: int
    passwd: str
