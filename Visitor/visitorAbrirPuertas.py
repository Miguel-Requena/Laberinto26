# -*- coding: utf-8 -*-

from .visitor import Visitor


class VisitorAbrirPuertas(Visitor):
    def visitar_puerta(self, una_puerta):
        una_puerta.abrir()
