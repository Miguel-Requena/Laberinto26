# -*- coding: utf-8 -*-
from Solucion.contenedor import Contenedor
from typing import Optional

from Solucion.habitacion import Habitacion


class Laberinto(Contenedor):
    """El laberinto es el contenedor principal del juego."""
    
    def __init__(self):
        super().__init__()
        self.hijos = []  # Habitaciones
        self.habitaciones = self.hijos
        self.bichos = []
    
    def agregar_habitacion(self, habitacion: 'Habitacion') -> None:
        """Agrega una habitacion al laberinto."""
        self.agregar_hijo(habitacion)

    def agregar_bicho(self, bicho) -> None:
        """Compatibilidad: agregar un bicho al laberinto."""
        bicho.juego = getattr(bicho, 'juego', None)
        self.bichos.append(bicho)
    
    def obtener_habitacion(self, num: int) -> Optional['Habitacion']:
        """Obtiene una habitacion por numero."""
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None
    
    def numero_habitaciones(self) -> int:
        """Retorna el numero de habitaciones."""
        return len(self.hijos)
    
    def entrar(self, alguien=None) -> None:
        """Entra en el laberinto (por defecto por habitacion 1)."""
        print(f"{alguien} ha entrado en el laberinto")
        hab1 = self.obtener_habitacion(1)
        if hab1:
            hab1.entrar(alguien)
    
    def recorrer(self, bloque) -> None:
        """Recorre todas las habitaciones del laberinto."""
        print("Recorriendo el laberinto")
        for habitacion in self.hijos:
            for _ in habitacion.recorrer(bloque):
                pass
    
    def aceptar_contenedor(self, visitor) -> None:
        """Patron Visitor para el laberinto."""
        # Visita todas sus habitaciones
        for habitacion in self.hijos:
            habitacion.aceptar(visitor)
    
    def __str__(self) -> str:
        return f"Laberinto({len(self.hijos)} habitaciones)"
