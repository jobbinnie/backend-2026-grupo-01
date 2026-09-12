from datetime import date

from fastapi import HTTPException

from app.domain.registro_habito import RegistroHabito
from app.repositories import habito_repository, registro_repository
from app.schemas.registro_schema import RegistroHabitoCreate, RegistroHabitoUpdate

def crear_registro_habito(datos: RegistroHabitoCreate):
    habito = habito_repository.obtener(datos.habito_id)
    if habito is None:
        raise HTTPException(status_code=404, detail="Hábito no encontrado.")

    if datos.fecha_registro > date.today():
        raise HTTPException(status_code=400, detail="La fecha de registro no puede ser futura.")

    if registro_repository.existe_registro_en_fecha(
        datos.habito_id,
        datos.fecha_registro,
    ):
        raise HTTPException(status_code=400, detail="Ya existe un registro para este hábito en la fecha especificada.")

    registro = RegistroHabito(
        id=0,
        habito_id=datos.habito_id,
        fecha_registro=datos.fecha_registro,
        completado=datos.completado,
        valor_medido=datos.valor_medido,
        nota=datos.nota,
    )
    return registro_repository.guardar(registro)

def listar_registros_habito():
    return registro_repository.listar()


def obtener_registro_habito(registro_id: int):
    registro = registro_repository.obtener(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    return registro

def actualizar_registro_habito(registro_id: int, datos: RegistroHabitoUpdate):
    registro = registro_repository.obtener(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")

    if datos.completado is not None:
        registro.completado = datos.completado

    if datos.valor_medido is not None:
        registro.valor_medido = datos.valor_medido

    if datos.nota is not None:
        registro.nota = datos.nota

    return registro_repository.actualizar(registro_id, registro)

def eliminar_registro_habito(registro_id: int):
    registro = registro_repository.obtener(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")

    registro_repository.eliminar(registro_id)