from habitacion import Habitacion


class Armario(Habitacion):
    """Contenedor interno conectado a otro contenedor mediante una puerta."""

    def __str__(self) -> str:
        return f"Armario {self.num}"
