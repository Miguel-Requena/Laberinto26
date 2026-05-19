# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Solucion.puerta import Puerta


class EstadoPuerta(ABC):
    
    @abstractmethod
    def abrir(self, puerta: 'Puerta') -> None:
        """Intenta abrir la puerta."""
        pass

    @abstractmethod
    def cerrar(self, puerta: 'Puerta') -> None:
        """Intenta cerrar la puerta."""
        pass

    @abstractmethod
    def entrar(self, alguien, puerta: 'Puerta') -> None:
        """Define como se comporta cuando alguien intenta entrar."""
        pass

    @abstractmethod
    def esta_abierta(self) -> bool:
        """Retorna True si la puerta esta abierta."""
        pass

    @abstractmethod
    def esta_cerrada(self) -> bool:
        """Retorna True si la puerta esta cerrada."""
        pass

    def es_abierta(self) -> bool:
        """Compatibilidad alias."""
        return self.esta_abierta()


class Abierta(EstadoPuerta):
    """Estado: Puerta Abierta."""
    
    def abrir(self, puerta: 'Puerta') -> None:
        """Ya esta abierta, no hace nada."""
        print(f"Abrimos {self._get_puerta_str(puerta)}")
    
    def cerrar(self, puerta: 'Puerta') -> None:
        """Cierra la puerta y cambia estado."""
        print(f"Cerramos {self._get_puerta_str(puerta)}")
        puerta.estado = Cerrada()
    
    def entrar(self, alguien, puerta: 'Puerta') -> None:
        """Permite entrar y atravesar la puerta."""
        if alguien is not None and puerta.lado1 is not None and puerta.lado2 is not None:
            if alguien.posicion == puerta.lado1:
                puerta.lado2.entrar(alguien)
            else:
                puerta.lado1.entrar(alguien)
        else:
            print(f"Puerta abierta {self._get_puerta_str(puerta)}")
    
    def esta_abierta(self) -> bool:
        return True
    
    def esta_cerrada(self) -> bool:
        return False
    
    def _get_puerta_str(self, puerta) -> str:
        return str(puerta)


class Cerrada(EstadoPuerta):
    """Estado: Puerta Cerrada."""
    
    def abrir(self, puerta: 'Puerta') -> None:
        """Abre la puerta y cambia estado."""
        print(f"Abrimos {self._get_puerta_str(puerta)}")
        puerta.estado = Abierta()
    
    def cerrar(self, puerta: 'Puerta') -> None:
        """Ya esta cerrada, no hace nada."""
        print(f"Cerramos {self._get_puerta_str(puerta)}")
    
    def entrar(self, alguien, puerta: 'Puerta') -> None:
        """No permite entrar, puerta cerrada."""
        print(f"Puerta {self._get_puerta_str(puerta)} cerrada")
    
    def esta_abierta(self) -> bool:
        return False
    
    def esta_cerrada(self) -> bool:
        return True
    
    def _get_puerta_str(self, puerta) -> str:
        return str(puerta)
