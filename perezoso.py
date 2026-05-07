# -*- coding: utf-8 -*-
import time
from modo import Modo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Perezoso(Modo):
    """Estrategia concreta: modo perezoso."""
    
    def duerme(self, bicho: 'Bicho') -> None:
        print(f"{bicho} duerme")
        time.sleep(3)  
    
    def es_agresivo(self) -> bool:
        return False
    
    def es_perezoso(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return "Perezoso"
    
    def __repr__(self) -> str:
        return str(self)
