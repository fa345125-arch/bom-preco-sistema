from sqlalchemy import Column, Integer, String
from database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    senha = Column(String)
    role = Column(String)  # admin, rh, funcionario