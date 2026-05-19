# -*- coding: utf-8 -*-
import copy
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
from pared import Pared
from personaje import Personaje
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from typing import Optional, List


class Juego:
    """Controlador del juego con Factory Methods."""
    
    def __init__(self):
        self.laberinto: Optional[Laberinto] = None
        self.bichos: List = []
        self.person: Optional[Personaje] = None
        self.hilos = {}
        self.prototipo: Optional[Laberinto] = None
    
    def fabricar_laberinto(self) -> Laberinto:
        return Laberinto()
    
    def fabricar_habitacion(self, num: int = 0) -> Habitacion:
        hab = Habitacion(num)
        self.asignar_orientaciones(hab)
        return hab
    
    def asignar_orientaciones(self, contenedor) -> None:
        contenedor.forma.norte = self.fabricar_pared()
        contenedor.forma.sur = self.fabricar_pared()
        contenedor.forma.este = self.fabricar_pared()
        contenedor.forma.oeste = self.fabricar_pared()
    
    def fabricar_pared(self) -> Pared:
        return Pared()
    
    def fabricar_puerta(self) -> Puerta:
        return Puerta()
    
    def fabricar_puerta_entre(self, hab1: Habitacion, hab2: Habitacion) -> Puerta:
        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        return puerta
    
    def fabricar_norte(self):
        return Norte.default()
    
    def fabricar_sur(self):
        return Sur.default()
    
    def fabricar_este(self):
        return Este.default()
    
    def fabricar_oeste(self):
        return Oeste.default()
    
    def fabricar_lab_2hab(self) -> None:
        hab1 = self.fabricar_habitacion(1)
        hab2 = self.fabricar_habitacion(2)
        puerta = self.fabricar_puerta_entre(hab1, hab2)
        hab1.forma.este = puerta
        hab2.forma.oeste = puerta
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        return self.laberinto

    def fabricarLab2Hab(self) -> None:
        return self.fabricar_lab_2hab()

    def fabricarPared(self):
        return self.fabricar_pared()

    def fabricarHabitacion(self, num: int = 0):
        return self.fabricar_habitacion(num)

    def fabricarPuerta(self):
        return self.fabricar_puerta()
    
    def fabricar_lab_4hab(self) -> None:
        hab1 = self.fabricar_habitacion(1)
        hab2 = self.fabricar_habitacion(2)
        hab3 = self.fabricar_habitacion(3)
        hab4 = self.fabricar_habitacion(4)
        
        p12 = self.fabricar_puerta_entre(hab1, hab2)
        p13 = self.fabricar_puerta_entre(hab1, hab3)
        p24 = self.fabricar_puerta_entre(hab2, hab4)
        p34 = self.fabricar_puerta_entre(hab3, hab4)
        
        hab1.forma.sur = p12
        hab2.forma.norte = p12
        hab1.forma.este = p13
        hab3.forma.oeste = p13
        hab2.forma.este = p24
        hab4.forma.oeste = p24
        hab3.forma.sur = p34
        hab4.forma.norte = p34
        
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)
        self.laberinto.agregar_habitacion(hab4)
        return self.laberinto
    
    def agregar_personaje(self, nombre: str) -> None:
        self.person = Personaje(nombre)
        self.person.juego = self
        hab1 = self.obtener_habitacion(1)
        if hab1:
            hab1.entrar(self.person)
    
    def obtener_habitacion(self, num: int) -> Optional[Habitacion]:
        if self.laberinto:
            return self.laberinto.obtener_habitacion(num)
        return None
    
    def numero_habitaciones(self) -> int:
        if self.laberinto:
            return self.laberinto.numero_habitaciones()
        return 0
    
    def agregar_bicho(self, bicho) -> None:
        bicho.juego = self
        self.bichos.append(bicho)
    
    def eliminar_bicho(self, bicho) -> None:
        if bicho in self.bichos:
            self.bichos.remove(bicho)
    
    def lanzar_bicho(self, bicho) -> None:
        print(f"{bicho} se activa")
    
    def lanzar_todos_los_bichos(self) -> None:
        print("Los bichos despiertan")
        for bicho in self.bichos:
            self.lanzar_bicho(bicho)
    
    def buscar_personaje(self, bicho):
        if self.person and bicho.posicion == self.person.posicion:
            return self.person
        return None
    
    def buscar_bicho(self):
        if self.person:
            for bicho in self.bichos:
                if bicho.esta_vivo() and bicho.posicion == self.person.posicion:
                    return bicho
        return None
    
    def muere_bicho(self, bicho) -> None:
        self.eliminar_bicho(bicho)
        if self.todos_muertos():
            print(f"Fin juego. Gana {self.person}")
    
    def muere_personaje(self) -> None:
        self.person.vidas = 0
        print("Manematao. Fin del juego")
        self.terminar_todos_los_bichos()
    
    def todos_muertos(self) -> bool:
        return all(not b.esta_vivo() for b in self.bichos)
    
    def terminar_todos_los_bichos(self) -> None:
        print("Los bichos terminan")
        for bicho in self.bichos:
            bicho.vidas = 0
    
    def activar_bombas(self) -> None:
        def fn(e):
            if hasattr(e, 'activar') and hasattr(e, 'es_bomba') and e.es_bomba():
                e.activar()
        if self.laberinto:
            self.laberinto.recorrer(fn)
    
    def desactivar_bombas(self) -> None:
        def fn(e):
            if hasattr(e, 'desactivar') and hasattr(e, 'es_bomba') and e.es_bomba():
                e.desactivar()
        if self.laberinto:
            self.laberinto.recorrer(fn)
    
    def abrir_puertas(self) -> None:
        def fn(e):
            if hasattr(e, 'abrir') and hasattr(e, 'es_puerta') and e.es_puerta():
                e.abrir()
        if self.laberinto:
            self.laberinto.recorrer(fn)
    
    def cerrar_puertas(self) -> None:
        def fn(e):
            if hasattr(e, 'cerrar') and hasattr(e, 'es_puerta') and e.es_puerta():
                e.cerrar()
        if self.laberinto:
            self.laberinto.recorrer(fn)
    
    def clonar(self) -> Laberinto:
        if self.prototipo:
            return copy.deepcopy(self.prototipo)
        return copy.deepcopy(self.laberinto)
