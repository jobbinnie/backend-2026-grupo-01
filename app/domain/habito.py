from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class EstadoHabito(str, Enum):
    """Valores permitidos para el estado de un hábito (validación de Enum)."""
    ACTIVO = "ACTIVO"
    PAUSADO = "PAUSADO"
    ARCHIVADO = "ARCHIVADO"
 
 
class Habito(Base):
    """
    Entidad de dominio: un hábito que un Usuario quiere seguir.
    Relación N:1 con Usuario y N:1 con Categoria.
    """
    __tablename__ = "habitos"

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    nombre: Mapped[str] = mapped_column(String(50))
    frecuencia_semanal: Mapped[int] = mapped_column(Integer)
    estado: Mapped[EstadoHabito] = mapped_column(
        SqlEnum(EstadoHabito), default=EstadoHabito.ACTIVO
    )
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
 
    def esta_activo(self) -> bool:
        """Comportamiento propio del dominio: no requiere consultar otras entidades."""
        return self.estado == EstadoHabito.ACTIVO
 
    def archivar(self) -> None:
        """Cambia el estado en vez de permitir el borrado físico (regla de negocio)."""
        self.estado = EstadoHabito.ARCHIVADO