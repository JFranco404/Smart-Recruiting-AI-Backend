from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id

router = APIRouter()


@router.get("/perfil-postulante/{usuario_id}", tags=["Perfil Postulante"])
async def ruta_obtener_perfil_postulante_por_usuario_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        perfil_postulante = obtener_perfil_postulante_por_usuario_id(
            usuario_id, db)
        return perfil_postulante

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
