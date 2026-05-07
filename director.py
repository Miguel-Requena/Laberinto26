# -*- coding: utf-8 -*-
class Director:
    """Director para construccion de laberintos."""
    
    def __init__(self, builder):
        self.builder = builder
    
    def construir_laberinto(self):
        return self.builder.construir()
