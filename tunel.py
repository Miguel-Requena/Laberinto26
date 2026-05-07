# -*- coding: utf-8 -*-
from hoja import Hoja
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from laberinto import Laberinto
    from juego import Juego


class Tunel(Hoja):
    """Tunel que crea/clona un nuevo laberinto."""
    
    def __init__(self):
        super().__init__()
        self.laberinto: Optional['Laberinto'] = None
    
    def entrar(self, alguien=None) -> None:
        """Entra en el tunel y va al laberinto clonado."""
        if self.laberinto is None and alguien is not None:
            # Lazy load: clonar laberinto la primera vez
            juego = getattr(alguien, 'juego', None)
            if juego and hasattr(juego, 'clonar'):
                self.laberinto = juego.clonar()
        
        if self.laberinto is not None:
            self.laberinto.entrar(alguien)
    
    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_tunel(self)
    
    def es_tunel(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return "Tunel"
