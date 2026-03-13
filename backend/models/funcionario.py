from pydantic import BaseModel
from datetime import date

class FuncionarioCreate(BaseModel):

    nome: str
    cargo: str
    departamento: str
    salario: float
    data_admissao: date


class FuncionarioResponse(FuncionarioCreate):

    id: int
    status: str

    class Config:
        orm_mode = True