from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import usuario_service
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/", status_code=201, response_model=UsuarioResponse)
def crear_usuario(datos: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.crear_usuario(db, datos)


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return usuario_service.obtener_usuario(db, usuario_id)


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate, db: Session = Depends(get_db)):
    return usuario_service.actualizar_usuario(db, usuario_id, datos)


@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_service.eliminar_usuario(db, usuario_id)