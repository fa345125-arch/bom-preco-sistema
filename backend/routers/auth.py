from backend.auth_jwt import criar_token
from backend.security import gerar_hash_senha, verificar_senha
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioLogin

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    dados = user.dict()
    dados["senha"] = gerar_hash_senha(dados["senha"])

    novo = Usuario(**dados)
    db.add(novo)
    db.commit()

    return {"status": "usuario criado"}


@router.post("/login")
def login(user: UsuarioLogin, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(
        Usuario.username == user.username
    ).first()

    if not usuario:
        return {"erro": "usuario não encontrado"}

    if not verificar_senha(user.senha, usuario.senha):
        return {"erro": "senha incorreta"}

    token = criar_token({"sub": usuario.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }