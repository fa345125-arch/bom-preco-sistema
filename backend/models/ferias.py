from sqlalchemy import Column, Integer, Date, String
from database.database import Base


class Ferias(Base):
    __tablename__ = "ferias"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    dias = Column(Integer)
    status = Column(String)