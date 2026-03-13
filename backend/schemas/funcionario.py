from pydantic import BaseModel
from datetime import date


class FuncionarioCreate(BaseModel):

    nome: str
    cpf: str
    email: str
    telefone: str

    cargo: str
    departamento: str

    salario: float
    carga_horaria: int

    data_admissao: date


class FuncionarioResponse(FuncionarioCreate):

    id: int
    status: str

    class Config:
        orm_mode = True