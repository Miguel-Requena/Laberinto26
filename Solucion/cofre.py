# -*- coding: utf-8 -*-
from Solucion.hoja import Hoja
from typing import TYPE_CHECKING, Iterator
from Solucion.llave import Llave

if TYPE_CHECKING:
    from Solucion.personaje import Personaje


class Cofre(Hoja):
    """Cofre: hoja que contiene un objeto y lo da al abrirse.

    Ahora puede requerir una llave (`Llave`) para abrirse si
    `necesita_llave` es True. En ese caso el `Personaje` debe
    tener una `Llave` en su inventario; la llave se consume al usarla.
    """

    def __init__(self, contenido: str = "tesoro", necesita_llave: bool = False):
        super().__init__()
        self.contenido: str = contenido
        self.abierto: bool = False
        self.necesita_llave: bool = necesita_llave
    
    def abrir(self, personaje: 'Personaje' = None) -> None:
        """Abre el cofre y entrega el contenido al personaje.

        Si `necesita_llave` es True se comprueba que `personaje` tenga
        una `Llave` en su inventario; si la tiene se usa (y se consume).
        """
        if self.abierto:
            print(f"El cofre ya estaba abierto")
            return

        if self.necesita_llave:
            if personaje is None:
                print("El cofre necesita una llave para abrirse.")
                return
            if not personaje.tiene_objeto(Llave):
                print("El cofre necesita una llave para abrirse.")
                return
            # usar y consumir la llave
            personaje.usar_objeto(Llave, consumir=True)

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
        llave = " (requiere llave)" if self.necesita_llave else ""
        return f"Cofre({self.contenido})-{estado}{llave}"
    
    def __repr__(self) -> str:
        return str(self)
