# -*- coding: utf-8 -*-
from Solucion.item_recolectable import ItemRecolectable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.personaje import Personaje


class Llave(ItemRecolectable):
    """Llave: ítem recogible que puede abrir cofres."""

    def __init__(self, nombre: str = "Llave"):
        super().__init__(nombre)

    def entrar(self, del_personaje: 'Personaje') -> None:
        """Cuando el personaje entra en la casilla con la llave, la recoge."""
        if del_personaje:
            del_personaje.agregar(self)

    def usar(self, del_personaje: 'Personaje') -> None:
        """Efecto al usar la llave (por defecto sólo informa)."""
        if del_personaje:
            print(f"{del_personaje} usa {self.nombre}.")

    def aceptar(self, visitor) -> None:
        """Patrón Visitor: permite a visitantes procesar la llave."""
        if hasattr(visitor, 'visitar_llave'):
            visitor.visitar_llave(self)

    def es_llave(self) -> bool:
        return True
    def es_cofre(self) -> bool:
        return False

    def es_pocion(self) -> bool:
        return False

    def es_trampa(self) -> bool:
        return False

    def es_moneda(self) -> bool:
        return False