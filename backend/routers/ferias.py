from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class FeriasCreate(BaseModel):
    funcionario_id: int
    data_inicio: date
    data_fim: date
    dias: int


@router.post("/ferias")
def registrar_ferias(ferias: FeriasCreate):

    return {
        "mensagem": "Férias registradas",
        "dados": ferias
    }


@router.get("/ferias")
def listar_ferias():

    return {"mensagem": "Lista de férias"}