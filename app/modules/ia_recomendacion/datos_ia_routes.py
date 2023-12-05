from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.ia_recomendacion.datos_ia_service import informacion_ia
from app.modules.auth.auth_services import autorizar_postulante

router = APIRouter()


@router.get("/ia-recommendation/", tags=["Recomendacion ia"])
async def ruta_obtener_recomendacion(payload = Depends(autorizar_postulante), db: Session = Depends(get_db)):
    try:

        vacantes = informacion_ia(
            payload.get("id_usr"), db)
        return vacantes

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


