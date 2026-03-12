from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date

router = APIRouter()

# modelo da transação
class Transacao(BaseModel):
    data: date
    descricao: str
    tipo: str
    valor: float

# registrar transação
@router.post("/transacoes")
def registrar_transacao(transacao: Transacao):

    return {
        "mensagem": "Transação registrada",
        "dados": transacao
    }

# consultar saldo
@router.get("/saldo")
def consultar_saldo():

    return {
        "saldo": "Função de cálculo será implementada"
    }