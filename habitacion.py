import random
from typing import Optional, Dict, List, Iterator
from elemento_mapa import ElementoMapa
from orientacion import Orientacion
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

# Contador global para asignar números a las habitaciones
_contador_habitaciones = 0


class Habitacion(ElementoMapa):
    """Representa una habitación en el laberinto."""
    
    def __init__(self, num: Optional[int] = None):
        global _contador_habitaciones
        if num is None:
            _contador_habitaciones += 1
            self.num = _contador_habitaciones
        else:
            self.num = num
            _contador_habitaciones = max(_contador_habitaciones, num)
        
        # Inicializar las orientaciones disponibles
        self._orientaciones: Dict[str, Orientacion] = {
            'norte': Norte(),
            'sur': Sur(),
            'este': Este(),
            'oeste': Oeste()
        }
        self.contenido: List['ElementoMapa'] = []
        
        # Atributos para los elementos del mapa en cada dirección
        self.norte: Optional['ElementoMapa'] = None
        self.sur: Optional['ElementoMapa'] = None
        self.este: Optional['ElementoMapa'] = None
        self.oeste: Optional['ElementoMapa'] = None

    @property
    def orientaciones(self) -> List[Orientacion]:
        return list(self._orientaciones.values())

    @orientaciones.setter
    def orientaciones(self, nuevas_orientaciones: List[Orientacion]) -> None:
        self._orientaciones = {
            orientacion.get_nombre().lower(): orientacion
            for orientacion in nuevas_orientaciones
        }
    
    def entrar(self, alguien=None) -> None:
        """Acción de entrar en la habitación."""
        if alguien is None:
            print("Has entrado en una habitación.")
            return
        print(f"{alguien} está en {self}")
        alguien.posicion = self

    def agregar_hijo(self, elemento: 'ElementoMapa') -> None:
        """Agrega un elemento interno a la habitación."""
        self.contenido.append(elemento)

    def agregarHijo(self, elemento: 'ElementoMapa') -> None:
        self.agregar_hijo(elemento)

    def poner_en(self, orientacion: Orientacion, elemento: 'ElementoMapa') -> None:
        setattr(self, orientacion.get_nombre().lower(), elemento)

    def ponerEn(self, orientacion: Orientacion, elemento: 'ElementoMapa') -> None:
        self.poner_en(orientacion, elemento)

    def obtener_orientacion_aleatoria(self) -> Orientacion:
        """Devuelve una orientación aleatoria de la habitación."""
        return random.choice(self.orientaciones)

    def obtener_orientacion(self) -> Orientacion:
        return self.obtener_orientacion_aleatoria()

    def obtenerOrientacionAleatoria(self) -> Orientacion:
        """Alias compatible con la nomenclatura del código Pharo."""
        return self.obtener_orientacion_aleatoria()

    def obtenerOrientacion(self) -> Orientacion:
        return self.obtener_orientacion()
    
    def mostrar_orientaciones(self) -> None:
        """Muestra las orientaciones disponibles en la habitación."""
        print("Orientaciones disponibles en esta habitación:")
        for orientacion in self.orientaciones:
            print(f"  - {orientacion.get_nombre()}")
    
    def get_hijos(self) -> List['ElementoMapa']:
        """Retorna los hijos (elementos del mapa) en las 4 direcciones."""
        hijos = list(self.contenido)
        if self.norte:
            hijos.append(self.norte)
        if self.sur:
            hijos.append(self.sur)
        if self.este:
            hijos.append(self.este)
        if self.oeste:
            hijos.append(self.oeste)
        return hijos
    
    def recorrer_hijos(self, bloque=None) -> Iterator['ElementoMapa']:
        """Recorre todos los elementos hijos de la habitación (patrón Iterator/Composite)."""
        for hijo in self.get_hijos():
            yield from hijo.recorrer(bloque)

    def recorrer(self, bloque=None) -> Iterator['ElementoMapa']:
        """Recorre la habitación y todos sus hijos."""
        print(str(self))
        if callable(bloque):
            bloque(self)
        yield self
        for hijo in self.contenido:
            yield from hijo.recorrer(bloque)
        for orientacion in self.orientaciones:
            orientacion.recorrer(bloque, self)

    def __str__(self) -> str:
        return f"Hab-{self.num}"

    def printOn(self, aStream) -> None:
        aStream.write(str(self))
 