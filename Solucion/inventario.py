# -*- coding: utf-8 -*-
from typing import List
from Solucion.item_recolectable import ItemRecolectable

class Inventario:
    """Contenedor secundario acoplado al personaje para guardar ítems."""
    
    def __init__(self):
        self.items: List[ItemRecolectable] = []

    def agregar(self, item: ItemRecolectable) -> None:
        self.items.append(item)
        print(f"[Inventario] Guardado con éxito: {self._nombre(item)}")

    def usar(self, item: ItemRecolectable, del_personaje=None, consumir: bool = True) -> bool:
        if item not in self.items:
            return False

        item.usar(del_personaje)
        if consumir:
            self.eliminar(item)
        return True

    def tiene_tipo(self, clase_tipo) -> bool:
        """Devuelve True si el inventario contiene alguna instancia de la clase pasada."""
        return any(isinstance(item, clase_tipo) for item in self.items)

    def obtener_tipo(self, clase_tipo):
        """Devuelve el primer ítem que coincida con el tipo pedido."""
        for item in self.items:
            if isinstance(item, clase_tipo):
                return item
        return None

    def eliminar(self, item: ItemRecolectable) -> None:
        if item in self.items:
            self.items.remove(item)
            print(f"[Inventario] Se ha eliminado/consumido: {self._nombre(item)}")

    def usar_tipo(self, clase_tipo, del_personaje=None, consumir: bool = True) -> bool:
        """Usa el primer ítem del tipo indicado."""
        item = self.obtener_tipo(clase_tipo)
        if item is None:
            return False
        return self.usar(item, del_personaje, consumir)

    def _nombre(self, item) -> str:
        return getattr(item, "nombre", str(item))

    def __str__(self) -> str:
        contenidos = ", ".join(self._nombre(item) for item in self.items)
        return f"Inventario([{contenidos}])"

    def __repr__(self) -> str:
        return str(self)