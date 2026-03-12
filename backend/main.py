from fastapi import FastAPI
from backend.routers import funcionarios
from backend.routers import ponto
from backend.routers import financeiro

app = FastAPI(title="Sistema Bom Preço")

app.include_router(funcionarios.router)
app.include_router(ponto.router)
app.include_router(financeiro.router)

@app.get("/")
def home():
    return {"mensagem": "Sistema interno Bom Preço funcionando"}