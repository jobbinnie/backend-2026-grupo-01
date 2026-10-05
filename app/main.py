from fastapi import FastAPI
from app.database import Base, engine
from app.domain import categoria, habito, registro_habito, usuario
from app.routers import usuarios, registros, habitos, categorias 
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuarios.router)
app.include_router(registros.router)
app.include_router(habitos.router)
app.include_router(categorias.router)  

