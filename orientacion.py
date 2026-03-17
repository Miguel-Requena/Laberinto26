from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Orientacion(ABC):
    """Clase abstracta que representa una orientación."""
    
    @abstractmethod
    def get_nombre(self) -> str:
        """Retorna el nombre de la orientación."""
        pass

    @abstractmethod
    def caminar(self, bicho: 'Bicho') -> None:
        """Mueve al bicho en la orientación correspondiente."""
        pass

    def recorrer(self, bloque, enContenedor) -> None:
        """Recorre el elemento asociado a esta orientación dentro de un contenedor."""
        elemento = getattr(enContenedor, self.get_nombre().lower(), None)
        if elemento is not None:
            for _ in elemento.recorrer(bloque):
                pass
