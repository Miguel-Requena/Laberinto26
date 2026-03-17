import json

from laberinto_builder import LaberintoBuilder


class Director:
    """Orquesta la lectura del JSON y la construcción del juego."""

    def __init__(self):
        self.builder = None
        self.dict = {}
        self.juego = None

    def leerArchivo(self, unArchivo: str) -> dict:
        with open(unArchivo, encoding="utf-8") as archivo:
            self.dict = json.load(archivo)
        return self.dict

    def iniBuilder(self) -> LaberintoBuilder:
        forma = self.dict.get("forma", "")
        if forma == "poligono4":
            self.builder = LaberintoBuilder()
        else:
            raise ValueError(f"Forma de laberinto no soportada: {forma}")
        return self.builder

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict.get("laberinto", []):
            self.fabricarLaberintoRecursivo(each, "root")

        for puerta in self.dict.get("puertas", []):
            self.builder.fabricarPuertaLado1(
                puerta[0],
                puerta[1],
                puerta[2],
                puerta[3],
            )
        return self.builder.laberinto

    def fabricarJuego(self):
        self.juego = self.builder.fabricarJuego()
        return self.juego

    def fabricarBichos(self) -> None:
        for each in self.dict.get("bichos", []):
            self.builder.fabricarBichoModo(each["modo"], each["posicion"])

    def fabricarLaberintoRecursivo(self, unDic: dict, padre):
        con = None
        tipo = unDic.get("tipo", "").lower()

        if tipo == "habitacion":
            con = self.builder.fabricarHabitacion(unDic["num"])
        elif tipo == "armario":
            con = self.builder.fabricarArmario(unDic["num"], padre)
        elif tipo == "bomba":
            con = self.builder.fabricarBombaEn(padre)

        for each in unDic.get("hijos", []):
            self.fabricarLaberintoRecursivo(each, con)

        return con

    def procesar(self, unArchivo: str):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        return self.juego
