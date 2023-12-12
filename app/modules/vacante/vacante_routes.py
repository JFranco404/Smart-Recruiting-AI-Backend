from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from app.modules.vacante.vacante_services import *
from app.modules.vacante.vacante_models import DatosVacante, ActualizarVacante, FiltrosVacante
from app.modules.auth.auth_services import autorizar_postulante, autorizar_reclutador

router = APIRouter()


@router.get("/vacantes-del-reclutador", tags=["Vacantes"])
async def ruta_obtener_vacantes_por_usuario_reclutador_id(payload=Depends(autorizar_reclutador), db: Session = Depends(get_db)):
    try:
        vacantes = obtener_vacantes_por_usuario_reclutador_id(
            payload.get('id_usr'), db)
        return vacantes

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.get("/vacantes/{id}", tags=["Vacantes"])
async def ruta_obtener_vacante_por_id(id: int, db: Session = Depends(get_db)):
    try:
        vacante = obtener_vacante_por_id(id, db)
        return vacante

    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post("/vacantes", tags=["Vacantes"])
async def ruta_crear_vacante(vacante: DatosVacante, payload=Depends(autorizar_reclutador), db: Session = Depends(get_db)):
    try:
        vacante_creada = crear_vacante(vacante, db)
        return vacante_creada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.put("/vacantes/", tags=["Vacantes"])
async def ruta_actualizar_vacante(vacante: ActualizarVacante, payload=Depends(autorizar_reclutador), db: Session = Depends(get_db)):
    try:
        vacante_actualizada = actualizar_vacante(vacante, db)
        return vacante_actualizada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.delete("/vacantes/{id_vacante}", tags=["Vacantes"])
async def ruta_eliminar_vacante(id_vacante: int, payload=Depends(autorizar_reclutador), db: Session = Depends(get_db)):
    try:
        vacante_eliminada = eliminar_vacante(id_vacante, db)
        return vacante_eliminada

    except ValueError as error:
        return HTTPException(status_code=400, detail=str(error))


@router.post("/vacantes_filtradas/", tags=["Vacantes"])
async def ruta_obtener_vacante_por_filtro(filtros: FiltrosVacante, db: Session = Depends(get_db)):
    try:
        vacantes = obtener_vacante_por_filtro(filtros, db)
        return vacantes

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
