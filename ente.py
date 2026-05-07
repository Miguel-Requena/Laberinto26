from estado_ente import Vivo


class Ente:
    """Entidad con posición dentro del laberinto y atributos básicos de combate.

    Ahora incluye un `estado` (Vivo/Muerto) para seguir el diagrama.
    """

    def __init__(self, vidas: int = 100, poder: int = 10, posicion=None):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.estado = Vivo()

    def morir(self) -> None:
        """Marca al ente como muerto y ajusta las vidas a 0."""
        from estado_ente import Muerto

        self.vidas = 0
        self.estado = Muerto()

    def esta_vivo(self) -> bool:
        return self.estado.nombre() == "Vivo"
