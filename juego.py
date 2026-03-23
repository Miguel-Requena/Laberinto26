from typing import Optional
from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta
from personaje import Personaje
from norte import Norte
from este import Este
from sur import Sur
from oeste import Oeste


class Juego:
    """Clase principal que gestiona el juego.
    Implementa el patrón Factory Method para crear elementos del laberinto."""
    
    def __init__(self):
        self.laberinto: Optional[Laberinto] = None
        self.personaje: Optional[Personaje] = None
        self.bichos = []
    
    # Factory Methods
    def fabricarPared(self) -> Pared:
        """Factory Method: Crea y retorna una nueva Pared."""
        return Pared()
    
    def fabricarHabitacion(self, unNum: int | None = None) -> Habitacion:
        """Factory Method: Crea y retorna una nueva Habitación."""
        hab = Habitacion(num=unNum)
        self.asignarOrientaciones(hab)
        for orientacion in hab.orientaciones:
            hab.ponerEn(orientacion, self.fabricarPared())
        return hab
    
    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarNorte(self) -> Norte:
        return Norte()

    def fabricarEste(self) -> Este:
        return Este()

    def fabricarSur(self) -> Sur:
        return Sur()

    def fabricarOeste(self) -> Oeste:
        return Oeste()

    def asignarOrientaciones(self, unCont) -> None:
        unCont.orientaciones = [
            self.fabricarNorte(),
            self.fabricarEste(),
            self.fabricarSur(),
            self.fabricarOeste(),
        ]
    
    def fabricarLab2Hab(self) -> Laberinto:
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

    def obtener_habitacion(self, num: int) -> Habitacion | None:
        """Busca una habitación por número dentro del laberinto actual."""
        if self.laberinto is None:
            return None
        return self.laberinto.obtener_habitacion(num)

    def obtenerHabitacion(self, unNum: int) -> Habitacion | None:
        """Alias compatible con la nomenclatura del código Pharo."""
        return self.obtener_habitacion(unNum)

    def agregar_bicho(self, bicho) -> None:
        self.bichos.append(bicho)
        if self.laberinto is not None:
            self.laberinto.agregar_bicho(bicho)

    def agregarBicho(self, bicho) -> None:
        self.agregar_bicho(bicho)

    def agregar_personaje(self, nombre: str) -> Personaje:
        """Crea un personaje y lo coloca en la habitación 1."""
        self.personaje = Personaje(nombre)
        habitacion_inicial = self.obtener_habitacion(1)
        if habitacion_inicial is None:
            raise ValueError("No existe la habitación 1 en el laberinto actual.")
        habitacion_inicial.entrar(self.personaje)
        return self.personaje

    def agregarPersonaje(self, unaCadena: str) -> Personaje:
        """Alias compatible con la nomenclatura del código Pharo."""
        return self.agregar_personaje(unaCadena)

    def abrirPuertas(self) -> None:
        if self.laberinto is None:
            return

        def abrir_si_puerta(each) -> None:
            if each.esPuerta():
                each.abrir()

        self.laberinto.recorrer(abrir_si_puerta)

    def cargar_desde_json(self, ruta_json: str) -> Laberinto:
        """Construye un laberinto a partir de un archivo JSON."""
        from director import Director

        director = Director()
        director.procesar(ruta_json)
        self.laberinto = director.juego.laberinto
        self.bichos = director.juego.bichos
        return self.laberinto
    
