# -*- coding: utf-8 -*-
import time
from Solucion.modo import Modo
from typing import TYPE_CHECKING

from Solucion.bicho import Bicho


class Tanque(Modo):
    """Estrategia concreta: modo tanque."""
    
    def duerme(self, bicho: 'Bicho') -> None:
        print(f"{bicho} duerme")
        time.sleep(1)  
    
    def es_agresivo(self) -> bool:
        return False
    
    def es_perezoso(self) -> bool:
        return False
    def es_tanque(self) -> bool:
        return True
    def __str__(self) -> str:
        return "Tanque"
    
    def __repr__(self) -> str:
        return str(self)