from app.modules.main import main_routes
from app.modules.vacante import vacante_routes
from app.modules.perfil_postulante import perfil_postulante_routes
from app.modules.postulacion import postulacion_routes
from app.modules.experiencia import experiencia_routes

def include_routes(app):
    app.include_router(main_routes.router, tags=["Principal"])
    app.include_router(vacante_routes.router, tags=["Vacantes"])
    app.include_router(perfil_postulante_routes.router, tags=["Perfil Postulante"])
    app.include_router(postulacion_routes.router, tags=["Postulation"])
    app.include_router(experiencia_routes.router, tags=["Experiencia"])
