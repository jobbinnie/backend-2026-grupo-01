from datetime import date
from fastapi import HTTPException
from App.Repositories import registro_repository
from Domain.registro_habito import RegistroHabito
from Repositories.habito_repository import HabitoRepository
from Repositories.registro_repository import RegistroHabitoRepository
from Schemas.registro_schema import RegistroHabitoCreate, RegistroHabitoUpdate, RegistroHabitoResponse

def crear_registro_habito(datos: RegistroHabitoCreate):
    habito = HabitoRepository.obtener_habito_por_id(datos.habito_id)
    if habito is None:
        raise HTTPException(status_code=404, detail="Hábito no encontrado.")

    if datos.fecha_registro > date.today():
        raise HTTPException(status_code=400, detail="La fecha de registro no puede ser futura.")

    registro_existente = registro_repository.obtener_registro_por_habito_y_fecha(datos.habito_id, datos.fecha_registro)

    if registro_existente is not None:
        raise HTTPException(status_code=400, detail="Ya existe un registro para este hábito en la fecha especificada.")

    nuevo_id = registro_repository.generar_id()

    registro = RegistroHabito(id=nuevo_id, habito_id=datos.habito_id, fecha_registro=datos.fecha_registro, completado=datos.completado, valor_medido=datos.valor_medido, nota=datos.nota)
    return registro_repository.crear_registro_habito(registro)

def obtener_registro_por_id(registro_id: int):
    registro = registro_repository.obtener_por_id(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    return registro

def actualizar_registro(registro_id: int, datos: RegistroHabitoUpdate):
    registro = registro_repository.obtener_por_id(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")

    if datos.completado is not None:
        registro.completado = datos.completado

    if datos.valor_medido is not None:
        registro.valor_medido = datos.valor_medido

    if datos.nota is not None:
        registro.nota = datos.nota

    return registro_repository.actualizar_registro(registro_id, registro)

def eliminar_registro(registro_id: int):
    registro = registro_repository.obtener_por_id(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")

    registro_repository.eliminar_registro(registro_id)