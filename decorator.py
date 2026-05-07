# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from hoja import Hoja


class Decorator(Hoja, ABC):
    """Patron Decorator."""
    
    def __init__(self, elemento=None):
        super().__init__()
        if elemento is None:
            from pared import Pared
            elemento = Pared()
        self.em = elemento
    
    @abstractmethod
    def entrar(self, alguien=None) -> None:
        pass
    
    def recorrer(self, bloque):
        if callable(bloque):
            bloque(self)
        yield self
        yield from self.em.recorrer(bloque)
