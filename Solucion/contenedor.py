# -*- coding: utf-8 -*-
from Solucion.elemento_mapa import ElementoMapa
from typing import Iterator, List, TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.forma import Forma


class Contenedor(ElementoMapa):
    
    def __init__(self):
        super().__init__()
        self.hijos: List[ElementoMapa] = []
        self.forma: 'Forma' = None
        self.num: int = 0
    
    def agregar_hijo(self, elemento: ElementoMapa) -> None:
        """Agrega un elemento hijo."""
        self.hijos.append(elemento)
    
    def remover_hijo(self, elemento: ElementoMapa) -> None:
        """Remueve un elemento hijo."""
        if elemento in self.hijos:
            self.hijos.remove(elemento)
    
    def obtener_elemento(self, orientacion) -> ElementoMapa:
        """Obtiene un elemento en una direccion."""
        if self.forma:
            return self.forma.obtener_elemento(orientacion)
        return None
    
    def poner_elemento(self, orientacion, elemento: ElementoMapa) -> None:
        """Pone un elemento en una direccion."""
        if self.forma:
            self.forma.poner_elemento(orientacion, elemento)
    
    def obtener_orientacion_aleatoria(self):
        """Obtiene una orientacion aleatoria."""
        if self.forma:
            return self.forma.obtener_orientacion_aleatoria()
        return None
    
    def entrar(self, alguien=None) -> None:
        """Entra en el contenedor."""
        if alguien:
            print(f"{alguien} esta en {self}")
            alguien.posicion = self
    
    def recorrer(self, bloque) -> Iterator[ElementoMapa]:
        """Recorre el contenedor y sus hijos (Composite)."""
        print(f"Recorriendo {self}")
        if callable(bloque):
            bloque(self)
        yield self
        
        # Recorre los hijos
        for hijo in self.hijos:
            yield from hijo.recorrer(bloque)
        
        # Recorre las orientaciones
        if self.forma:
            for orientacion in self.forma.orientaciones:
                elemento = self.obtener_elemento(orientacion)
                if elemento:
                    yield from elemento.recorrer(bloque)
    
    def aceptar(self, visitor) -> None:
        """Patron Visitor."""
        self.aceptar_contenedor(visitor)
        
        # Visita todos los hijos
        for hijo in self.hijos:
            hijo.aceptar(visitor)
        
        # Visita las orientaciones
        if self.forma:
            for orientacion in self.forma.orientaciones:
                elemento = self.obtener_elemento(orientacion)
                if elemento:
                    elemento.aceptar(visitor)
    
    def aceptar_contenedor(self, visitor) -> None:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}-{self.num}"
