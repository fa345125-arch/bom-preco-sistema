from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base


class RegistroPonto(Base):
    __tablename__ = "ponto"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer)
    tipo = Column(String)
    data_hora = Column(DateTime)
    origem = Column(String)