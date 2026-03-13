from pydantic import BaseModel


class FolhaCreate(BaseModel):

    funcionario_id: int
    mes: int
    ano: int

    salario_base: float
    hora_extra_60: float
    hora_extra_100: float

    descontos: float
    liquido: float


class FolhaResponse(FolhaCreate):

    id: int

    class Config:
        orm_mode = True