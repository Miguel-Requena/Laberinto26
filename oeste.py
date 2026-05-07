# -*- coding: utf-8 -*-
from orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho
    from forma import Forma


class Oeste(Orientacion):
    """Orientacion OESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el oeste."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.oeste
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        """Obtiene el elemento al oeste."""
        return forma.oeste
    
    def poner_elemento(self, elemento, contenedor) -> None:
        """Pone un elemento al oeste."""
        contenedor.oeste = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        """Recorre los elementos al oeste."""
        contenedor.oeste.recorrer(bloque)
    
    @staticmethod
    def default():
        """Retorna la unica instancia (patron Singleton)."""
        return Oeste()
    
    def __str__(self) -> str:
        return "Oeste"
