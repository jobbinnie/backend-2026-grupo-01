from datetime import date

from app.domain.registro_habito import RegistroHabito

_registros: dict[int, RegistroHabito] = {}
_contador_id = 0


def guardar(db: Session, registro: RegistroHabito) -> RegistroHabito:
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro


def listar(db: Session) -> list[RegistroHabito]:
    return list(db.scalars(select(RegistroHabito).order_by(RegistroHabito.id)).all())


def obtener(db: Session, registro_id: int) -> RegistroHabito | None:
    return db.get(RegistroHabito, registro_id)


def listar_por_habito(db: Session, habito_id: int) -> list[RegistroHabito]:
    consulta = select(RegistroHabito).where(RegistroHabito.habito_id == habito_id)
    return list(db.scalars(consulta).all())


def existe_registro_en_fecha(db: Session, habito_id: int, fecha: date) -> bool:
    consulta = select(RegistroHabito.id).where(
        RegistroHabito.habito_id == habito_id,
        RegistroHabito.fecha_registro == fecha,
    )
    return db.scalar(consulta) is not None


def actualizar(db: Session, registro: RegistroHabito) -> RegistroHabito:
    db.commit()
    db.refresh(registro)
    return registro


def eliminar(db: Session, registro: RegistroHabito) -> None:
    db.delete(registro)
    db.commit()


def existe(registro_id: int) -> bool:
    return registro_id in _registros