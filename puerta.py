from typing import Optional
from hoja import Hoja
from habitacion import Habitacion
from estado_puerta import Cerrada


class Puerta(Hoja):
    
    def __init__(self):
        # Mantener compatibilidad con la API previa (booleano)
        self.abierta: bool = False
        # Estado más rico según diagrama
        self.estado = Cerrada()
        self.lado1: Optional[Habitacion] = None
        self.lado2: Optional[Habitacion] = None
    
    def entrar(self, alguien=None) -> None:
        """Acción de intentar entrar por la puerta."""
        if self.abierta or getattr(self, 'estado', None) is not None and getattr(self.estado, 'es_abierta', lambda: False)():
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
        if getattr(self, 'estado', None) is not None and hasattr(self.estado, 'abrir'):
            self.estado = self.estado.abrir()

    def cerrar(self) -> None:
        self.abierta = False
        if getattr(self, 'estado', None) is not None and hasattr(self.estado, 'cerrar'):
            self.estado = self.estado.cerrar()

    def esPuerta(self) -> bool:
        return True

    def __str__(self) -> str:
        if self.lado1 is None or self.lado2 is None:
            return "Puerta"
        return f"Puerta-{self.lado1.num}-{self.lado2.num}"

    def printOn(self, aStream) -> None:
        aStream.write(str(self))
