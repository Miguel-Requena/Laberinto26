# -*- coding: utf-8 -*-
from Solucion.orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho
    from Solucion.forma import Forma


class Suroeste(Orientacion):
    """Orientacion SUROESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el suroeste."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.so
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        return forma.so
    
    def poner_elemento(self, elemento, contenedor) -> None:
        contenedor.so = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        contenedor.so.recorrer(bloque)
    
    @staticmethod
    def default():
        return Suroeste()
    
    def __str__(self) -> str:
        return "Suroeste"
