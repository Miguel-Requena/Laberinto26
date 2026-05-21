# -*- coding: utf-8 -*-
import os
import sys
# Añade la carpeta raíz (Laberinto26) al camino de búsqueda de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.armario import Armario
from Solucion.agresivo import Agresivo
from Solucion.bicho import Bicho
from Solucion.bomba import Bomba
from Solucion.cofre import Cofre
from Solucion.cuadrado import Cuadrado
from Solucion.este import Este
from Solucion.habitacion import Habitacion
from Solucion.juego import Juego
from Solucion.laberinto import Laberinto
from Solucion.inventario import Inventario
from Solucion.moneda import Moneda
from Solucion.noreste import Noreste
from Solucion.noroeste import Noroeste
from Solucion.norte import Norte
from Solucion.oeste import Oeste
from Solucion.pared import Pared
from Solucion.perezoso import Perezoso
from Solucion.pocion import Pocion
from Solucion.puerta import Puerta
from Solucion.trampa import Trampa
from Solucion.sur import Sur
from Solucion.sureste import Sureste
from Solucion.suroeste import Suroeste
from Solucion.tunel import Tunel
from Solucion.tanque import Tanque
from Solucion.llave import Llave

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

    def fabricarInventario(self) -> Inventario:
        return Inventario()

    

    def fabricarPuerta(self) -> Puerta:
        return Puerta()

    def fabricarCofre(self, contenido: str = "tesoro") -> Cofre:
        return Cofre(contenido)

    def fabricarLlave(self, nombre: str = "Llave") -> Llave:
        return Llave(nombre)

    def fabricarPocion(self, curacion: int = 25) -> Pocion:
        return Pocion(curacion)

    def fabricarTrampa(self, dano: int = 10) -> Trampa:
        return Trampa(dano)

    def fabricarMoneda(self, valor: int = 1) -> Moneda:
        return Moneda(valor)

    def fabricarForma(self):
        return Cuadrado()

    def fabricarNorte(self) -> Norte:
        return Norte()

    def fabricarSur(self) -> Sur:
        return Sur()

    def fabricarEste(self) -> Este:
        return Este()

    def fabricarOeste(self) -> Oeste:
        return Oeste()

    def fabricarNoreste(self) -> Noreste:
        return Noreste()

    def fabricarNoroeste(self) -> Noroeste:
        return Noroeste()

    def fabricarSureste(self) -> Sureste:
        return Sureste()

    def fabricarSuroeste(self) -> Suroeste:
        return Suroeste()

    def fabricarAgresivo(self) -> Agresivo:
        return Agresivo()

    def fabricarPerezoso(self) -> Perezoso:
        return Perezoso()

    def asignarOrientaciones(self, unCont) -> None:
        if hasattr(unCont, 'norte'):
            unCont.norte = self.fabricarPared()
        if hasattr(unCont, 'este'):
            unCont.este = self.fabricarPared()
        if hasattr(unCont, 'sur'):
            unCont.sur = self.fabricarPared()
        if hasattr(unCont, 'oeste'):
            unCont.oeste = self.fabricarPared()
        if hasattr(unCont, 'ne'):
            unCont.ne = self.fabricarPared()
        if hasattr(unCont, 'no'):
            unCont.no = self.fabricarPared()
        if hasattr(unCont, 'se'):
            unCont.se = self.fabricarPared()
        if hasattr(unCont, 'so'):
            unCont.so = self.fabricarPared()

    def _orientaciones_de_forma(self):
        return [
            self.fabricarNorte(),
            self.fabricarEste(),
            self.fabricarSur(),
            self.fabricarOeste(),
        ]

    def _orientacion_puerta_armario(self):
        return self.fabricarEste()

    def fabricarHabitacion(self, unNum: int) -> Habitacion:
        hab = Habitacion(num=unNum)
        hab.forma = self.fabricarForma()
        hab.forma.num = unNum
        self.asignarOrientaciones(hab.forma)
        for orientacion in self._orientaciones_de_forma():
            hab.poner_elemento(orientacion, self.fabricarPared())
        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricarArmario(self, unNum: int, en) -> Armario:
        arm = Armario(num=unNum)
        arm.forma = self.fabricarForma()
        arm.forma.num = unNum
        self.asignarOrientaciones(arm.forma)
        for orientacion in self._orientaciones_de_forma():
            arm.poner_elemento(orientacion, self.fabricarPared())

        pt = self.fabricarPuerta()
        pt.lado1 = arm
        pt.lado2 = en

        arm.poner_elemento(self._orientacion_puerta_armario(), pt)
        en.agregar_hijo(arm)
        return arm

    def fabricarBombaEn(self, unCont):
        bm = Bomba()
        unCont.agregar_hijo(bm)
        return bm

    def fabricarTunelEn(self, unCont):
        tn = Tunel()
        unCont.agregar_hijo(tn)
        return tn

    # ==== Extension 1: Cofres ====
    def fabricarCofreEn(self, unCont, contenido: str = "tesoro"):
        cf = self.fabricarCofre(contenido)
        unCont.agregar_hijo(cf)
        return cf

    # ==== Extension 2: Pociones ====
    def fabricarPocionEn(self, unCont, curacion: int = 25):
        poc = self.fabricarPocion(curacion)
        unCont.agregar_hijo(poc)
        return poc

    # ==== Extension 3: Trampas ====
    def fabricarTrampaEn(self, unCont, dano: int = 10):
        tr = self.fabricarTrampa(dano)
        unCont.agregar_hijo(tr)
        return tr
    
    # ==== Extension 4: Monedas ====
    def fabricarMonedaEn(self, unCont, valor: int = 1):
        mon = self.fabricarMoneda(valor)
        unCont.agregar_hijo(mon)
        return mon
    
    #==== Extension 5: Tanques como modo de bicho ====
    def fabricarTanque(self) -> Tanque:
        return Tanque()
    
    #==== Extension 6: Inventario Demo ====
    def fabricarInventarioDemo(self, items_demo=None) -> Inventario:
        inventario = self.fabricarInventario()
        for item_demo in items_demo or []:
            tipo = item_demo.get("tipo")
            if tipo == "pocion":
                inventario.agregar(self.fabricarPocion(item_demo.get("curacion", 25)))
            elif tipo == "moneda":
                inventario.agregar(self.fabricarMoneda(item_demo.get("valor", 1)))
            elif tipo == "llave":
                inventario.agregar(self.fabricarLlave(item_demo.get("nombre", "Llave")))
        return inventario

    # ==== Extension 7: Llaves ====
    def fabricarLlaveEn(self, unCont, nombre: str = "Llave"):
        llave = self.fabricarLlave(nombre)
        unCont.agregar_hijo(llave)
        return llave

    

    def fabricarPuertaLado1(self, num1: int, or1: str, Lado2: int, or2: str) -> Puerta:
        pt = self.fabricarPuerta()
        lado1 = self.laberinto.obtener_habitacion(num1)
        lado2 = self.laberinto.obtener_habitacion(Lado2)

        if lado1 is None or lado2 is None:
            raise ValueError("No se puede crear la puerta: una de las habitaciones no existe.")

        pt.lado1 = lado1
        pt.lado2 = lado2

        objOr1 = getattr(self, f"fabricar{or1}")()
        objOr2 = getattr(self, f"fabricar{or2}")()

        lado1.poner_elemento(objOr1, pt)
        lado2.poner_elemento(objOr2, pt)
        return pt

    def fabricarBichoModo(self, strModo: str, posicion: int) -> Bicho:
        modo = getattr(self, f"fabricar{strModo}")()
        hab = self.juego.obtener_habitacion(posicion)
        if hab is None:
            raise ValueError(f"No existe la habitación {posicion} para ubicar el bicho.")

        # Modificación 5 para el bicho Tanque
        if modo.es_tanque():
            bicho = Bicho(modo, vidas = 150, poder = 5) # Tanques tienen más vidas pero menos poder
        elif modo.es_agresivo():
            bicho = Bicho(modo, vidas = 100, poder=15) # Bichos normales
        else:
            bicho = Bicho(modo, vidas = 100, poder=5) # Bichos perezosos u otros
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)
        return bicho
 