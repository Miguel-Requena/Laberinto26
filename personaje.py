from ente import Ente


class Personaje(Ente):
    """Representa al personaje controlado por el jugador."""

    def __init__(self, nombre: str, vidas: int = 100, poder: int = 10):
        super().__init__(vidas=vidas, poder=poder, posicion=None)
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return str(self)