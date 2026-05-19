# -*- coding: utf-8 -*-
from Solucion.orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho
    from Solucion.forma import Forma


class Noroeste(Orientacion):
    """Orientacion NOROESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el noroeste."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.no
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        return forma.no
    
    def poner_elemento(self, elemento, contenedor) -> None:
        contenedor.no = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        contenedor.no.recorrer(bloque)
    
    @staticmethod
    def default():
        return Noroeste()
    
    def __str__(self) -> str:
        return "Noroeste"
