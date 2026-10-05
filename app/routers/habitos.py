from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.habito_schema import (
    HabitoCreate,
    HabitoUpdate,
    HabitoResponse,
)
from app.services import habito_service

router = APIRouter(
    prefix="/habitos",
    tags=["Habitos"]
)

@router.post("/", status_code=201, response_model=HabitoResponse)
def crear_habito(datos: HabitoCreate, db: Session = Depends(get_db)):
    return habito_service.crear_habito(db, datos)

@router.get("/", response_model=list[HabitoResponse])
def listar_habitos(
    usuario_id: int | None = None,
    categoria_id: int | None = None,
    estado: str | None = None,
    orden: str = "nombre",
    pagina: int = 1,
    tamano_pagina: int = 10,
    db: Session = Depends(get_db),
):
    return habito_service.listar_habitos(
        db=db,
        usuario_id=usuario_id,
        categoria_id=categoria_id,
        estado=estado,
        orden=orden,
        pagina=pagina,
        tamano_pagina=tamano_pagina,
    )

@router.get("/{habito_id}", response_model=HabitoResponse)
def obtener_habito(habito_id: int, db: Session = Depends(get_db)):
    return habito_service.obtener_habito(db, habito_id)

@router.put("/{habito_id}", response_model=HabitoResponse)
def actualizar_habito(habito_id: int, datos: HabitoUpdate, db: Session = Depends(get_db)):
    return habito_service.actualizar_habito(db, habito_id, datos)

@router.delete("/{habito_id}", status_code=204)
def eliminar_habito(habito_id: int, db: Session = Depends(get_db)):
    habito_service.eliminar_habito(db, habito_id)
