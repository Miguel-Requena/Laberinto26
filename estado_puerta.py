from abc import ABC, abstractmethod


class EstadoPuerta(ABC):
    @abstractmethod
    def abrir(self) -> 'EstadoPuerta':
        pass

    @abstractmethod
    def cerrar(self) -> 'EstadoPuerta':
        pass

    @abstractmethod
    def es_abierta(self) -> bool:
        pass


class Abierta(EstadoPuerta):
    def abrir(self) -> 'EstadoPuerta':
        return self

    def cerrar(self) -> 'EstadoPuerta':
        from estado_puerta import Cerrada
        return Cerrada()

    def es_abierta(self) -> bool:
        return True


class Cerrada(EstadoPuerta):
    def abrir(self) -> 'EstadoPuerta':
        from estado_puerta import Abierta
        return Abierta()

    def cerrar(self) -> 'EstadoPuerta':
        return self

    def es_abierta(self) -> bool:
        return False
