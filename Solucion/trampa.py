# -*- coding: utf-8 -*-
from Solucion.hoja import Hoja
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.ente import Ente


class Trampa(Hoja):
    """Trampa de pinchos que causa daño al entrar."""

    def __init__(self, dano: int = 10):
        super().__init__()
        self.dano = dano
        self.activada = False

    def activar(self, alguien=None) -> None:
        """Activa la trampa y causa daño."""
        if self.activada:
            print("La trampa ya fue disparada")
            return

        self.activada = True
        if alguien is None:
            print(f"La trampa se dispara y causa {self.dano} de daño")
            return

        if hasattr(alguien, 'es_atacado_por'):
            print(f"{alguien} dispara la trampa de pinchos")
            # Simular ataque sin atacante real
            alguien.vidas -= self.dano
            print(f"{alguien} recibe {self.dano} de daño, vida: {alguien.vidas}")
            if alguien.vidas <= 0:
                alguien.muero()
        else:
            print(f"La trampa no puede afectar a {alguien}")

    def entrar(self, alguien=None) -> None:
        """Al entrar, la trampa se activa de inmediato."""
        self.activar(alguien)

    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        visitor.visitar_trampa(self)

    def es_trampa(self) -> bool:
        """Retorna True si es una trampa."""
        return True

    def __str__(self) -> str:
        estado = "disparada" if self.activada else "activa"
        return f"Trampa({self.dano})-{estado}"

    def __repr__(self) -> str:
        return str(self)
