from app.modules.main import main_routes
from app.modules.vacante import vacante_routes
from app.modules.perfil_postulante import perfil_postulante_routes
from app.modules.postulacion import postulacion_routes
from app.modules.auth import auth_routes
from app.modules.hoja_de_vida import hoja_de_vida_routes

def include_routes(app):
    app.include_router(main_routes.router, tags=["Principal"])
    app.include_router(vacante_routes.router, tags=["Vacantes"])
    app.include_router(perfil_postulante_routes.router, tags=["Perfil Postulante"])
    app.include_router(postulacion_routes.router, tags=["Postulation"])
    app.include_router(auth_routes.router, tags=["Auth"])
    app.include_router(hoja_de_vida_routes.router, tags=["Hoja de vida"])
