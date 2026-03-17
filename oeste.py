from orientacion import Orientacion


class Oeste(Orientacion):
    """Orientación Oeste."""
    
    def get_nombre(self) -> str:
        """Retorna el nombre de la orientación Oeste."""
        return "Oeste"

    def caminar(self, bicho) -> None:
        destino = getattr(bicho.posicion, 'oeste', None)
        if destino is not None:
            destino.entrar(bicho)
