from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import Base, Engine
from app import routes

Base.metadata.create_all(bind=Engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes.include_routes(app)
