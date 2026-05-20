# -*- coding: utf-8 -*-
from Solucion.ente import Ente
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.juego import Juego


class Personaje(Ente):
    """El personaje controlado por el jugador."""

    def __init__(self, nombre: str, vidas: int = 100, poder: int = 10):
        super().__init__(vidas=vidas, poder=poder)
        self.nombre = nombre
        self.puntos = 0

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

    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return str(self)
