from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

url_object = URL.create(
    "postgresql",
    host="smartrecruitaiserver.postgres.database.azure.com",
    username="franco@smartrecruitaiserver",
    password="xL9racipi0of",
    database="SmartRecruitAiDB",
)
Base = declarative_base()
Engine = create_engine(url_object, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
