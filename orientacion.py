from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Orientacion(ABC):
    """Clase abstracta que representa una orientación."""
    
    @abstractmethod
    def get_nombre(self) -> str:
        pass

    @abstractmethod
    def caminar(self, bicho: 'Bicho') -> None:
        pass

    def recorrer(self, bloque, enContenedor) -> None:
        elemento = getattr(enContenedor, self.get_nombre().lower(), None)
        if elemento is not None:
            for _ in elemento.recorrer(bloque):
                pass
