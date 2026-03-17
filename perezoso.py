from modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Perezoso(Modo):
    """Estrategia concreta: modo perezoso."""
    
    def actua(self, bicho: 'Bicho') -> None:
        """Implementación del comportamiento perezoso."""
        print("Modo PEREZOSO activado:")
        self.dormir(bicho)
        self.camina(bicho)
        self.caminar(bicho)
    
    def caminar(self, bicho: 'Bicho') -> None:
        """Caminar de forma perezosa."""
        print("  - Camina lentamente, arrastrando los pies")
    
    def atacar(self, bicho: 'Bicho') -> None:
        """Atacar (modo perezoso casi no ataca)."""
        print("  - Ataca débilmente, sin ganas")
    
    def dormir(self, bicho: 'Bicho') -> None:
        """Dormir mucho."""
        print("  - Duerme profundamente y mucho tiempo")
