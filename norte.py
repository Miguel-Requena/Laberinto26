# -*- coding: utf-8 -*-
from orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho
    from forma import Forma


class Norte(Orientacion):
    """Orientacion NORTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el norte."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.norte
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        """Obtiene el elemento al norte."""
        return forma.norte
    
    def poner_elemento(self, elemento, contenedor) -> None:
        """Pone un elemento al norte."""
        contenedor.norte = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        """Recorre los elementos al norte."""
        contenedor.norte.recorrer(bloque)
    
    @staticmethod
    def default():
        """Retorna la unica instancia (patron Singleton)."""
        return Norte()
    
    def __str__(self) -> str:
        return "Norte"
