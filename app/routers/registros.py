from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.registro_schema import (
    RegistroHabitoCreate,
    RegistroHabitoResponse,
    RegistroHabitoUpdate,
)
from app.services import registro_service

router = APIRouter(
    prefix="/registros",
    tags=["Registros"]
)


@router.post("/", status_code=201, response_model=RegistroHabitoResponse)
def crear_registro_habito(datos: RegistroHabitoCreate, db: Session = Depends(get_db)):
    return registro_service.crear_registro_habito(db, datos)


@router.get("/", response_model=list[RegistroHabitoResponse])
def listar_registros_habito(db: Session = Depends(get_db)):
    return registro_service.listar_registros_habito(db)


@router.get("/{registro_id}", response_model=RegistroHabitoResponse)
def obtener_registro_habito(registro_id: int, db: Session = Depends(get_db)):
    return registro_service.obtener_registro_habito(db, registro_id)


@router.put("/{registro_id}", response_model=RegistroHabitoResponse)
def actualizar_registro_habito(registro_id: int, datos: RegistroHabitoUpdate, db: Session = Depends(get_db)):
    return registro_service.actualizar_registro_habito(db, registro_id, datos)


@router.delete("/{registro_id}", status_code=204)
def eliminar_registro_habito(registro_id: int, db: Session = Depends(get_db)):
    registro_service.eliminar_registro_habito(db, registro_id)