import bcrypt
import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.modules.usuario.usuario_database_model import Usuario
from app.modules.usuario.rol_database_model import Rol
from app.modules.auth.auth_models import Auth_login, Auth_register
from fastapi import Depends, Request, HTTPException, status

SECRET_KEY = "46a88a90c0c6c3f240c0b6f198ce59700752e0ba900b0661d1b9ae41e08d5ef5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30


def login_service(auth: Auth_login, db: Session):
    email_usuario = consultar_usuario_por_email(auth, db)
    rol_usuario = consultar_rol_del_usuario(auth, db)
    if email_usuario is not None and validar_credenciales(auth, email_usuario.passwd):
        return crear_token(email_usuario, rol_usuario)
    else:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")


def consultar_usuario_por_email(auth: Auth_login, db: Session) -> Usuario:
    return db.query(Usuario).filter(Usuario.correo == auth.correo).first()


def consultar_rol_del_usuario(auth: Auth_login, db: Session) -> Rol:
    user = consultar_usuario_por_email(auth, db)
    rol = db.query(Rol).filter(user.rol == Rol.id).first()
    return rol

def validar_credenciales(auth: Auth_login, hashed: str) -> str :
    return bcrypt.checkpw(to_encode_utf8(auth.passwd), to_encode_utf8(hashed))


def to_encode_utf8(str) -> str:
    return str.encode('utf8')


def crear_token(usuario: Usuario, rol: Rol):
    expires_delta = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode = {"id_usr": usuario.id, "mail": usuario.correo, "rol": rol.id}
    to_encode.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def registrar_usuario(auth: Auth_register, db: Session) -> bool:
    
    usuario = Usuario(
        correo=auth.correo,
        passwd=bcrypt.hashpw(auth.passwd.encode('utf8'), bcrypt.gensalt()),
        rol = auth.rol_id
    )

    if consultar_usuario_por_email(auth, db):
        raise HTTPException(status_code=400, detail="Este usuario ya está registrado")
    

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


def obtener_header(request: Request):
    try: 
        authorization_header = request.headers.get("Authorization").split(" ")[1]
        if not authorization_header:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autorización no válido",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return authorization_header
    except:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autorización no válido",
                headers={"WWW-Authenticate": "Bearer"},
            )


def autorizar_usuario(token : str, rol_requerido : int = 0):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    rol: str = payload.get('rol')

    if rol != rol_requerido:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para acceder a este recurso",
        )

    return payload


def autorizar_postulante(token: str = Depends(obtener_header)):
    return autorizar_usuario(token, 2)

def autorizar_reclutador(token: str = Depends(obtener_header)):
    return autorizar_usuario(token, 1)