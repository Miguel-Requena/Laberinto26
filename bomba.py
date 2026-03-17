from decorator import Decorator
from pared import Pared


class Bomba(Decorator):
    """Decorador que añade funcionalidad de bomba a un elemento."""
    
    def __init__(self, elemento=None):
        if elemento is None:
            elemento = Pared()
        super().__init__(elemento)
        self.activa: bool = False
    
    def entrar(self, alguien=None) -> None:
        """Acción de entrar en un elemento con bomba."""
        if self.activa:
            print("¡BOOM! La bomba ha explotado.")
        else:
            print("La bomba no está activa.")
        self.em.entrar(alguien)
