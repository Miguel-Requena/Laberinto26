from modo import Modo
from ente import Ente


class Bicho(Ente):
    """Usa el patrón Strategy para cambiar su comportamiento."""
    
    def __init__(self, modo: Modo, vidas: int = 100, poder: int = 10, posicion=None):
        """
        Inicializa el bicho con un modo específico.
        
        Args:
            modo: La estrategia de comportamiento del bicho.
            vidas: Puntos de vida del bicho.
            poder: Nivel de poder del bicho.
        """
        super().__init__(vidas=vidas, poder=poder, posicion=posicion)
        self._modo = modo
    
    def set_modo(self, modo: Modo) -> None:
        """
        Cambia el modo del bicho en tiempo de ejecución.
        
        Args:
            modo: El nuevo modo de comportamiento.
        """
        self._modo = modo
        print(f"El bicho ha cambiado su modo de comportamiento a {modo.__class__.__name__}")
    
    def actua(self) -> None:
        """El bicho actúa según su modo actual."""
        print(f"[Bicho - Vidas: {self.vidas}, Poder: {self.poder}]")
        self._modo.actua(self)
    
    def comportarse(self) -> None:
        """Ejecuta el comportamiento según el modo actual (método legacy)."""
        self.actua()

    @property
    def modo(self) -> Modo:
        return self._modo

    def __str__(self) -> str:
        return f"Bicho-{self._modo.__class__.__name__}"

    def __repr__(self) -> str:
        return str(self)

    def printOn(self, aStream) -> None:
        aStream.write(str(self))
