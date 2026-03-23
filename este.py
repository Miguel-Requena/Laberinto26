from orientacion import Orientacion


class Este(Orientacion):
    """Orientación Este."""
    
    def get_nombre(self) -> str:
        return "Este"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'este', None)
        if destino is not None:
            destino.entrar(bicho)
