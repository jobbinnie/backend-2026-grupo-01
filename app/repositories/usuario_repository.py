from app.domain.usuario import Usuario

_usuarios: dict[int, Usuario] = {}
_contador_id = 0


def guardar(db: Session, usuario: Usuario) -> Usuario:
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def listar(db: Session) -> list[Usuario]:
    return list(db.scalars(select(Usuario).order_by(Usuario.id)).all())


def obtener(db: Session, usuario_id: int) -> Usuario | None:
    return db.get(Usuario, usuario_id)


def actualizar(db: Session, usuario: Usuario) -> Usuario:
    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar(db: Session, usuario: Usuario) -> None:
    db.delete(usuario)
    db.commit()


def existe(db: Session, usuario_id: int) -> bool:
    return obtener(db, usuario_id) is not None

def obtener_por_email(db: Session, email: str) -> Usuario | None:
    return db.scalar(select(Usuario).where(Usuario.email == email))

    return None