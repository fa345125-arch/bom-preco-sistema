from fastapi import APIRouter

router = APIRouter()

@router.get("/funcionarios")
def listar_funcionarios():
    return {"mensagem": "Lista de funcionários"}