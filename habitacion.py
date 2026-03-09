from typing import Optional, TYPE_CHECKING, Dict, List, Iterator

if TYPE_CHECKING:
    from elemento_mapa import ElementoMapa

from orientacion import Orientacion
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

# Contador global para asignar números a las habitaciones
_contador_habitaciones = 0


class Habitacion:
    """Representa una habitación en el laberinto."""
    
    def __init__(self):
        global _contador_habitaciones
        _contador_habitaciones += 1
        self.num = _contador_habitaciones
        
        # Inicializar las orientaciones disponibles
        self.orientaciones: Dict[str, Orientacion] = {
            'norte': Norte(),
            'sur': Sur(),
            'este': Este(),
            'oeste': Oeste()
        }
        
        # Atributos para los elementos del mapa en cada dirección
        self.norte: Optional['ElementoMapa'] = None
        self.sur: Optional['ElementoMapa'] = None
        self.este: Optional['ElementoMapa'] = None
        self.oeste: Optional['ElementoMapa'] = None
    
    def entrar(self) -> None:
        """Acción de entrar en la habitación."""
        print("Has entrado en una habitación.")
    
    def mostrar_orientaciones(self) -> None:
        """Muestra las orientaciones disponibles en la habitación."""
        print("Orientaciones disponibles en esta habitación:")
        for key, orientacion in self.orientaciones.items():
            print(f"  - {orientacion.get_nombre()}")
    
    def get_hijos(self) -> List['ElementoMapa']:
        """Retorna los hijos (elementos del mapa) en las 4 direcciones."""
        hijos = []
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
