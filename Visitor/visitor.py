# -*- coding: utf-8 -*-


class Visitor:
    """Interfaz base de visitantes para el patrón Visitor."""

    def visitar_armario(self, un_armario):
        pass

    def visitar_bomba(self, una_bomba):
        pass

    def visitar_habitacion(self, una_hab):
        pass

    def visitar_pared(self, una_pared):
        pass

    def visitar_puerta(self, una_puerta):
        pass

    def visitar_tunel(self, un_tunel):
        pass
