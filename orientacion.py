# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho
    from forma import Forma


class Orientacion(ABC):
    """Clase base para orientaciones (patron Strategy + Singleton)."""
    
    @abstractmethod
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina en esta direccion."""
        pass
    
    @abstractmethod
    def obtener_elemento(self, forma: 'Forma'):
        """Obtiene el elemento en esta direccion dentro de una forma."""
        pass
    
    @abstractmethod
    def poner_elemento(self, elemento, contenedor) -> None:
        """Pone un elemento en esta direccion dentro de un contenedor."""
        pass
    
    @abstractmethod
    def recorrer(self, bloque, contenedor) -> None:
        """Recorre el elemento en esta direccion."""
        pass
