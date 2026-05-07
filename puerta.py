# -*- coding: utf-8 -*-
from typing import Optional, TYPE_CHECKING
from hoja import Hoja
from estado_puerta import Cerrada

if TYPE_CHECKING:
    from habitacion import Habitacion


class Puerta(Hoja):
    """Puerta que conecta dos habitaciones y maneja estado."""
    
    def __init__(self):
        super().__init__()
        self.lado1: Optional['Habitacion'] = None
        self.lado2: Optional['Habitacion'] = None
        self.estado = Cerrada()
        self._abierta = False
    
    def entrar(self, alguien=None) -> None:
        """Delega a su estado para determinar si se puede entrar."""
        self.estado.entrar(alguien, self)
    
    def abrir(self) -> None:
        """Abre la puerta."""
        self._abierta = True
        self.estado.abrir(self)
    
    def cerrar(self) -> None:
        """Cierra la puerta."""
        self._abierta = False
        self.estado.cerrar(self)

    @property
    def abierta(self) -> bool:
        return getattr(self, '_abierta', False) or self.estado.esta_abierta()

    @abierta.setter
    def abierta(self, value: bool) -> None:
        if value:
            self.abrir()
        else:
            self.cerrar()
    
    def puede_entrar(self, alguien) -> None:
        """Logica adicional de entrada."""
        self.entrar(alguien)
    
    def es_puerta(self) -> bool:
        """Retorna True si es una puerta."""
        return True
    
    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_puerta(self)
    
    def esta_abierta(self) -> bool:
        """Retorna si esta abierta segun su estado."""
        return self.estado.esta_abierta()
    
    def esta_cerrada(self) -> bool:
        """Retorna si esta cerrada segun su estado."""
        return self.estado.esta_cerrada()

    def __str__(self) -> str:
        if self.lado1 is None or self.lado2 is None:
            return "Puerta"
        return f"Puerta-{self.lado1.num}-{self.lado2.num}"

    def __repr__(self) -> str:
        return str(self)
