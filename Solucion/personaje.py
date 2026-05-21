# -*- coding: utf-8 -*-
from Solucion.ente import Ente
from typing import Optional, TYPE_CHECKING
from Solucion.item_recolectable import ItemRecolectable
from Solucion.inventario import Inventario

if TYPE_CHECKING:
    from Solucion.juego import Juego


class Personaje(Ente):
    """El personaje controlado por el jugador."""

    def __init__(self, nombre: str, vidas: int = 100, poder: int = 10):
        super().__init__(vidas=vidas, poder=poder)
        # Ajuste: aumentar poder por defecto para que los ataques del héroe sean efectivos
        if poder == 10:
            self.poder = 25
        self.nombre = nombre
        self.puntos = 0
        self.inventario = Inventario()

    def buscar_enemigo(self) -> Optional['Ente']:
        """Busca un bicho en su misma posicion."""
        if self.juego:
            return self.juego.buscar_bicho()
        return None

    def muero(self) -> None:
        """El personaje muere."""
        if self.juego:
            self.juego.muere_personaje()

    def ir_a(self, orientacion) -> None:
        """Se mueve en una direccion."""
        orientacion.caminar(self)

    def ir_al_norte(self) -> None:
        """Se mueve al norte."""
        if self.posicion:
            from Solucion.norte import Norte
            Norte.default().caminar(self)

    def sumar_puntos(self, puntos: int) -> None:
        """Incrementa la puntuacion acumulada del personaje."""
        if puntos <= 0:
            return
        self.puntos += puntos
        print(f"{self} suma {puntos} puntos, total: {self.puntos}")

    def agregar(self, item: ItemRecolectable) -> None:
        """Método delegado para añadir al inventario."""
        self.inventario.agregar(item)

    def eliminar(self, item: ItemRecolectable) -> None:
        """Método delegado para eliminar del inventario."""
        self.inventario.eliminar(item)

    def tiene_objeto(self, clase_tipo) -> bool:
        """Método delegado para comprobar la existencia de un tipo de objeto."""
        return self.inventario.tiene_tipo(clase_tipo)

    def usar_item(self, item: ItemRecolectable, consumir: bool = True) -> bool:
        """Usa un ítem concreto del inventario."""
        return self.inventario.usar(item, self, consumir)

    def usar_objeto(self, clase_tipo, consumir: bool = True) -> bool:
        """Usa el primer ítem de un tipo concreto del inventario."""
        return self.inventario.usar_tipo(clase_tipo, self, consumir)

    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return str(self)
