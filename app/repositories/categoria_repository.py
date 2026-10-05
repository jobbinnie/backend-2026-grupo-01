from app.domain.categoria import Categoria

_categorias: dict[int, Categoria] = {}
_contador_id = 0


def guardar(db: Session, categoria: Categoria) -> Categoria:
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


def listar(db: Session) -> list[Categoria]:
    return list(db.scalars(select(Categoria).order_by(Categoria.id)).all())


def obtener(db: Session, categoria_id: int) -> Categoria | None:
    return db.get(Categoria, categoria_id)


def existe(db: Session, categoria_id: int) -> bool:
    return obtener(db, categoria_id) is not None