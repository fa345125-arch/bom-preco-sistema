from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.services.calculo_folha import calcular_folha
from database.database import SessionLocal
from backend.models.folha_pagamento import FolhaPagamento
from backend.schemas.folha_pagamento import FolhaCreate

router = APIRouter(prefix="/folha", tags=["Folha"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def criar_folha(dados: FolhaCreate, db: Session = Depends(get_db)):

    calculo = calcular_folha(
        dados.salario_base,
        dados.hora_extra_60,
        dados.hora_extra_100,
        0,
        dados.descontos
    )

    folha = FolhaPagamento(
        funcionario_id=dados.funcionario_id,
        mes=dados.mes,
        ano=dados.ano,
        salario_base=dados.salario_base,
        hora_extra_60=dados.hora_extra_60,
        hora_extra_100=dados.hora_extra_100,
        adicionais=0,
        descontos=dados.descontos,
        inss=calculo["inss"],
        liquido=calculo["liquido"]
    )

    db.add(folha)
    db.commit()
    db.refresh(folha)

    return folha

@router.get("/")
def listar_folhas(db: Session = Depends(get_db)):

    return db.query(FolhaPagamento).all()