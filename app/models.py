from sqlalchemy import Column, Integer, String, Text
from db import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    url = Column
    category = Column(String(30))
    notes = Column(Text, nullable=True)

    