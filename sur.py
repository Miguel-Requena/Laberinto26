from orientacion import Orientacion


class Sur(Orientacion):
    """Orientación Sur."""
    
    def get_nombre(self) -> str:
        """Retorna el nombre de la orientación Sur."""
        return "Sur"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'sur', None)
        if destino is not None:
            destino.entrar(bicho)
