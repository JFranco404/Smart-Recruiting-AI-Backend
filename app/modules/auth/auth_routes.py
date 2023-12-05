from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from database.db import get_db
from app.modules.auth.auth_models import Auth_login, Auth_register
from app.modules.auth.auth_services import *

router = APIRouter()


@router.post("/auth/login", tags=["Auth"])
def login(auth: Auth_login, db: Session = Depends(get_db)):
    try:
        token = login_service(auth, db)
        return token
    except ValueError as error:
        return HTTPException(status_code=404, detail=str(error))


@router.post("/auth/registrarse", tags=["Auth"])
def register(auth: Auth_register, db: Session = Depends(get_db)):
    try:
        return registrar_usuario(auth, db)
    except:
        return HTTPException(status_code=404, detail="No se pudo registrar el usuario")
