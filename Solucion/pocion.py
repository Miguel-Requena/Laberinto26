# -*- coding: utf-8 -*-
from Solucion.item_recolectable import ItemRecolectable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.ente import Ente


class Pocion(ItemRecolectable):
    """Pocion de curacion que recupera vidas al usarse."""

    def __init__(self, curacion: int = 25):
        super().__init__()
        self.curacion = curacion
        self.usada = False

    def usar(self, alguien=None) -> None:
        """Aplica la curacion a quien la use."""
        if self.usada:
            print("La pocion ya fue usada")
            return

        self.usada = True
        if alguien is None:
            print(f"La pocion se usa y recupera {self.curacion} vidas")
            return

        if hasattr(alguien, 'curar'):
            print(f"{alguien} usa una pocion de curacion")
            alguien.curar(self.curacion)
        else:
            print(f"La pocion no puede curar a {alguien}")

    def entrar(self, alguien=None) -> None:
        """Al entrar, la pocion se recoge para poder usarse desde el inventario."""
        if self.usada:
            print("La pocion ya fue usada")
            return

        if alguien is None:
            print(f"La pocion queda disponible para ser recogida ({self.curacion} vidas)")
            return

        if hasattr(alguien, 'agregar'):
            print(f"{alguien} recoge una pocion de curacion")
            alguien.agregar(self)
        else:
            self.usar(alguien)

    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_pocion(self)

    def es_pocion(self) -> bool:
        """Retorna True si es una pocion."""
        return True

    def __str__(self) -> str:
        estado = "usada" if self.usada else "sin usar"
        return f"Pocion({self.curacion})-{estado}"

    def __repr__(self) -> str:
        return str(self)