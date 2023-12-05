from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.experiencia.experiencia_services import *
from app.modules.experiencia.experiencia_models import *
from app.modules.experiencia_por_perfil_postulante.experiencia_por_perfil_postulante_services import obtener_experiencia_por_perfil_postulante_por_postulante_id
from app.modules.auth.auth_services import autorizar_postulante

router = APIRouter()

@router.get("/experiencia", tags=["Experiencia"])
async def ruta_obtener_experiencia_por_postulante_id(payload = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        educacion = obtener_experiencia_por_perfil_postulante_por_postulante_id(
            payload.get("id_usr"), db)
        return educacion

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post('/experiencia', tags=["Experiencia"])
async def ruta_crear_experiencia (experiencia: DatosExperiencia, db:Session = Depends(get_db)):
    try:
        experiencia_creada = crear_experiencia(experiencia, db)
        return experiencia_creada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    

@router.put('/experiencia', tags=["Experiencia"])
async def ruta_actualizar_experiencia(experiencia: ActualizarExperiencia, db:Session= Depends(get_db)):
    try:
        experiencia_actualizada = actualizar_experiencia(experiencia, db)
        return experiencia_actualizada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    

@router.delete('/experiencia/{id_experiencia}', tags=["Experiencia"])
async def ruta_eliminar_experiencia(id_experiencia: int, db: Session = Depends(get_db)):
    try:
        experiencia_eliminada = eliminar_experiencia(id_experiencia, db)
        return experiencia_eliminada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
