from app.modules.usuario.usuario_database_model import Usuario
from sqlalchemy.orm import Session


def obtener_usuario_por_id(user_id: int, db: Session):
    return db.query(Usuario).filter(Usuario.id == user_id).first()


def actualizar_usuario(usuario: Usuario, db: Session) -> bool:
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario.id).first()

    if usuario_db is None:
        return False

    if usuario.cedula is not None and usuario.cedula != 0 and usuario.cedula != '':
        usuario_db.cedula = usuario.cedula

    if usuario.nombres is not None and usuario.nombres != '':
        usuario_db.nombres = usuario.nombres

    if usuario.apellidos is not None and usuario.apellidos != '':
        usuario_db.apellidos = usuario.apellidos

    if usuario.fecha_nacimiento is not None and usuario.fecha_nacimiento != '':
        usuario_db.fecha_nacimiento = usuario.fecha_nacimiento

    if usuario.lugar_residencia is not None and usuario.lugar_residencia != 0 and usuario.lugar_residencia != '':
        usuario_db.lugar_residencia = usuario.lugar_residencia

    if usuario.correo is not None and usuario.correo != '':
        usuario_db.correo = usuario.correo

    if usuario.rol is not None and usuario.rol != 0 and usuario.rol != '':
        usuario_db.rol = usuario.rol

    if usuario.passwd is not None and usuario.passwd != '':
        usuario_db.passwd = usuario.passwd

    db.commit()
    db.refresh(usuario_db)
    return True
