from pydantic import BaseModel
from datetime import date


class VagaCreate(BaseModel):

    titulo: str
    departamento: str
    descricao: str
    salario: float
    data_abertura: date


class VagaResponse(VagaCreate):

    id: int
    status: str

    class Config:
        from_attributes = True