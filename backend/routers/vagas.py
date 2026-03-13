from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.vaga import Vaga
from backend.schemas.vaga import VagaCreate

router = APIRouter(prefix="/vagas", tags=["Vagas"])


@router.post("/")
def criar_vaga(vaga: VagaCreate, db: Session = Depends(get_db)):

    nova = Vaga(**vaga.dict())

    db.add(nova)

    db.commit()

    db.refresh(nova)

    return nova


@router.get("/")
def listar_vagas(db: Session = Depends(get_db)):

    return db.query(Vaga).all()