from typing import Optional
from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta


class Juego:
    """Clase principal que gestiona el juego.
    Implementa el patrón Factory Method para crear elementos del laberinto."""
    
    def __init__(self):
        self.laberinto: Optional[Laberinto] = None
    
    # Factory Methods
    def fabricarPared(self) -> Pared:
        """Factory Method: Crea y retorna una nueva Pared."""
        return Pared()
    
    def fabricarHabitacion(self) -> Habitacion:
        """Factory Method: Crea y retorna una nueva Habitación."""
        return Habitacion()
    
    def fabricarPuerta(self) -> Puerta:
        """Factory Method: Crea y retorna una nueva Puerta."""
        return Puerta()
    
    def fabricarLab2Hab(self) -> Laberinto:
        """Factory Method: Crea y retorna un Laberinto con 2 habitaciones conectadas."""
        # Crear el laberinto
        laberinto = Laberinto()
        
        # Crear las dos habitaciones
        hab1 = self.fabricarHabitacion()
        hab2 = self.fabricarHabitacion()
        
        # Crear una puerta entre las habitaciones
        puerta = self.fabricarPuerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        # Configurar las habitaciones
        hab1.este = puerta
        hab2.oeste = puerta
        
        # Crear paredes para las demás direcciones
        hab1.norte = self.fabricarPared()
        hab1.sur = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        
        hab2.norte = self.fabricarPared()
        hab2.sur = self.fabricarPared()
        hab2.este = self.fabricarPared()
        
        # Agregar habitaciones al laberinto
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        
        return laberinto
    
    def crear_laberinto(self) -> None:
        """Crea un nuevo laberinto."""
        self.laberinto = Laberinto()
        print("Laberinto creado.")
    
    def iniciar(self) -> None:
        """Inicia el juego."""
        if self.laberinto is None:
            self.crear_laberinto()
        print("Juego iniciado.")
    
