from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class RegistroPonto(BaseModel):
    funcionario_id: int
    tipo: str

@router.post("/ponto")
def registrar_ponto(registro: RegistroPonto):

    data_hora = datetime.now()

    return {
        "mensagem": "Ponto registrado",
        "funcionario": registro.funcionario_id,
        "tipo": registro.tipo,
        "data_hora": data_hora
    }