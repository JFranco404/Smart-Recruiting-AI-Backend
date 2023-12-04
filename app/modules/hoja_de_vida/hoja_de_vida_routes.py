from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from .hoja_de_vida_services import generar_hoja_de_vida
from app.modules.auth.auth_services import autorizar_postulante

router = APIRouter()


@router.get("/generar-hoja-de-vida/", tags=["Hoja de vida"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(payload=Depends(autorizar_postulante), db: Session = Depends(get_db)) -> str:
    try:
        return generar_hoja_de_vida(payload.get('id_usr'), db)

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
