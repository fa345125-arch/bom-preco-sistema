from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# modelo de dados
class Funcionario(BaseModel):
    nome: str
    cargo: str
    salario: float


# listar funcionarios
@router.get("/funcionarios")
def listar_funcionarios():
    return {"mensagem": "Lista de funcionários"}


# cadastrar funcionario
@router.post("/funcionarios")
def criar_funcionario(funcionario: Funcionario):
    return {
        "mensagem": "Funcionário criado",
        "dados": funcionario
    }