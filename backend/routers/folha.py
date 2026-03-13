from fastapi import APIRouter
from backend.services.folha_pdf import gerar_recibo

router = APIRouter(prefix="/folha", tags=["Folha"])


@router.get("/recibo/{nome}")
def gerar(nome: str):

    funcionario = {
        "nome": nome,
        "salario": 5000,
        "liquido": 4500
    }

    arquivo = gerar_recibo(funcionario)

    return {"arquivo": arquivo}