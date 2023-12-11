from typing import List
from sqlalchemy.orm import Session
from .ubicacion_database_model import Ubicacion


def obtener_todas_las_ubicaciones(db: Session) -> List[Ubicacion]:
    """
    Obtiene todas las ubicaciones de la base de datos.

    Returns:
        List[Ubicacion]: Lista de ubicaciones.
    """
    ubicaciones = db.query(Ubicacion).all()
    return ubicaciones
