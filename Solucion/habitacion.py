# -*- coding: utf-8 -*-
from Solucion.contenedor import Contenedor
from Solucion.cuadrado import Cuadrado


class Habitacion(Contenedor):
    """Una habitacion es un contenedor con forma cuadrada."""
    
    def __init__(self, num: int = 0):
        super().__init__()
        self.num = num
        self.forma = Cuadrado()
        self.forma.num = num

    # Compatibility helpers expected by main.py
    @property
    def norte(self):
        return self.forma.norte

    @property
    def sur(self):
        return self.forma.sur

    @property
    def este(self):
        return self.forma.este

    @property
    def oeste(self):
        return self.forma.oeste

    def mostrar_orientaciones(self) -> None:
        """Muestra orientaciones y elementos presentes (compatibilidad)."""
        print(f"Orientaciones en Hab-{self.num}:")
        for o in self.forma.orientaciones:
            try:
                print(f"  - {o}")
            except Exception:
                print("  - orientacion")

    def recorrer_hijos(self):
        """Iterador simple sobre hijos y elementos de la forma."""
        # hijos
        for h in self.hijos:
            yield h
        # orientaciones
        for o in self.forma.orientaciones:
            elem = self.forma.obtener_elemento(o)
            if elem is not None:
                yield elem
    
    def aceptar_contenedor(self, visitor) -> None:
        """Patron Visitor para habitaciones."""
        visitor.visitar_habitacion(self)
    
    def es_armario(self) -> bool:
        return False
    
    def __str__(self) -> str:
        return f"Hab-{self.num}"
