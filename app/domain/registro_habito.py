from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RegistroHabito(Base):
    """
    Entidad de dominio: el check-in diario de un Hábito.
    Relación N:1 con Habito (habito_id).
    """
    __tablename__ = "registros_habito"

    id: Mapped[int] = mapped_column(primary_key=True)
    habito_id: Mapped[int] = mapped_column(ForeignKey("habitos.id"))
    fecha_registro: Mapped[date] = mapped_column(Date)
    completado: Mapped[bool] = mapped_column(Boolean, default=True)
    valor_medido: Mapped[float | None] = mapped_column(Float, nullable=True)
    nota: Mapped[str | None] = mapped_column(String(200), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
 
    def es_fecha_futura(self) -> bool:
        """Comportamiento propio: el service usará esto para aplicar la regla de negocio."""
        return self.fecha_registro > date.today()