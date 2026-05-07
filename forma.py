from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def tipo(self) -> str:
        pass


class Cuadrado(Forma):
    def tipo(self) -> str:
        return "Cuadrado"


class Rombo(Forma):
    def tipo(self) -> str:
        return "Rombo"
