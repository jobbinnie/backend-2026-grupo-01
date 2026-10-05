from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.domain.categoria import Categoria
from app.repositories import categoria_repository
from app.schemas.categoria_schema import CategoriaCreate


def listar_categorias(db: Session):
    return categoria_repository.listar(db)


def crear_categoria(db: Session, datos: CategoriaCreate):
    categoria_existente = next(
        (
            categoria
            for categoria in categoria_repository.listar(db)
            if categoria.nombre.casefold() == datos.nombre.casefold()
        ),
        None,
    )

    if categoria_existente is not None:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una categoría con ese nombre.",
        )

    categoria = Categoria(
        id=0,
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )

    return categoria_repository.guardar(db, categoria)
