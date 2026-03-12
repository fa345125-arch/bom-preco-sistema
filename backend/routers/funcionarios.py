from fastapi import APIRouter
from backend.schemas.funcionario import FuncionarioCreate

router = APIRouter()

funcionarios = []

@router.post("/funcionarios")
def criar_funcionario(funcionario: FuncionarioCreate):

    funcionarios.append(funcionario)

    return {
        "mensagem": "Funcionário cadastrado",
        "dados": funcionario
    }


@router.get("/funcionarios")
def listar_funcionarios():

    return funcionarios