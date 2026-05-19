# -*- coding: utf-8 -*-
from Solucion.juego import Juego
from Solucion.pared_bomba import ParedBomba


class JuegoBombas(Juego):
    """Variante con bombas en lugar de paredes."""
    
    def fabricar_pared(self) -> ParedBomba:
        return ParedBomba()
