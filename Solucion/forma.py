# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.orientacion import Orientacion


class Forma(ABC):
    """Clase base para formas (Cuadrado, Rombo, etc.)."""
    
    def __init__(self):
        self.num: int = 0
    
    @abstractmethod
    def obtener_elemento(self, orientacion: 'Orientacion'):
        """Obtiene el elemento en una direccion."""
        pass
    
    @abstractmethod
    def poner_elemento(self, orientacion: 'Orientacion', elemento) -> None:
        """Pone un elemento en una direccion."""
        pass
    
    @abstractmethod
    def obtener_orientacion_aleatoria(self) -> 'Orientacion':
        """Retorna una orientacion aleatoria."""
        pass
    
    def agregar_orientacion(self, orientacion: 'Orientacion') -> None:
        """Agrega una orientacion (no usado en Pharo pero compatible)."""
        pass
    
    def remover_orientacion(self, orientacion: 'Orientacion') -> None:
        """Remueve una orientacion."""
        pass
    
    @property
    def orientaciones(self) -> List['Orientacion']:
        """Retorna las orientaciones disponibles."""
        return []
