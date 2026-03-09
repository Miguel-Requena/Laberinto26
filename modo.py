from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bicho import Bicho


class Modo(ABC):
    """Clase abstracta que define el comportamiento de un modo (Strategy)."""
    
    @abstractmethod
    def actua(self, bicho: 'Bicho') -> None:
        """Define cómo actúa el bicho según su modo."""
        pass
    
    @abstractmethod
    def caminar(self) -> None:
        """Define cómo camina el bicho."""
        pass
    
    @abstractmethod
    def atacar(self) -> None:
        """Define cómo ataca el bicho."""
        pass
    
    @abstractmethod
    def dormir(self) -> None:
        """Define cómo duerme el bicho."""
        pass
