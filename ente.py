# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from juego import Juego


class Ente(ABC):
    """Clase base para entidades vivas en el laberinto."""
    
    def __init__(self, vidas: int = 50, poder: int = 1):
        self.vidas = vidas
        self.poder = poder
        self.posicion: Optional['Contenedor'] = None
        self.juego: Optional['Juego'] = None
    
    def atacar(self) -> None:
        """Ataca a un enemigo si lo encuentra."""
        enemigo = self.buscar_enemigo()
        if enemigo:
            enemigo.es_atacado_por(self)
    
    @abstractmethod
    def buscar_enemigo(self) -> Optional['Ente']:
        """Busca un enemigo."""
        pass
    
    @abstractmethod
    def muero(self) -> None:
        """Define que pasa cuando muere."""
        pass
    
    def es_atacado_por(self, atacante: 'Ente') -> None:
        """Es atacado por otro ente."""
        self.vidas -= atacante.poder
        print(f"{self} es atacado por {atacante}, vidas: {self.vidas}")
        
        if self.vidas <= 0:
            self.muero()
    
    def esta_vivo(self) -> bool:
        """Retorna si esta vivo."""
        return self.vidas > 0
    
    def __str__(self) -> str:
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return str(self)
