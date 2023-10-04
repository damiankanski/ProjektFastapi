from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings as settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}@{settings.database_password}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()