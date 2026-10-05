from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse,
)
from app.services import categoria_service


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.get( "/", response_model=list[CategoriaResponse],)
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.listar_categorias(db)


@router.post( "/", response_model=CategoriaResponse, status_code=201,)
def crear_categoria(datos: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.crear_categoria(db, datos)