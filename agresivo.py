from modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Agresivo(Modo):
    """Estrategia concreta: modo agresivo."""
    
    def actua(self, bicho: 'Bicho') -> None:
        """Implementación del comportamiento agresivo."""
        print("Modo AGRESIVO activado:")
        self.caminar()
        self.atacar()
    
    def caminar(self) -> None:
        """Caminar de forma agresiva."""
        print("  - Camina rápidamente y con determinación")
    
    def atacar(self) -> None:
        """Atacar ferozmente."""
        print("  - ¡Ataca con toda su fuerza!")
    
    def dormir(self) -> None:
        """Dormir (modo agresivo casi no duerme)."""
        print("  - Duerme muy poco, siempre alerta")
