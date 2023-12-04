from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.perfil_postulante.perfil_postulante_services import *
from app.modules.perfil_postulante.perfil_postulante_models import DatosPostulante
from  app.modules.auth.auth_services import autorizar_postulante


router = APIRouter()


@router.get("/perfil-postulante", tags=["Perfil Postulante"])
async def ruta_obtener_perfil_postulante_por_usuario_id(payload = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        perfil_postulante = obtener_perfil_postulante_por_usuario_id(
            payload.get("id_usr"), db)
        return perfil_postulante

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))

@router.post('/perfil-postulante', tags=["Perfil Postulante"])
async def ruta_crear_perfil_postulante(postulante:DatosPostulante, db:Session= Depends(get_db)):
    try:
        postulante_creado = crear_postulante(postulante, db)
        return postulante_creado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    
@router.put('/perfil-postulante', tags=["Perfil Postulante"])
async def ruta_actualizar_perfil_postulante(postulante:ActualizarPerfilPostulante, db:Session= Depends(get_db)):
    try:
        postulante_actualizado = actualizar_postulante(postulante, db)
        return postulante_actualizado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
    
@router.delete('/perfil-postulante', tags=["Perfil Postulante"])
async def ruta_eliminar_postulante(payload = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:
        postulante_eliminado = eliminar_postulante(payload.get("id_usr"), db)
        return postulante_eliminado

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
