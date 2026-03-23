from orientacion import Orientacion


class Sur(Orientacion):
    """Orientación Sur."""
    
    def get_nombre(self) -> str:
        return "Sur"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'sur', None)
        if destino is not None:
            destino.entrar(bicho)
