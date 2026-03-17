from modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Agresivo(Modo):
    """Estrategia concreta: modo agresivo."""
    
    def actua(self, bicho: 'Bicho') -> None:
        """Implementación del comportamiento agresivo."""
        print("Modo AGRESIVO activado:")
        self.camina(bicho)
        self.caminar(bicho)
        self.atacar(bicho)
    
    def caminar(self, bicho: 'Bicho') -> None:
        """Caminar de forma agresiva."""
        print("  - Camina rápidamente y con determinación")
    
    def atacar(self, bicho: 'Bicho') -> None:
        """Atacar ferozmente."""
        print("  - ¡Ataca con toda su fuerza!")
    
    def dormir(self, bicho: 'Bicho') -> None:
        """Dormir (modo agresivo casi no duerme)."""
        print("  - Duerme muy poco, siempre alerta")
