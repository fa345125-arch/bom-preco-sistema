from fastapi import FastAPI
from backend.routers import funcionarios

app = FastAPI(title="Sistema Bom Preço")

app.include_router(funcionarios.router)

@app.get("/")
def home():
    return {"mensagem": "Sistema interno Bom Preço funcionando"}