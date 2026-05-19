# -*- coding: utf-8 -*-
from Solucion.pared import Pared


class ParedBomba(Pared):
    """Pared que tiene una bomba integrada."""
    
    def __init__(self):
        super().__init__()
        self.activa: bool = False
    
    def entrar(self, alguien=None) -> None:
        """Si la bomba esta activa, explota."""
        if self.activa:
            if alguien:
                print(f"{alguien} se ha chocado con una pared bomba y BOOM!")
            else:
                print("Ha explotado una bomba en la pared")
        else:
            super().entrar(alguien)
    
    def activar(self) -> None:
        """Activa la bomba."""
        print("Bomba activada")
        self.activa = True
    
    def desactivar(self) -> None:
        """Desactiva la bomba."""
        print("Bomba desactivada")
        self.activa = False
    
    def __str__(self) -> str:
        return "ParedBomba"
