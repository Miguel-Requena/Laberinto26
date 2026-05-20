# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from Solucion.hoja import Hoja


class ItemRecolectable(Hoja, ABC):
    """Clase base abstracta para los componentes que entran en el inventario."""
    
    def __init__(self, nombre: str = None):
        super().__init__()
        self.nombre = nombre or self.__class__.__name__

    @abstractmethod
    def entrar(self, del_personaje) -> None:
        """Comportamiento al pisar el objeto en el mapa."""
        pass

    @abstractmethod
    def usar(self, del_personaje) -> None:
        """Efecto al consumir o activar el objeto desde el inventario."""
        pass

    def __str__(self) -> str:
        return self.nombre