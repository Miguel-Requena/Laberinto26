# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho


class Modo(ABC):
    """Clase base que define el comportamiento de un modo (Strategy)."""
    
    def actua(self, bicho: 'Bicho') -> None:
        """Patron Template Method: define secuencia fija.
        Las subclases solo implementan duerme()."""
        self.camina(bicho)
        self.ataca(bicho)
        self.duerme(bicho)
    
    def camina(self, bicho: 'Bicho') -> None:
        """Mueve al bicho en una orientacion aleatoria."""
        if bicho.posicion is None:
            print("El bicho no tiene posicion asignada.")
            return
        orientacion = bicho.posicion.obtener_orientacion_aleatoria()
        orientacion.caminar(bicho)
    
    def ataca(self, bicho: 'Bicho') -> None:
        """El bicho ataca al enemigo."""
        bicho.atacar()
    
    @abstractmethod
    def duerme(self, bicho: 'Bicho') -> None:
        """Define cuanto duerme segun el modo. ABSTRACTO en base."""
        pass
    
    @abstractmethod
    def es_agresivo(self) -> bool:
        """Retorna True si el modo es agresivo."""
        pass
    
    @abstractmethod
    def es_perezoso(self) -> bool:
        """Retorna True si el modo es perezoso."""
        pass
