from sqlalchemy.orm import Session
from app.modules.postulacion.postulacion_database_model import Postulacion


def eliminar_postulacion(postulacion_id: int, db: Session) -> Postulacion:
    """
    Elimina una postulacion.

    Raises:
        ValueError: Cuando la postulacion no es encontrada.
    """

    postulacion = db.query(Postulacion).filter(
        Postulacion.id == postulacion_id).first()
    if not postulacion:
        raise ValueError("La postulacion no existe")

    db.delete(postulacion)
    db.commit()
    db.refresh(postulacion)

    return postulacion


def obtener_postulacion_por_vacante_id(vacante_id: int, db: Session) -> Postulacion:
    """
    Obtiene una postulacion por vacante_id.
    """

    postulacion = db.query(Postulacion).filter(
        Postulacion.id_vacante == vacante_id).first()
    if not postulacion:
        return None

    return postulacion


def eliminar_postulacion_por_vacante_id(vacante_id: int, db: Session) -> Postulacion:
    """
    Elimina una postulacion.
    """

    postulacion = obtener_postulacion_por_vacante_id(vacante_id, db)

    if postulacion:
        db.delete(postulacion)
        db.commit()
        db.refresh(postulacion)
        return postulacion
    else:
        return None
