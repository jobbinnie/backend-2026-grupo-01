from dataclasses import dataclass, field
from datetime import date, datetime
 
 
@dataclass
class RegistroHabito:
    """
    Entidad de dominio: el check-in diario de un Hábito.
    Relación N:1 con Habito (habito_id).
    """
    id: int
    habito_id: int
    fecha_registro: date
    completado: bool
    valor_medido: float | None = None
    nota: str | None = None
    creado_en: datetime = field(default_factory=datetime.now)
 
    def es_fecha_futura(self) -> bool:
        """Comportamiento propio: el service usará esto para aplicar la regla de negocio."""
        return self.fecha_registro > date.today()