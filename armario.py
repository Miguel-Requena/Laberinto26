# -*- coding: utf-8 -*-
from habitacion import Habitacion


class Armario(Habitacion):
    """Contenedor interno conectado a otro contenedor mediante una puerta."""

    def __str__(self) -> str:
        return f"Armario {self.num}"
    
    def es_armario(self) -> bool:
        """Retorna True si es un armario."""
        return True
    
    def aceptar(self, visitor) -> None:
        """Patrón Visitor: acepta un visitante para procesarse."""
        visitor.visitar_armario(self)
