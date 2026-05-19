# -*- coding: utf-8 -*-
from Solucion.orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho
    from Solucion.forma import Forma


class Noreste(Orientacion):
    """Orientacion NORESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el noreste."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.ne
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        return forma.ne
    
    def poner_elemento(self, elemento, contenedor) -> None:
        contenedor.ne = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        contenedor.ne.recorrer(bloque)
    
    @staticmethod
    def default():
        return Noreste()
    
    def __str__(self) -> str:
        return "Noreste"
