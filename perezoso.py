from modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Perezoso(Modo):
    """Estrategia concreta: modo perezoso."""
    
    def actua(self, bicho: 'Bicho') -> None:
        """Implementación del comportamiento perezoso."""
        print("Modo PEREZOSO activado:")
        self.dormir()
        self.caminar()
    
    def caminar(self) -> None:
        """Caminar de forma perezosa."""
        print("  - Camina lentamente, arrastrando los pies")
    
    def atacar(self) -> None:
        """Atacar (modo perezoso casi no ataca)."""
        print("  - Ataca débilmente, sin ganas")
    
    def dormir(self) -> None:
        """Dormir mucho."""
        print("  - Duerme profundamente y mucho tiempo")
