# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Comando(ABC):
    
    def __init__(self):
        self.receptor = None
    
    @abstractmethod
    def ejecutar(self, alguien=None) -> None:
        pass


class Abrir(Comando):
    """Comando abrir."""
    
    def ejecutar(self, alguien=None) -> None:
        if self.receptor and hasattr(self.receptor, 'abrir'):
            self.receptor.abrir()


class Cerrar(Comando):
    """Comando cerrar."""
    
    def ejecutar(self, alguien=None) -> None:
        if self.receptor and hasattr(self.receptor, 'cerrar'):
            self.receptor.cerrar()
