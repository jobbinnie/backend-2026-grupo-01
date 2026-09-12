from fastapi import FastAPI
from Routers import usuarios  
app = FastAPI()

app.include_router(usuarios.router)

