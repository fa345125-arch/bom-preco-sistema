from pydantic import BaseModel
from datetime import date


class CandidatoCreate(BaseModel):

    nome: str
    telefone: str
    email: str
    cidade: str
    experiencia: str
    data_cadastro: date


class CandidatoResponse(CandidatoCreate):

    id: int
    status: str

    class Config:
        from_attributes = True