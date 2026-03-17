from armario import Armario
from agresivo import Agresivo
from bicho import Bicho
from bomba import Bomba
from este import Este
from habitacion import Habitacion
from juego import Juego
from laberinto import Laberinto
from norte import Norte
from oeste import Oeste
from pared import Pared
from perezoso import Perezoso
from puerta import Puerta
from sur import Sur


class LaberintoBuilder:
    """Construye el juego y sus elementos a partir de la estructura descrita en JSON."""

    def __init__(self):
        self.laberinto = Laberinto()
        self.juego = Juego()
        self.juego.laberinto = self.laberinto

    def fabricarJuego(self) -> Juego:
        self.juego.laberinto = self.laberinto
        return self.juego

    def fabricarLaberinto(self) -> Laberinto:
        self.laberinto = Laberinto()
        if self.juego is not None:
            self.juego.laberinto = self.laberinto
        return self.laberinto

    def fabricarPared(self) -> Pared:
        return Pared()

    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarNorte(self) -> Norte:
        return Norte()

    def fabricarSur(self) -> Sur:
        return Sur()

    def fabricarEste(self) -> Este:
        return Este()

    def fabricarOeste(self) -> Oeste:
        return Oeste()

    def fabricarAgresivo(self) -> Agresivo:
        return Agresivo()

    def fabricarPerezoso(self) -> Perezoso:
        return Perezoso()

    def asignarOrientaciones(self, unCont) -> None:
        unCont.orientaciones = [
            self.fabricarNorte(),
            self.fabricarEste(),
            self.fabricarSur(),
            self.fabricarOeste(),
        ]

    def fabricarHabitacion(self, unNum: int) -> Habitacion:
        hab = Habitacion(num=unNum)
        self.asignarOrientaciones(hab)
        for orientacion in hab.orientaciones:
            hab.ponerEn(orientacion, self.fabricarPared())
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarArmario(self, unNum: int, en) -> Armario:
        arm = Armario(num=unNum)
        self.asignarOrientaciones(arm)
        for orientacion in arm.orientaciones:
            arm.ponerEn(orientacion, self.fabricarPared())

        pt = self.fabricarPuerta()
        pt.lado1 = arm
        pt.lado2 = en

        arm.ponerEn(self.fabricarEste(), pt)
        en.agregarHijo(arm)
        return arm

    def fabricarBombaEn(self, unCont):
        bm = Bomba()
        unCont.agregarHijo(bm)
        return bm

    def fabricarPuertaLado1(self, num1: int, or1: str, Lado2: int, or2: str) -> Puerta:
        pt = self.fabricarPuerta()
        lado1 = self.laberinto.obtenerHabitacion(num1)
        lado2 = self.laberinto.obtenerHabitacion(Lado2)

        if lado1 is None or lado2 is None:
            raise ValueError("No se puede crear la puerta: una de las habitaciones no existe.")

        pt.lado1 = lado1
        pt.lado2 = lado2

        objOr1 = getattr(self, f"fabricar{or1}")()
        objOr2 = getattr(self, f"fabricar{or2}")()

        lado1.ponerEn(objOr1, pt)
        lado2.ponerEn(objOr2, pt)
        return pt

    def fabricarBichoModo(self, strModo: str, posicion: int) -> Bicho:
        modo = getattr(self, f"fabricar{strModo}")()
        hab = self.juego.obtenerHabitacion(posicion)
        if hab is None:
            raise ValueError(f"No existe la habitación {posicion} para ubicar el bicho.")

        bicho = Bicho(modo)
        hab.entrar(bicho)
        self.juego.agregarBicho(bicho)
        return bicho
