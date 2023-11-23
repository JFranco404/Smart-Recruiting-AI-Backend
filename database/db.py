from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

connection_string = URL.create(
    'postgresql',
    username='yoniervasquezmarin',
    password='6XNzkUu7BMwO',
    host='ep-fragrant-base-38617296.us-east-2.aws.neon.tech',
    database='SmartRecruitAiDB',
)
Base = declarative_base()
Engine = create_engine(connection_string, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
