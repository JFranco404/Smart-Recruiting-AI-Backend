from fastapi import FastAPI
from database.db import Base, Engine
import routes

Base.metadata.create_all(bind=Engine)
app = FastAPI()

routes.include_routes(app)
