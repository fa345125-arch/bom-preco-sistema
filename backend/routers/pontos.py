from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from database.database import SessionLocal
from backend.models.ponto import Ponto
from analytics.compliance import analisar_jornada

router = APIRouter(prefix="/ponto", tags=["Ponto"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def registrar_ponto(funcionario_id: int, tipo: str, db: Session = Depends(get_db)):

    registro = Ponto(
        funcionario_id=funcionario_id,
        tipo=tipo,
        data_hora=datetime.now()
    )

    db.add(registro)
    db.commit()

    return {
        "mensagem": "Ponto registrado",
        "funcionario": funcionario_id,
        "tipo": tipo
    }


@router.get("/")
def listar_pontos(db: Session = Depends(get_db)):

    return db.query(Ponto).all()
    @router.get("/funcionario/{funcionario_id}")
def relatorio_funcionario(funcionario_id: int, db: Session = Depends(get_db)):

    registros = db.query(Ponto).filter(
        Ponto.funcionario_id == funcionario_id
    ).all()

    resultado = []

    for r in registros:

        horas = None

        if r.entrada and r.saida:
            horas = (r.saida - r.entrada).total_seconds() / 3600

        resultado.append({
            "entrada": r.entrada,
            "saida": r.saida,
            "horas_trabalhadas": horas
        })

    return resultado