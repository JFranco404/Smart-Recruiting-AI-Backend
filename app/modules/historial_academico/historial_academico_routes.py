from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.historial_academico.historial_academico_services import *
from app.modules.historial_academico.historial_academico_models import *
from app.modules.educacion_por_perfil_postulante.educacion_por_perfil_postulante_services import obtener_educacion_por_perfil_postulante_por_postulante_id 
from app.modules.auth.auth_services import autorizar_postulante

router = APIRouter()

@router.get("/historial-academico", tags=["Historial Academico"])
async def ruta_obtener_historial_academico_por_postulante_id(payload = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        educacion = obtener_educacion_por_perfil_postulante_por_postulante_id(
            payload.get("id_usr"), db)
        return educacion

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post('/historial-academico', tags=["Historial Academico"])
async def ruta_crear_historial_academico(historial: DatosHistorialAcademico, db:Session = Depends(get_db)):
    try:
        historial_creado = crear_historial_academico(historial, db)
        return historial_creado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    
@router.put('/historial-academico', tags=["Historial Academico"])
async def ruta_actualizar_historial_academico(historial: ActualizarHistorialAcademico, db:Session= Depends(get_db)):
    try:
        historial_actualizado = actualizar_historial_academico(historial, db)
        return historial_actualizado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    
@router.delete('/historial-academico/{id_historial}', tags=["Historial Academico"])
async def ruta_eliminar_historial_academico(id_historial: int, db: Session = Depends(get_db)):
    try:
        historial_eliminado = eliminar_historial_academico(id_historial, db)
        return historial_eliminado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
