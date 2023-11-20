from modules.usuario.usuario_database_model import Usuario


def obtener_usuario_por_id(user_id: int, db):
    return db.query(Usuario).filter(Usuario.id == user_id).first()
