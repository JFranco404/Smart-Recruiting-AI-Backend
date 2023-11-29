from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from app.modules.postulacion.postulacion_services import *

router = APIRouter()

@router.get("/postulaciones/{user_id}", tags=["Postulation"])
async def ruta_obtener_postulacion_por_usuario_id(user_id: int, db: Session = Depends(get_db)):
    try:
        postulaciones = obtener_postulacion_por_usuario_id(
            user_id, db)
        return postulaciones

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
    

@router.post("/postular_a_vacante/{usuario_id}/{vacante_id}", tags=["Postulation"])
async def ruta_seleccionar_postulacion(usuario_id: int, vacante_id: int, db: Session = Depends(get_db)):
    try:
        seleccionar_postulacion(usuario_id, vacante_id, db)
        return {"message": "La postulación se realizó exitosamente"}
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
