from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from app.modules.postulacion.postulacion_services import *
from app.modules.auth.auth_services import autorizar_postulante, autorizar_reclutador

router = APIRouter()

@router.get("/postulaciones", tags=["Postulation"])
async def ruta_obtener_postulacion_por_usuario_id(payload : dict = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        postulaciones = obtener_postulacion_por_usuario_id(
            payload.get('id_usr'), db)
        return postulaciones

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
    

@router.post("/postular_a_vacante/{vacante_id}", tags=["Postulation"])
async def ruta_seleccionar_postulacion(vacante_id: int, payload : dict = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        seleccionar_postulacion(vacante_id, payload.get('id_usr'), db)
        return {"message": "La postulación se realizó exitosamente"}
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
