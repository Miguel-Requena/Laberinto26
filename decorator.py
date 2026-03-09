from abc import abstractmethod
from elemento_mapa import ElementoMapa
from typing import Iterator


class Decorator(ElementoMapa):
    """Decorador abstracto para elementos del mapa."""
    
    def __init__(self, elemento: ElementoMapa):
        self.em: ElementoMapa = elemento
    
    @abstractmethod
    def entrar(self) -> None:
        """Método abstracto para entrar en el elemento decorado."""
        pass
    
    def recorrer(self, bloque) -> Iterator[ElementoMapa]:
        """Recorre el elemento decorado."""
        yield self
        yield from self.em.recorrer(bloque)
