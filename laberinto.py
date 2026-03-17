from typing import List, TYPE_CHECKING
from habitacion import Habitacion

if TYPE_CHECKING:
    from bicho import Bicho


class Laberinto:
    """Representa el laberinto completo."""
    
    def __init__(self):
        self.habitaciones: List[Habitacion] = []
        self.bichos: List['Bicho'] = []
        self.hijos = self.habitaciones
    
    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al laberinto."""
        self.habitaciones.append(habitacion)

    def agregarHabitacion(self, habitacion: Habitacion) -> None:
        self.agregar_habitacion(habitacion)

    def obtener_habitacion(self, num: int) -> Habitacion | None:
        """Devuelve la habitación cuyo número coincide con el indicado."""
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion
        return None

    def obtenerHabitacion(self, num: int) -> Habitacion | None:
        """Alias compatible con la nomenclatura del código Pharo."""
        return self.obtener_habitacion(num)
    
    def agregar_bicho(self, bicho: 'Bicho') -> None:
        """Agrega un bicho al laberinto."""
        self.bichos.append(bicho)

    def agregarBicho(self, bicho: 'Bicho') -> None:
        self.agregar_bicho(bicho)

    def recorrer(self, unBloque) -> None:
        print("Recorriendo el laberinto")
        for each in self.hijos:
            for _ in each.recorrer(unBloque):
                pass
