from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class usuario(BaseModel):
    id: int
    name: str
    email: str

@app.get("/usuario")
async def Usuario():
    return {"message": "Hello, World!"}

@app.post("/usuario")
async def create_usuario(usuario: usuario):
    return {"message": "Usuario created successfully", "usuario": usuario}