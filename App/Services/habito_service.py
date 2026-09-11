from fastapi import HTTPException

from Domain.habito import Habito
from Schemas.habito_schema import HabitoCreate, HabitoUpdate

try:
    from Repositories.habito_repository import habito_repository
except ImportError:
    habito_repository = None

try:
    from Repositories.usuario_repository import usuario_repository
except ImportError:
    usuario_repository = None


def crear_habito(datos: HabitoCreate):
    if usuario_repository is None:
        raise RuntimeError("El repositorio de usuarios todavía no está implementado.")
    if habito_repository is None:
        raise RuntimeError("El repositorio de hábitos todavía no está implementado.")

    usuario = usuario_repository.obtener_por_id(datos.usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    habito_existente = habito_repository.obtener_por_nombre_y_usuario(
        datos.usuario_id,
        datos.nombre,
    )
    if habito_existente is not None:
        raise HTTPException(
            status_code=400,
            detail="El hábito con este nombre ya existe para este usuario.",
        )

    nuevo_id = habito_repository.generar_id()
    habito = Habito(
        id=nuevo_id,
        usuario_id=datos.usuario_id,
        categoria_id=datos.categoria_id,
        nombre=datos.nombre,
        frecuencia_semanal=datos.frecuencia_semanal,
    )
    return habito_repository.crear(habito)


def listar_habitos(usuario_id: int | None = None, categoria_id: int | None = None, estado: str | None = None):
    if habito_repository is None:
        raise RuntimeError("El repositorio de hábitos todavía no está implementado.")

    habitos = habito_repository.listar()

    if usuario_id is not None:
        habitos = [h for h in habitos if h.usuario_id == usuario_id]

    if categoria_id is not None:
        habitos = [h for h in habitos if h.categoria_id == categoria_id]

    if estado is not None:
        habitos = [h for h in habitos if h.estado.value == estado.upper()]

    return habitos


def obtener_habito(habito_id: int):
    if habito_repository is None:
        raise RuntimeError("El repositorio de hábitos todavía no está implementado.")

    habito = habito_repository.obtener_por_id(habito_id)
    if habito is None:
        raise HTTPException(status_code=404, detail="Hábito no encontrado.")
    return habito


def actualizar_habito(habito_id: int, datos: HabitoUpdate):
    if habito_repository is None:
        raise RuntimeError("El repositorio de hábitos todavía no está implementado.")

    habito = habito_repository.obtener_por_id(habito_id)
    if habito is None:
        raise HTTPException(status_code=404, detail="Hábito no encontrado.")

    if datos.nombre is not None:
        habito_existente = habito_repository.obtener_por_nombre_y_usuario(
            habito.usuario_id,
            datos.nombre,
        )
        if habito_existente is not None and habito_existente.id != habito_id:
            raise HTTPException(
                status_code=400,
                detail="El hábito con este nombre ya existe para este usuario.",
            )
        habito.nombre = datos.nombre

    if datos.frecuencia_semanal is not None:
        habito.frecuencia_semanal = datos.frecuencia_semanal

    if datos.categoria_id is not None:
        habito.categoria_id = datos.categoria_id

    if datos.estado is not None:
        habito.estado = datos.estado

    return habito_repository.actualizar(habito_id, habito)


def eliminar_habito(habito_id: int):
    if habito_repository is None:
        raise RuntimeError("El repositorio de hábitos todavía no está implementado.")

    habito = habito_repository.obtener_por_id(habito_id)
    if habito is None:
        raise HTTPException(status_code=404, detail="Hábito no encontrado.")

    habito_repository.eliminar(habito_id)