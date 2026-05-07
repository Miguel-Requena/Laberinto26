# -*- coding: utf-8 -*-
import random
from forma import Forma
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from orientacion import Orientacion


class Cuadrado(Forma):
    """Forma cuadrada con 4 direcciones (Norte, Sur, Este, Oeste)."""
    
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    
    def obtener_elemento(self, orientacion: 'Orientacion'):
        """Obtiene el elemento en una direccion."""
        return orientacion.obtener_elemento(self)
    
    def poner_elemento(self, orientacion: 'Orientacion', elemento) -> None:
        """Pone un elemento en una direccion."""
        orientacion.poner_elemento(elemento, self)
    
    def obtener_orientacion_aleatoria(self) -> 'Orientacion':
        """Retorna una orientacion aleatoria entre las 4."""
        from norte import Norte
        from sur import Sur
        from este import Este
        from oeste import Oeste
        
        orientaciones = [Norte.default(), Sur.default(), Este.default(), Oeste.default()]
        return random.choice(orientaciones)
    
    @property
    def orientaciones(self):
        """Retorna las 4 orientaciones."""
        from norte import Norte
        from sur import Sur
        from este import Este
        from oeste import Oeste
        
        return [Norte.default(), Sur.default(), Este.default(), Oeste.default()]
    
    def __str__(self) -> str:
        return "Cuadrado"
