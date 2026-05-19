# -*- coding: utf-8 -*-
from Solucion.decorator import Decorator
from Solucion.pared import Pared


class Bomba(Decorator):
    """Decorador que añade funcionalidad de bomba a un elemento."""
    
    def __init__(self, elemento=None):
        if elemento is None:
            elemento = Pared()
        super().__init__(elemento)
        self.activa: bool = False
    
    def activar(self) -> None:
        """Activa la bomba."""
        print("Bomba activada")
        self.activa = True
    
    def desactivar(self) -> None:
        """Desactiva la bomba."""
        print("Bomba desactivada")
        self.activa = False
    
    def entrar(self, alguien=None) -> None:
        """Acción de entrar en un elemento con bomba."""
        if self.activa:
            if alguien:
                print(f"{alguien}, te ha explotado una bomba")
                # TODO: quitar vidas a alguien
            else:
                print("¡BOOM! La bomba ha explotado.")
        self.em.entrar(alguien)
    
    def es_bomba(self) -> bool:
        """Retorna True si el elemento es una bomba."""
        return True
    
    def aceptar(self, visitor) -> None:
        """Patrón Visitor: acepta un visitante y lo procesa."""
        visitor.visitar_bomba(self)
