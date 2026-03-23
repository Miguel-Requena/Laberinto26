from abc import ABC, abstractmethod
from typing import Iterator, TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class ElementoMapa(ABC):
    
    @abstractmethod
    def entrar(self, alguien=None) -> None:
        pass
    
    @abstractmethod
    def recorrer(self, bloque) -> Iterator['ElementoMapa']:
        """Método abstracto para recorrer el elemento (patrón Iterator)."""
        pass

    def esPuerta(self) -> bool:
        return False
