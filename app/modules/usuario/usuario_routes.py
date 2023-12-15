from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from app.modules.auth.auth_services import autorizar_todos
from .usuario_services import obtener_usuario_por_id, actualizar_usuario
from .usuario_models import Usuario

router = APIRouter()


@router.get("/usuario", tags=["Usuario"])
async def ruta_obtener_usuario_por_id(payload: dict = Depends(autorizar_todos), db: Session = Depends(get_db)):
    try:
        postulaciones = obtener_usuario_por_id(
            payload.get('id_usr'), db)
        return postulaciones

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.put("/usuario", tags=["Usuario"])
async def ruta_actualizar_usuario_por_id(usuario: Usuario, payload: dict = Depends(autorizar_todos), db: Session = Depends(get_db)):
    try:
        return actualizar_usuario(usuario, db)
    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
