from sqlalchemy import Column, Integer, String, Text
from db import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    url = Column(String)
    category = Column(String(30), nullable=False)
    notes = Column(Text, nullable=True)

    