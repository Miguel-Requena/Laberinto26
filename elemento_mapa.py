from abc import ABC, abstractmethod
from typing import Iterator, TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class ElementoMapa(ABC):
    """Clase abstracta que representa un elemento del mapa."""
    
    @abstractmethod
    def entrar(self) -> None:
        """Método abstracto para entrar en el elemento."""
        pass
    
    @abstractmethod
    def recorrer(self, bloque) -> Iterator['ElementoMapa']:
        """Método abstracto para recorrer el elemento (patrón Iterator)."""
        pass
