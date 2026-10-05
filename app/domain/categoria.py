from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Categoria(Base):
    """Modelo persistente que clasifica los hábitos."""

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    descripcion: Mapped[str] = mapped_column(String(200))