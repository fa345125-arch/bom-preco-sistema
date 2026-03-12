from fastapi import FastAPI
from backend.routers import funcionarios
from backend.routers import ponto
from backend.routers import financeiro
from backend.routers import ferias
from routers import auth

app = FastAPI(title="Sistema Bom Preço")

app.include_router(funcionarios.router)
app.include_router(ponto.router)
app.include_router(financeiro.router)
app.include_router(ferias.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"mensagem": "Sistema interno Bom Preço funcionando"}