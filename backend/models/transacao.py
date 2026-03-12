from sqlalchemy import Column, Integer, String, Float, Date
from database.database import Base


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    descricao = Column(String)
    categoria = Column(String)
    tipo = Column(String)
    valor = Column(Float)