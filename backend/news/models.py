from sqlalchemy import Column, String, TIMESTAMP, BOOLEAN, text, DateTime, Integer, Index
from datetime import datetime
from database.postgres import Base



class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    title = Column(String)
    body = Column(String)

    image_path = Column(String)

    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
