from fastapi import FastAPI
from backend.routers import funcionarios
from backend.routers import pontos
from backend.routers import financeiro
from backend.routers import ferias
from backend.routers import auth
from backend.routers import folha
from backend.routers import vagas
from backend.routers import candidatos


app = FastAPI(title="Sistema Bom Preço")

app.include_router(funcionarios.router)
app.include_router(pontos.router)
app.include_router(financeiro.router)
app.include_router(ferias.router)
app.include_router(auth.router)
app.include_router(vagas.router)
app.include_router(candidatos.router)

@app.get("/")
def home():
    return {"mensagem": "Sistema interno Bom Preço funcionando"}