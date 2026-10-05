from app.domain.habito import Habito

_habitos: dict[int, Habito] = {}
_contador_id = 0


def guardar(db: Session, habito: Habito) -> Habito:
    db.add(habito)
    db.commit()
    db.refresh(habito)
    return habito


def listar(db: Session) -> list[Habito]:
    return list(db.scalars(select(Habito).order_by(Habito.id)).all())


def obtener(db: Session, habito_id: int) -> Habito | None:
    return db.get(Habito, habito_id)


def listar_por_usuario(db: Session, usuario_id: int) -> list[Habito]:
    consulta = select(Habito).where(Habito.usuario_id == usuario_id)
    return list(db.scalars(consulta).all())


def actualizar(db: Session, habito: Habito) -> Habito:
    db.commit()
    db.refresh(habito)
    return habito


def eliminar(habito_id: int) -> bool:
    return _habitos.pop(habito_id, None) is not None


def existe(db: Session, habito_id: int) -> bool:
    return obtener(db, habito_id) is not None