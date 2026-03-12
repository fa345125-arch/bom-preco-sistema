from fastapi import FastAPI

app = FastAPI(title="Sistema Bom Preço")

@app.get("/")
def home():
    return {"mensagem": "Sistema interno Bom Preço funcionando"}