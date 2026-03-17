from elemento_mapa import ElementoMapa
from typing import Iterator


class Hoja(ElementoMapa):
    """Clase base para componentes concretos del mapa (hojas del patrón Decorator)."""
    
    def entrar(self, alguien=None) -> None:
        """Método para entrar en el elemento hoja."""
        pass
    
    def recorrer(self, bloque) -> Iterator[ElementoMapa]:
        """Recorre el elemento hoja (retorna solo a sí mismo)."""
        if callable(bloque):
            bloque(self)
        yield self
