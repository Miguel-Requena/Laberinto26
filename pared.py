# -*- coding: utf-8 -*-
from hoja import Hoja


class Pared(Hoja):
    """Pared: un obstaculo que impide el paso."""
    
    def entrar(self, alguien=None) -> None:
        """Intenta entrar en una pared."""
        if alguien:
            print(f"{alguien} se ha chocado con una pared")
        else:
            print("Se ha chocado con una pared")
    
    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_pared(self)
    
    def es_pared(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return "Pared"
