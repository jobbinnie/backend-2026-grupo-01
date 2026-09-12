from fastapi import APIRouter

from schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse,
)
from services import categoria_service


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.get( "/", response_model=list[CategoriaResponse],)
def listar_categorias():
    return categoria_service.listar_categorias()


@router.post( "/", response_model=CategoriaResponse, status_code=201,)
def crear_categoria(datos: CategoriaCreate):
    return categoria_service.crear_categoria(datos)