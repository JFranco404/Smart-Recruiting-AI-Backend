from app.modules.usuario.usuario_database_model import Usuario
from sqlalchemy.orm import Session


def obtener_usuario_por_id(user_id: int, db: Session):
    return db.query(Usuario).filter(Usuario.id == user_id).first()
