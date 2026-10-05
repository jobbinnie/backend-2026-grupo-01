from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Usuario(Base):
    """Modelo persistente: representa a la persona que sigue sus hábitos."""

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    fecha_registro: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)