from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
import modules.vacante.vacante_services as vacante_services

router = APIRouter()


@router.get("/vacantes/{user_recruiter_id}", tags=["Vacancy"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(user_recruiter_id: int, db: Session = Depends(get_db)):
    try:
        vacantes = vacante_services.obtener_vacantes_por_usuario_reclutador_id(
            user_recruiter_id, db)
        return vacantes

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))
