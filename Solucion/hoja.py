# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from Solucion.elemento_mapa import ElementoMapa
from typing import Iterator


class Hoja(ElementoMapa, ABC):
    """Hoja en el patron Composite: elemento terminal sin hijos."""
    
    def recorrer(self, bloque) -> Iterator[ElementoMapa]:
        """Recorre solo este elemento."""
        print(f"Recorriendo {self}")
        if callable(bloque):
            bloque(self)
        yield self
    
    @abstractmethod
    def entrar(self, alguien=None) -> None:
        """Metodo que define que pasa al entrar."""
        pass
    
    def __str__(self) -> str:
        return self.__class__.__name__
