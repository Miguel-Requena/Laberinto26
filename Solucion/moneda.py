# -*- coding: utf-8 -*-
from Solucion.hoja import Hoja
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.ente import Ente


class Moneda(Hoja):
    """Item recolectable que suma puntuacion."""

    def __init__(self, valor: int = 1):
        super().__init__()
        self.valor = valor
        self.recogida = False

    def recoger(self, alguien=None) -> None:
        """Recoge la moneda y suma su valor a la puntuacion de quien la toma."""
        if self.recogida:
            print("La moneda ya fue recogida")
            return

        self.recogida = True
        if alguien is None:
            print(f"Se recoge una moneda de valor {self.valor}")
            return

        if hasattr(alguien, "sumar_puntos"):
            alguien.sumar_puntos(self.valor)
            print(f"{alguien} recoge una moneda (+{self.valor} puntos)")
        else:
            print(f"La moneda no puede sumarse a {alguien}")

    def entrar(self, alguien=None) -> None:
        """Al entrar, la moneda se recoge automaticamente."""
        self.recoger(alguien)

    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_moneda(self)

    def es_moneda(self) -> bool:
        """Retorna True si es una moneda."""
        return True

    def __str__(self) -> str:
        estado = "recogida" if self.recogida else "disponible"
        return f"Moneda({self.valor})-{estado}"

    def __repr__(self) -> str:
        return str(self)
