# -*- coding: utf-8 -*-
import time
from Solucion.modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.bicho import Bicho


class Agresivo(Modo):
    """Estrategia concreta: modo agresivo."""
    
    def duerme(self, bicho: 'Bicho') -> None:
        print(f"{bicho} duerme")
        time.sleep(1)  
    
    def es_agresivo(self) -> bool:
        return True
    
    def es_perezoso(self) -> bool:
        return False
    
    def __str__(self) -> str:
        return "Agresivo"
    
    def __repr__(self) -> str:
        return str(self)
