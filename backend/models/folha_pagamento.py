from sqlalchemy import Column, Integer, Float, ForeignKey
from database.database import Base


class FolhaPagamento(Base):

    __tablename__ = "folha_pagamento"

    id = Column(Integer, primary_key=True, index=True)

    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))

    mes = Column(Integer)
    ano = Column(Integer)

    salario_base = Column(Float)

    hora_extra_60 = Column(Float)
    hora_extra_100 = Column(Float)

    descontos = Column(Float)

    liquido = Column(Float)