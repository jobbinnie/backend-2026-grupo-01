from datetime import datetime
 
from pydantic import BaseModel, EmailStr, Field
 
 
class UsuarioCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=60)   
    email: EmailStr                                       
 
 
class UsuarioUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=60)
    email: EmailStr | None = None
 
 
class UsuarioResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    name: str
    email: EmailStr
    fecha_registro: datetime
 