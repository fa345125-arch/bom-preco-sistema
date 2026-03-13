from sqlalchemy import Column, Integer, String, Float, Date
from database.database import Base


class Funcionario(Base):

    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)
    cpf = Column(String)

    email = Column(String)
    telefone = Column(String)

    cargo = Column(String)
    departamento = Column(String)

    salario = Column(Float)

    carga_horaria = Column(Integer)

    data_admissao = Column(Date)

    status = Column(String, default="ativo")