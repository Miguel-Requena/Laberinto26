from juego import Juego
from bomba import Bomba
from pared import Pared
from puerta import Puerta
from elemento_mapa import ElementoMapa


class JuegoBombas(Juego):
    """Juego especializado que crea elementos con bombas.
    Hereda de Juego y sobrescribe los Factory Methods."""
    
    def fabricarPared(self) -> ElementoMapa:
        """Factory Method: Crea y retorna una Pared decorada con Bomba."""
        pared = Pared()
        bomba = Bomba(pared)
        return bomba
    
    def fabricarPuerta(self) -> ElementoMapa:
        """Factory Method: Crea y retorna una Puerta decorada con Bomba."""
        puerta = Puerta()
        bomba = Bomba(puerta)
        return bomba
