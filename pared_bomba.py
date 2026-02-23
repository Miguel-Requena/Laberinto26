from pared import Pared


class ParedBomba(Pared):
    """Representa una pared con bomba."""
    
    def __init__(self):
        self.activa: bool = False
    
    def entrar(self) -> None:
        """Acción de intentar entrar en una pared con bomba."""
        if self.activa:
            print("¡BOOM! La pared con bomba ha explotado.")
        else:
            super().entrar()
