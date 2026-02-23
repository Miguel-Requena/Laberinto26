from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from elemento_mapa import ElementoMapa


class Habitacion:
    """Representa una habitación en el laberinto."""
    
    def __init__(self):
        self.norte: Optional['ElementoMapa'] = None
        self.sur: Optional['ElementoMapa'] = None
        self.este: Optional['ElementoMapa'] = None
        self.oeste: Optional['ElementoMapa'] = None
    
    def entrar(self) -> None:
        """Acción de entrar en la habitación."""
        print("Has entrado en una habitación.")
