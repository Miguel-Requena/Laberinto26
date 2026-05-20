# -*- coding: utf-8 -*-
from hoja import Hoja
from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
    from personaje import Personaje


class Cofre(Hoja):
    """Cofre: hoja que contiene un objeto y lo da al abrirse."""
    
    def __init__(self, contenido: str = "tesoro"):
        super().__init__()
        self.contenido: str = contenido
        self.abierto: bool = False
    
    def abrir(self, personaje: 'Personaje' = None) -> None:
        """Abre el cofre y entrega el contenido al personaje."""
        if self.abierto:
            print(f"El cofre ya estaba abierto")
            return
        
        self.abierto = True
        if personaje:
            print(f"{personaje} abre el cofre y obtiene: {self.contenido}")
        else:
            print(f"El cofre se abre y contiene: {self.contenido}")
    
    def entrar(self, alguien=None) -> None:
        """Al entrar al cofre, se abre automáticamente."""
        if alguien:
            self.abrir(alguien)
        else:
            self.abrir()
    
    def recorrer(self, bloque) -> Iterator[Hoja]:
        """Recorre el cofre (es una hoja, no tiene hijos)."""
        if callable(bloque):
            bloque(self)
        yield self
    
    def aceptar(self, visitor) -> None:
        """Patrón Visitor: acepta un visitante para procesarse."""
        visitor.visitar_cofre(self)
    
    def es_cofre(self) -> bool:
        """Retorna True si es un cofre."""
        return True
    
    def __str__(self) -> str:
        estado = "cerrado" if not self.abierto else "abierto"
        return f"Cofre({self.contenido})-{estado}"
    
    def __repr__(self) -> str:
        return str(self)
