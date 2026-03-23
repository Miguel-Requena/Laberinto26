from typing import Optional
from hoja import Hoja
from habitacion import Habitacion


class Puerta(Hoja):
    
    def __init__(self):
        self.abierta: bool = False
        self.lado1: Optional[Habitacion] = None
        self.lado2: Optional[Habitacion] = None
    
    def entrar(self, alguien=None) -> None:
        """Acción de intentar entrar por la puerta."""
        if self.abierta:
            if alguien is not None and self.lado1 is not None and self.lado2 is not None:
                if alguien.posicion == self.lado1:
                    self.lado2.entrar(alguien)
                else:
                    self.lado1.entrar(alguien)
                return
            print("Has atravesado la puerta.")
        else:
            print("La puerta está cerrada.")

    def abrir(self) -> None:
        self.abierta = True

    def cerrar(self) -> None:
        self.abierta = False

    def esPuerta(self) -> bool:
        return True

    def __str__(self) -> str:
        if self.lado1 is None or self.lado2 is None:
            return "Puerta"
        return f"Puerta-{self.lado1.num}-{self.lado2.num}"

    def printOn(self, aStream) -> None:
        aStream.write(str(self))
