from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.candidato import Candidato
from backend.schemas.candidato import CandidatoCreate

router = APIRouter(prefix="/candidatos", tags=["Candidatos"])


@router.post("/")
def criar_candidato(candidato: CandidatoCreate, db: Session = Depends(get_db)):

    novo = Candidato(**candidato.dict())

    db.add(novo)

    db.commit()

    db.refresh(novo)

    return novo


@router.get("/")
def listar_candidatos(db: Session = Depends(get_db)):

    return db.query(Candidato).all()