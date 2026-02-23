from juego import Juego


if __name__ == "__main__":
    print("=== Demostración del Patrón Factory Method ===\n")
    
    # Crear el juego
    juego = Juego()
    
    # Usar el Factory Method para crear un laberinto con 2 habitaciones
    print("Creando laberinto con 2 habitaciones usando fabricarLab2Hab()...")
    laberinto = juego.fabricarLab2Hab()
    print(f"Laberinto creado con {len(laberinto.habitaciones)} habitaciones.\n")
    
    # Probar los elementos creados
    print("--- Prueba de elementos creados por Factory Methods ---")
    
    # Probar habitación 1
    print("\nEntrando en habitación 1:")
    hab1 = laberinto.habitaciones[0]
    
    print("  - Intentando ir al norte (pared):")
    hab1.norte.entrar()
    
    print("  - Intentando ir al este (puerta):")
    hab1.este.entrar()
    
    print("  - Abriendo la puerta y volviendo a intentar:")
    hab1.este.abierta = True
    hab1.este.entrar()
    
    # Probar habitación 2
    print("\nEntrando en habitación 2:")
    hab2 = laberinto.habitaciones[1]
    
    print("  - Intentando ir al sur (pared):")
    hab2.sur.entrar()
    
    print("  - Intentando ir al oeste (puerta abierta):")
    hab2.oeste.entrar()
    
    # Demostrar creación individual de elementos con Factory Methods
    print("\n--- Creación individual de elementos ---")
    pared = juego.fabricarPared()
    print("Pared creada con fabricarPared():")
    pared.entrar()
    
    habitacion = juego.fabricarHabitacion()
    print("\nHabitación creada con fabricarHabitacion():")
    habitacion.entrar()
    
    puerta = juego.fabricarPuerta()
    print("\nPuerta creada con fabricarPuerta():")
    puerta.entrar()
    
    print("\n=== Fin de la demostración ===" )
