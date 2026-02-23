from abc import ABC, abstractmethod


class ElementoMapa(ABC):
    """Clase abstracta que representa un elemento del mapa."""
    
    @abstractmethod
    def entrar(self) -> None:
        """Método abstracto para entrar en el elemento."""
        pass
