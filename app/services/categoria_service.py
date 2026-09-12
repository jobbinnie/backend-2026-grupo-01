from app.domain.categoria import Categoria
from app.repositories import categoria_repository
from app.schemas.categoria_schema import CategoriaCreate


def listar_categorias():
    return categoria_repository.listar()


def crear_categoria(datos: CategoriaCreate):
    categoria = Categoria(
        id=0,
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )

    return categoria_repository.guardar(categoria)
