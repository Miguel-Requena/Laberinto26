# -*- coding: utf-8 -*-
from .laberinto_builder import LaberintoBuilder
from Solucion.rombo import Rombo


class LaberintoBuilderRombo(LaberintoBuilder):
    """Construye laberintos con forma rombo."""

    def fabricarForma(self):
        return Rombo()

    def _orientaciones_de_forma(self):
        return [
            self.fabricarNoreste(),
            self.fabricarNoroeste(),
            self.fabricarSureste(),
            self.fabricarSuroeste(),
        ]

    def _orientacion_puerta_armario(self):
        return self.fabricarNoreste()
