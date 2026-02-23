from typing import Optional
from elemento_mapa import ElementoMapa
from habitacion import Habitacion


class Puerta(ElementoMapa):
    """Representa una puerta entre dos habitaciones."""
    
    def __init__(self):
        self.abierta: bool = False
        self.lado1: Optional[Habitacion] = None
        self.lado2: Optional[Habitacion] = None
    
    def entrar(self) -> None:
        """Acción de intentar entrar por la puerta."""
        if self.abierta:
            print("Has atravesado la puerta.")
        else:
            print("La puerta está cerrada.")
