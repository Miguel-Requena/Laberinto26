from typing import List
from habitacion import Habitacion


class Laberinto:
    """Representa el laberinto completo."""
    
    def __init__(self):
        self.habitaciones: List[Habitacion] = []
    
    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al laberinto."""
        self.habitaciones.append(habitacion)
