# -*- coding: utf-8 -*-
from Solucion.orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho
    from Solucion.forma import Forma


class Sur(Orientacion):
    """Orientacion SUR (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el sur."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.sur
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        """Obtiene el elemento al sur."""
        return forma.sur
    
    def poner_elemento(self, elemento, contenedor) -> None:
        """Pone un elemento al sur."""
        contenedor.sur = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        """Recorre los elementos al sur."""
        contenedor.sur.recorrer(bloque)
    
    @staticmethod
    def default():
        """Retorna la unica instancia (patron Singleton)."""
        return Sur()
    
    def __str__(self) -> str:
        return "Sur"
