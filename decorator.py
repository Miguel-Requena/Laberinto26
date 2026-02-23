from abc import abstractmethod
from elemento_mapa import ElementoMapa


class Decorator(ElementoMapa):
    """Decorador abstracto para elementos del mapa."""
    
    def __init__(self, elemento: ElementoMapa):
        self._elemento: ElementoMapa = elemento
    
    @abstractmethod
    def entrar(self) -> None:
        """Método abstracto para entrar en el elemento decorado."""
        pass
