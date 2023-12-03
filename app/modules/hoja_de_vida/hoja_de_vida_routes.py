from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from .hoja_de_vida_services import generar_hoja_de_vida

router = APIRouter()


@router.get("/generar-hoja-de-vida/{id_usuario}", tags=["Hoja de vida"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(id_usuario: int, db: Session = Depends(get_db)) -> str:
    try:
        return generar_hoja_de_vida(id_usuario, db)

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
