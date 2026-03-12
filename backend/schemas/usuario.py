from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    username: str
    senha: str
    role: str


class UsuarioLogin(BaseModel):
    username: str
    senha: str