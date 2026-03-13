from sqlalchemy import Column, Integer, String, Float, Date
from backend.database import Base


class Vaga(Base):

    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String)

    departamento = Column(String)

    descricao = Column(String)

    salario = Column(Float)

    data_abertura = Column(Date)

    status = Column(String, default="aberta")