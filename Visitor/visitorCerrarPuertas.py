# -*- coding: utf-8 -*-

from .visitor import Visitor


class VisitorCerrarPuertas(Visitor):
    def visitar_puerta(self, una_puerta):
        una_puerta.cerrar()
