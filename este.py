# -*- coding: utf-8 -*-
from orientacion import Orientacion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho
    from forma import Forma


class Este(Orientacion):
    """Orientacion ESTE (Singleton)."""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def caminar(self, bicho: 'Bicho') -> None:
        """El bicho camina hacia el este."""
        if bicho.posicion is None:
            return
        em = bicho.posicion.forma.este
        em.entrar(bicho)
    
    def obtener_elemento(self, forma: 'Forma'):
        """Obtiene el elemento al este."""
        return forma.este
    
    def poner_elemento(self, elemento, contenedor) -> None:
        """Pone un elemento al este."""
        contenedor.este = elemento
    
    def recorrer(self, bloque, contenedor) -> None:
        """Recorre los elementos al este."""
        contenedor.este.recorrer(bloque)
    
    @staticmethod
    def default():
        """Retorna la unica instancia (patron Singleton)."""
        return Este()
    
    def __str__(self) -> str:
        return "Este"
