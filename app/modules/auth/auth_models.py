from pydantic import BaseModel

class Auth_login(BaseModel):
    correo: str
    passwd: str

class Auth_register(BaseModel):
    names: str
    surnames: str
    correo: str
    passwd: str
    rol_id: int

