from dataclasses import dataclass
 
 
@dataclass
class Categoria:
    """Entidad de dominio: clasifica los hábitos (SALUD, EJERCICIO, etc.)"""
    id: int
    nombre: str
    descripcion: str