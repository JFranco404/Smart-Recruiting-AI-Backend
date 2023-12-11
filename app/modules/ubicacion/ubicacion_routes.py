from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from .ubicacion_services import obtener_todas_las_ubicaciones
from app.modules.auth.auth_services import autorizar_todos

router = APIRouter()


@router.get("/ubicaciones", tags=["Ubicacion"])
async def ruta_obtener_todas_las_ubicaciones(payload=Depends(autorizar_todos), db: Session = Depends(get_db)):
    try:
        ubicaciones = obtener_todas_las_ubicaciones(db)
        return ubicaciones

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
