# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Iterator


class ElementoMapa(ABC):
    """Clase base para todos los elementos del mapa (patron Composite)."""
    
    def __init__(self):
        self.comandos = []
    
    @abstractmethod
    def aceptar(self, visitor) -> None:
        """Patron Visitor: acepta un visitante."""
        pass
    
    @abstractmethod
    def entrar(self, alguien=None) -> None:
        """Define que pasa cuando alguien entra."""
        pass
    
    @abstractmethod
    def recorrer(self, bloque) -> Iterator['ElementoMapa']:
        """Patron Iterator: recorre el elemento."""
        pass
    
    def agregar_comando(self, comando) -> None:
        """Agrega un comando al elemento."""
        self.comandos.append(comando)
    
    def remover_comando(self, comando) -> None:
        """Remueve un comando."""
        if comando in self.comandos:
            self.comandos.remove(comando)
    
    def es_armario(self) -> bool:
        return False
    
    def es_bomba(self) -> bool:
        return False
    
    def es_puerta(self) -> bool:
        return False
    
    def es_tunel(self) -> bool:
        return False
    
    def es_pared(self) -> bool:
        return False
    
    def es_cofre(self) -> bool:
        return False

    def es_pocion(self) -> bool:
        return False
    
    def __str__(self) -> str:
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return str(self)
