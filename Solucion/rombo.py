# -*- coding: utf-8 -*-
import random
from Solucion.forma import Forma
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.orientacion import Orientacion


class Rombo(Forma):
    """Forma rombo con 4 direcciones diagonales (NE, NO, SE, SO)."""
    
    def __init__(self):
        super().__init__()
        self.ne = None  # Noreste
        self.no = None  # Noroeste
        self.se = None  # Sureste
        self.so = None  # Suroeste
    
    def obtener_elemento(self, orientacion: 'Orientacion'):
        """Obtiene el elemento en una direccion."""
        return orientacion.obtener_elemento(self)
    
    def poner_elemento(self, orientacion: 'Orientacion', elemento) -> None:
        """Pone un elemento en una direccion."""
        orientacion.poner_elemento(elemento, self)
    
    def obtener_orientacion_aleatoria(self) -> 'Orientacion':
        """Retorna una orientacion aleatoria entre las 4 diagonales."""
        from Solucion.noreste import Noreste
        from Solucion.noroeste import Noroeste
        from Solucion.sureste import Sureste
        from Solucion.suroeste import Suroeste
        
        orientaciones = [Noreste.default(), Noroeste.default(), Sureste.default(), Suroeste.default()]
        return random.choice(orientaciones)
    
    @property
    def orientaciones(self):
        """Retorna las 4 orientaciones diagonales."""
        from Solucion.noreste import Noreste
        from Solucion.noroeste import Noroeste
        from Solucion.sureste import Sureste
        from Solucion.suroeste import Suroeste
        
        return [Noreste.default(), Noroeste.default(), Sureste.default(), Suroeste.default()]
    
    def __str__(self) -> str:
        return "Rombo"
