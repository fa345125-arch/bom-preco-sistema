from pydantic import BaseModel


class FuncionarioCreate(BaseModel):
    nome: str
    cargo: str
    salario: float