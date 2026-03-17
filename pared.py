from hoja import Hoja


class Pared(Hoja):
    """Representa una pared en el laberinto."""
    
    def entrar(self, alguien=None) -> None:
        """Acción de intentar entrar en una pared."""
        print("Has chocado con una pared")
