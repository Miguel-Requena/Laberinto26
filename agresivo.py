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
        print("  - Camina rápidamente y con determinación")
    
    def atacar(self, bicho: 'Bicho') -> None:
        print("  - ¡Ataca de forma agresiva!")
    
    def dormir(self, bicho: 'Bicho') -> None:
        print("  - Duerme muy poco, siempre alerta")
