from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.vacante.vacante_services import *
from app.modules.vacante.vacante_models import CrearVacante

router = APIRouter()


@router.get("/vacantes/{user_recruiter_id}", tags=["Vacancy"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(user_recruiter_id: int, db: Session = Depends(get_db)):
    try:
        vacantes = obtener_vacantes_por_usuario_reclutador_id(
            user_recruiter_id, db)
        return vacantes

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post("/vacantes", tags=["Vacancy"])
async def ruta_crear_vacante(vacante: CrearVacante, db: Session = Depends(get_db)):
    try:
        vacante_creada = crear_vacante(vacante, db)
        return vacante_creada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))
