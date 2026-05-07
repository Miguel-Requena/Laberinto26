from abc import ABC, abstractmethod


class EstadoEnte(ABC):
    @abstractmethod
    def nombre(self) -> str:
        pass


class Vivo(EstadoEnte):
    def nombre(self) -> str:
        return "Vivo"


class Muerto(EstadoEnte):
    def nombre(self) -> str:
        return "Muerto"
