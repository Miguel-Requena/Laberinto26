# -*- coding: utf-8 -*-
from Solucion.orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho
    from Solucion.forma import Forma


class Sureste(Orientacion):
    """Orientacion SURESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el sureste."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.se
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        return forma.se
    
    def poner_elemento(self, elemento, contenedor) -> None:
        contenedor.se = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        contenedor.se.recorrer(bloque)
    
    @staticmethod
    def default():
        return Sureste()
    
    def __str__(self) -> str:
        return "Sureste"
