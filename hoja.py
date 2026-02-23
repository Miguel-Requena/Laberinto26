from elemento_mapa import ElementoMapa


class Hoja(ElementoMapa):
    """Clase base para componentes concretos del mapa (hojas del patrón Decorator)."""
    
    def entrar(self) -> None:
        """Método para entrar en el elemento hoja."""
        pass
