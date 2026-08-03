from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Servicio:
    
    id_servicio: Optional[int] = None
    cliente: str = ""
    vehiculo: str = ""
    tipo_servicio: str = ""
    costo: float = 0.0
    fecha_registro: Optional[datetime] = None
    
    def __post_init__(self):
        if self.costo < 0:
            raise ValueError("El costo no puede ser negativo")
    
    def to_dict(self) -> dict:
        return {
            'id_servicio': self.id_servicio,
            'cliente': self.cliente,
            'vehiculo': self.vehiculo,
            'tipo_servicio': self.tipo_servicio,
            'costo': self.costo,
            'fecha_registro': self.fecha_registro
        }
    
    def __str__(self) -> str:
        return f"Servicio({self.id_servicio}): {self.cliente} - {self.vehiculo} - ${self.costo}"