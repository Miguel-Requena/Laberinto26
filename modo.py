from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Modo(ABC):
    """Clase abstracta que define el comportamiento de un modo (Strategy)."""
    
    @abstractmethod
    def actua(self, bicho: 'Bicho') -> None:
        """Define cómo actúa el bicho según su modo."""
        pass

    def camina(self, bicho: 'Bicho') -> None:
        """Mueve al bicho en una orientación aleatoria desde su posición actual."""
        if bicho.posicion is None:
            print("El bicho no tiene posición asignada.")
            return
        orientacion = bicho.posicion.obtenerOrientacion()
        orientacion.caminar(bicho)
    
    @abstractmethod
    def caminar(self, bicho: 'Bicho') -> None:
        pass
    
    @abstractmethod
    def atacar(self, bicho: 'Bicho') -> None:
        pass
    
    @abstractmethod
    def dormir(self, bicho: 'Bicho') -> None:
        pass
