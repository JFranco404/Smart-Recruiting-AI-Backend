from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.vacante.vacante_services import *
from app.modules.vacante.vacante_models import DatosVacante, ActualizarVacante, FiltrosVacante

router = APIRouter()


@router.get("/vacantes/{id_usuario_reclutador}", tags=["Vacancy"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(id_usuario_reclutador: int, db: Session = Depends(get_db)):
    try:
        vacantes = obtener_vacantes_por_usuario_reclutador_id(
            id_usuario_reclutador, db)
        return vacantes

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post("/vacantes", tags=["Vacancy"])
async def ruta_crear_vacante(vacante: DatosVacante, db: Session = Depends(get_db)):
    try:
        vacante_creada = crear_vacante(vacante, db)
        return vacante_creada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.put("/vacantes/", tags=["Vacancy"])
async def ruta_actualizar_vacante(vacante: ActualizarVacante, db: Session = Depends(get_db)):
    try:
        vacante_actualizada = actualizar_vacante(vacante, db)
        return vacante_actualizada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.delete("/vacantes/{id_vacante}", tags=["Vacancy"])
async def ruta_eliminar_vacante(id_vacante: int, db: Session = Depends(get_db)):
    try:
        vacante_eliminada = eliminar_vacante(id_vacante, db)
        return vacante_eliminada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.post("/vacantes_filtradas/", tags=["Vacancy"])
async def ruta_obtener_vacante_por_filtro(filtros: FiltrosVacante, db: Session = Depends(get_db)):
    try:
        vacantes = obtener_vacante_por_filtro(filtros, db)
        return vacantes

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
