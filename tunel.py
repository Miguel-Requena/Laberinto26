from hoja import Hoja


class Tunel(Hoja):
    """Conecta con otro laberinto o zona, según el diagrama de dominio."""

    def __init__(self, laberinto=None):
        self.laberinto = laberinto

    def entrar(self, alguien=None) -> None:
        if alguien is not None:
            print(f"{alguien} atraviesa un tunel")
        else:
            print("Has entrado en un tunel")
