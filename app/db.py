from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

sql_db_url = "sqlite:///articles.db"

engine = create_engine(sql_db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass