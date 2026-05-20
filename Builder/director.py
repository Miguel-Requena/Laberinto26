# -*- coding: utf-8 -*-
import json

from .laberinto_builder import LaberintoBuilder
from .laberinto_builder_rombo import LaberintoBuilderRombo


class Director:
    """Director del patrón Builder para construir laberintos desde JSON."""

    def __init__(self, builder=None, dict=None):
        self.builder = builder
        self.dict = dict or {}

    def leerArchivo(self, unArchivo):
        with open(unArchivo, "r", encoding="utf-8") as archivo:
            self.dict = json.load(archivo)
        return self.dict

    def iniBuilder(self):
        if self.dict.get("forma") == "rombo":
            self.builder = LaberintoBuilderRombo()
        else:
            self.builder = LaberintoBuilder()
        return self.builder

    def fabricarJuego(self):
        return self.builder.fabricarJuego()

    def fabricarLaberintoRecursivo(self, unDic, padre):
        tipo = unDic.get("tipo")

        if tipo == "habitacion":
            con = self.builder.fabricarHabitacion(unDic.get("num", 0))
        elif tipo == "armario":
            con = self.builder.fabricarArmario(unDic.get("num", 0), padre)
        elif tipo == "bomba":
            return self.builder.fabricarBombaEn(padre)
        elif tipo == "tunel":
            return self.builder.fabricarTunelEn(padre)
        elif tipo == "cofre":
            return self.builder.fabricarCofreEn(padre, unDic.get("contenido", "tesoro"))
        elif tipo == "pocion":
            return self.builder.fabricarPocionEn(padre, unDic.get("curacion", 25))
        elif tipo == "trampa":
            return self.builder.fabricarTrampaEn(padre, unDic.get("dano", 10))
        else:
            return None

        for each in unDic.get("hijos", []):
            self.fabricarLaberintoRecursivo(each, con)

        return con

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()

        for each in self.dict.get("laberinto", []):
            self.fabricarLaberintoRecursivo(each, "root")

        for each in self.dict.get("puertas", []):
            self.builder.fabricarPuertaLado1(each[0], each[1], each[2], each[3])

        return self.builder.laberinto

    def fabricarBichos(self):
        for each in self.dict.get("bichos", []):
            self.builder.fabricarBichoModo(each.get("modo"), each.get("posicion"))

    def obtenerJuego(self):
        if self.builder is None:
            return None
        return self.builder.juego

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        return self.obtenerJuego()
