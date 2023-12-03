from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.shared.generar_archivo.generar_archivo import FabricaDeArchivos
from app.shared.generar_archivo.tipo_plantilla import TipoPlantilla


def generar_hoja_de_vida(id_usuario: int, db: Session) -> str:
    '''Genera una hoja de vida en formato PDF y la retorna en base64'''
    datos = __obtener_datos_hoja_de_vida(id_usuario, db)
    return FabricaDeArchivos().generar_pdf(datos, TipoPlantilla.HOJA_DE_VIDA)


def __obtener_datos_hoja_de_vida(id_usuario: int, db: Session) -> dict:
    '''Obtiene los datos necesarios para generar una hoja de vida'''
    return {
        "usuario": "Juan",
        "apellido": "Perez",
        "edad": 20,
        "correo": "juan.perez@gmail.com",
    }
