class Ente:
    """Entidad con posición dentro del laberinto y atributos básicos de combate."""

    def __init__(self, vidas: int = 100, poder: int = 10, posicion=None):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
