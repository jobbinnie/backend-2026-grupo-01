from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.domain.usuario import Usuario
from app.repositories import usuario_repository
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate


def crear_usuario(db: Session, datos: UsuarioCreate):
    usuario_existente = usuario_repository.obtener_por_email(db, str(datos.email))
    if usuario_existente is not None:
        raise HTTPException(
            status_code=400,
            detail="El usuario con este correo electrónico ya existe.",
        )

    usuario = Usuario(
        id=0,
        name=datos.name,
        email=str(datos.email),
    )
    return usuario_repository.guardar(db, usuario)


def listar_usuarios(db: Session):
    return usuario_repository.listar(db)


def obtener_usuario(db: Session, usuario_id: int):
    usuario = usuario_repository.obtener(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario


def actualizar_usuario(db: Session, usuario_id: int, datos: UsuarioUpdate):
    usuario_actual = usuario_repository.obtener(db, usuario_id)
    if usuario_actual is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    if datos.name is not None:
        usuario_actual.name = datos.name

    if datos.email is not None:
        usuario_con_email = usuario_repository.obtener_por_email(db, str(datos.email))
        if usuario_con_email is not None and usuario_con_email.id != usuario_id:
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico ya está en uso por otro usuario.",
            )
        usuario_actual.email = str(datos.email)

    return usuario_repository.actualizar(db, usuario_actual)


def eliminar_usuario(db: Session, usuario_id: int):
    usuario_existente = usuario_repository.obtener(db, usuario_id)
    if usuario_existente is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    usuario_repository.eliminar(db, usuario_existente)