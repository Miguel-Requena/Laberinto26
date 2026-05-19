# -*- coding: utf-8 -*-
from Solucion.ente import Ente
from Solucion.modo import Modo
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.personaje import Personaje


class Bicho(Ente):
    """Bicho: usa Strategy (Modo) para comportamiento."""
    
    def __init__(self, modo: Modo, vidas: int = 100, poder: int = 10):
        super().__init__(vidas=vidas, poder=poder)
        self._modo = modo
    
    @property
    def modo(self) -> Modo:
        return self._modo
    
    def set_modo(self, modo: Modo) -> None:
        self._modo = modo
        print(f"El bicho cambio a modo {modo}")
    
    def actua(self) -> None:
        if self.esta_vivo():
            print(f"[Bicho - Vidas: {self.vidas}, Poder: {self.poder}]")
            self._modo.actua(self)
    
    def buscar_enemigo(self) -> Optional['Personaje']:
        if self.juego:
            return self.juego.buscar_personaje(self)
        return None
    
    def muero(self) -> None:
        self.vidas = 0
        if self.juego:
            self.juego.muere_bicho(self)
        print(f"{self} ha muerto")
    
    def es_agresivo(self) -> bool:
        return self._modo.es_agresivo()
    
    def es_perezoso(self) -> bool:
        return self._modo.es_perezoso()
    
    def __str__(self) -> str:
        return f"Bicho-{self._modo}"
