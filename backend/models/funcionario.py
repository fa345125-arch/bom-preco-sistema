from sqlalchemy import Column, Integer, String, Float
from database.database import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cargo = Column(String)
    salario = Column(Float)
    status = Column(String)