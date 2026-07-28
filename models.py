from sqlalchemy import Column, Integer, String
from database import Base

class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    author = Column(String, default="anonymous")
    word_count = Column(Integer)