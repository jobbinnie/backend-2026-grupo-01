from fastapi import FastAPI
from routers import usuarios, registros, habitos, categorias 
app = FastAPI()

app.include_router(usuarios.router)
app.include_router(registros.router)
app.include_router(habitos.router)
app.include_router(categorias.router)  

