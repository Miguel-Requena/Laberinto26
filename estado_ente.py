# -*- coding: utf-8 -*-
class EstadoEnte:
    def nombre(self) -> str:
        return "EstadoEnte"


class Vivo(EstadoEnte):
    def nombre(self) -> str:
        return "Vivo"


class Muerto(EstadoEnte):
    def nombre(self) -> str:
        return "Muerto"
