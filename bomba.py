from decorator import Decorator
from elemento_mapa import ElementoMapa


class Bomba(Decorator):
    """Decorador que añade funcionalidad de bomba a un elemento."""
    
    def __init__(self, elemento: ElementoMapa):
        super().__init__(elemento)
        self.activa: bool = False
    
    def entrar(self) -> None:
        """Acción de entrar en un elemento con bomba."""
        if self.activa:
            print("¡BOOM! La bomba ha explotado.")
        else:
            print("La bomba no está activa.")
        self._elemento.entrar()
