from abc import ABC, abstractmethod


class Fase(ABC):
    @abstractmethod
    def nombre(self) -> str:
        pass


class Inicial(Fase):
    def nombre(self) -> str:
        return "Inicial"


class Jugando(Fase):
    def nombre(self) -> str:
        return "Jugando"


class Final(Fase):
    def nombre(self) -> str:
        return "Final"
