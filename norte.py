from orientacion import Orientacion


class Norte(Orientacion):
    """Orientación Norte."""
    
    def get_nombre(self) -> str:
        return "Norte"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'norte', None)
        if destino is not None:
            destino.entrar(bicho)
