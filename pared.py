from hoja import Hoja


class Pared(Hoja):
    """Representa una pared en el laberinto."""
    
    def entrar(self) -> None:
        """Acción de intentar entrar en una pared."""
        print("No puedes atravesar la pared.")
