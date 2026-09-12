from fastapi import APIRouter

from Schemas.habito_schema import (
    HabitoCreate,
    HabitoUpdate,
    HabitoResponse,
)
from Services import habito_service

router = APIRouter(
    prefix="/habitos",
    tags=["Habitos"]
)

@router.post("/", status_code=201, response_model=HabitoResponse)
def crear_habito(datos: HabitoCreate):
    return habito_service.crear_habito(datos)

@router.get("/", response_model=list[HabitoResponse])
def listar_habitos(
    usuario_id: int | None = None,
    categoria_id: int | None = None,
    estado: str | None = None,
):
    return habito_service.listar_habitos(
        usuario_id=usuario_id, categoria_id=categoria_id, estado=estado, )

@router.get("/{habito_id}", response_model=HabitoResponse)
def obtener_habito(habito_id: int):
    return habito_service.obtener_habito(habito_id)

@router.put("/{habito_id}", response_model=HabitoResponse)
def actualizar_habito(habito_id: int, datos: HabitoUpdate):
    return habito_service.actualizar_habito(habito_id, datos)

@router.delete("/{habito_id}", status_code=204)
def eliminar_habito(habito_id: int):
    habito_service.eliminar_habito(habito_id)
