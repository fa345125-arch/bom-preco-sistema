from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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

    folha = FolhaPagamento(**dados.dict())

    db.add(folha)
    db.commit()
    db.refresh(folha)

    return folha


@router.get("/")
def listar_folhas(db: Session = Depends(get_db)):

    return db.query(FolhaPagamento).all()