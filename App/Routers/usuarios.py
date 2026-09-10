from fastapi import APIRouter
from Services import usuario_service

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/", status_code=201)
def crear_usuario(datos):
    return usuario_service.crear_usuario(datos)


@router.get("/")
def listar_usuarios():
    return usuario_service.listar_usuarios()


@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return usuario_service.obtener_usuario(usuario_id)


@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos):
    return usuario_service.actualizar_usuario(usuario_id, datos)


@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: int):
    usuario_service.eliminar_usuario(usuario_id)