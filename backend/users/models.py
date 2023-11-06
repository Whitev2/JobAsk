from sqlalchemy import Column, String, TIMESTAMP, BOOLEAN, text, DateTime

from database.postgres import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, unique=True)

    username = Column(String)
    email = Column(String, unique=True)

    is_verified = Column(BOOLEAN, default=False)
