from fastapi import HTTPException

from Domain.usuario import Usuario
from Schemas.usuario_schema import UsuarioCreate, UsuarioUpdate

try:
    from Repositories.usuario_repository import usuario_repository
except ImportError:
    usuario_repository = None


def crear_usuario(datos: UsuarioCreate):
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")

    usuario_existente = usuario_repository.obtener_por_email(str(datos.email))
    if usuario_existente is not None:
        raise HTTPException(
            status_code=400,
            detail="El usuario con este correo electrónico ya existe.",
        )

    nuevo_id = usuario_repository.generar_id()
    usuario = Usuario(
        id=nuevo_id,
        name=datos.name,
        email=str(datos.email),
    )
    return usuario_repository.crear(usuario)


def listar_usuarios():
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")
    return usuario_repository.listar()


def obtener_usuario(usuario_id: int):
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")

    usuario = usuario_repository.obtener_por_id(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario


def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate):
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")

    usuario_actual = usuario_repository.obtener_por_id(usuario_id)
    if usuario_actual is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    if datos.name is not None:
        usuario_actual.name = datos.name

    if datos.email is not None:
        usuario_con_email = usuario_repository.obtener_por_email(str(datos.email))
        if usuario_con_email is not None and usuario_con_email.id != usuario_id:
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico ya está en uso por otro usuario.",
            )
        usuario_actual.email = str(datos.email)

    return usuario_repository.actualizar(usuario_id, usuario_actual)


def eliminar_usuario(usuario_id: int):
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")

    usuario_existente = usuario_repository.obtener_por_id(usuario_id)
    if usuario_existente is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    usuario_repository.eliminar(usuario_id)