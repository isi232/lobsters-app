import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pipeline.models import Base

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "lobsters.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()
