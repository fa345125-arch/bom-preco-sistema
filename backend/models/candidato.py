from sqlalchemy import Column, Integer, String, Date
from backend.database import Base


class Candidato(Base):

    __tablename__ = "candidatos"

    id = Column(Integer, primary_key=True)

    nome = Column(String)

    telefone = Column(String)

    email = Column(String)

    cidade = Column(String)

    experiencia = Column(String)

    data_cadastro = Column(Date)

    status = Column(String, default="novo")