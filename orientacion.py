from abc import ABC, abstractmethod


class Orientacion(ABC):
    """Clase abstracta que representa una orientación."""
    
    @abstractmethod
    def get_nombre(self) -> str:
        """Retorna el nombre de la orientación."""
        pass
