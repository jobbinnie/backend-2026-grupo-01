from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.include_router(usuarios.router)

class usuario(BaseModel):
    id: int
    name: str
    email: str
    fecha_registro: datetime = datetime.now()

class Habito(BaseModel):
    id: int
    usuario_id: int
    categoria: str
    nombre: str
    frecuancia_semanal: int
    estado: bool
    fecha_creacion: datetime = datetime.now()

class registro_habito(BaseModel):
    id: int
    habito_id: int
    fecha_registro: datetime = datetime.now()
    estado: bool
    nota: str

class categoria(BaseModel):
    id: int
    nombre: str
    descripcion: str



@app.get("/usuario")
async def Usuario():
    return {"message": "Hello, World!"}

@app.post("/usuario")
async def create_usuario(usuario: usuario):
    return {"message": "El usuario fue creado exitosamente", "usuario": usuario}

@app.delete("/usuario")
async def delete_usuario(usuario_id: int):
    return {"message": f"El usuario con el id {usuario_id} fue eliminado exitosamente"}

@app.patch("/usuario")
async def upgrade_usuario(usuario_id: int, usuario: usuario):
    return {"message": f"El usuario con el id {usuario_id} fue actualizado exitosamente", "usuario": usuario}