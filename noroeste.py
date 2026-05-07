from orientacion import Orientacion


class Noroeste(Orientacion):
    def get_nombre(self) -> str:
        return "Noroeste"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'noroeste', None)
        if destino is not None:
            destino.entrar(bicho)
