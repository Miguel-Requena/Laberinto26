from typing import List, TYPE_CHECKING
from habitacion import Habitacion

if TYPE_CHECKING:
    from bicho import Bicho


class Laberinto:
    """Representa el laberinto completo."""
    
    def __init__(self):
        self.habitaciones: List[Habitacion] = []
        self.bichos: List['Bicho'] = []
    
    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al laberinto."""
        self.habitaciones.append(habitacion)
    
    def agregar_bicho(self, bicho: 'Bicho') -> None:
        """Agrega un bicho al laberinto."""
        self.bichos.append(bicho)
