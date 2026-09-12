from pydantic import BaseModel, Field
 
 
class CategoriaCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)     
    descripcion: str = Field(..., max_length=200)
 
 
class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str