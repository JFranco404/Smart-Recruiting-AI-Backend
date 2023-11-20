from modules.main import main_routes
from modules.vacante import vacante_routes


def include_routes(app):
    app.include_router(main_routes.router, tags=["Main"])
    app.include_router(vacante_routes.router, tags=["Vacancy"])
