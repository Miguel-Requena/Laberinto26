from juego import Juego
from juegobombas import JuegoBombas
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso


if __name__ == "__main__":
    print("=== Demostración del Patrón Factory Method ===\n")
    
    # Crear el juego
    juego = Juego()
    
    # Usar el Factory Method para crear un laberinto con 2 habitaciones
    print("Creando laberinto con 2 habitaciones usando fabricarLab2Hab()...")
    laberinto = juego.fabricarLab2Hab()
    print(f"Laberinto creado con {len(laberinto.habitaciones)} habitaciones.\n")
    # Probar los elementos creados.
    print("--- Prueba de elementos creados por Factory Methods ---")
    
    # Probar habitación 1
    print("\nEntrando en habitación 1:")
    hab1 = laberinto.habitaciones[0]
    
    print("  - Mostrando orientaciones disponibles:")
    hab1.mostrar_orientaciones()
    
    print("\n  - Intentando ir al norte (pared):")
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
    
    print("\n=== Fin de la demostración del Factory Method ===\n")
    
    # ====== Demostración del Patrón Strategy ======
    print("\n=== Demostración del Patrón Strategy ===\n")
    
    # Crear estrategias
    modo_agresivo = Agresivo()
    modo_perezoso = Perezoso()
    
    # Crear un bicho con modo agresivo
    print("Creando un bicho con modo Agresivo (100 vidas, 50 poder):")
    bicho1 = Bicho(modo_agresivo, vidas=100, poder=50)
    bicho1.actua()
    
    # Cambiar el modo a perezoso en tiempo de ejecución
    print("\nCambiando el modo del bicho a Perezoso:")
    bicho1.set_modo(modo_perezoso)
    bicho1.actua()
    
    # Volver a cambiar a agresivo
    print("\nCambiando nuevamente a modo Agresivo:")
    bicho1.set_modo(modo_agresivo)
    bicho1.actua()
    
    # Crear otro bicho directamente con modo perezoso
    print("\nCreando un segundo bicho con modo Perezoso (80 vidas, 20 poder):")
    bicho2 = Bicho(modo_perezoso, vidas=80, poder=20)
    bicho2.actua()
    
    # Agregar bichos al laberinto
    print("\nAgregando bichos al laberinto...")
    laberinto.agregar_bicho(bicho1)
    laberinto.agregar_bicho(bicho2)
    print(f"Total de bichos en el laberinto: {len(laberinto.bichos)}")
    
    # Mostrar números de habitaciones
    print("\nNúmeros de las habitaciones creadas:")
    for hab in laberinto.habitaciones:
        print(f"  - Habitación {hab.num}")
    
    print("\n=== Fin de la demostración del Strategy ===")
    
    # ====== Demostración del Patrón Decorator con JuegoBombas ======
    print("\n\n=== Demostración del Patrón Decorator (JuegoBombas) ===\n")
    
    # Crear un juego con bombas
    juego_bombas = JuegoBombas()
    
    print("Creando laberinto con JuegoBombas (elementos decorados con bombas)...")
    laberinto_bombas = juego_bombas.fabricarLab2Hab()
    
    hab1_bombas = laberinto_bombas.habitaciones[0]
    
    print("\nIntentando entrar al norte (pared con bomba):")
    hab1_bombas.norte.entrar()
    
    print("\nActivando la bomba en la pared norte:")
    hab1_bombas.norte.activa = True
    hab1_bombas.norte.entrar()
    
    print("\nIntentando atravesar la puerta del este (con bomba):")
    hab1_bombas.este.activa = True
    hab1_bombas.este.entrar()
    
    print("\n=== Fin de la demostración del Decorator ===")
    
    # ====== Demostración del Patrón Iterator ======
    print("\n\n=== Demostración del Patrón Iterator ===\n")
    
    print("Recorriendo todos los elementos de la habitación 1:")
    for elemento in hab1.recorrer_hijos():
        print(f"  - Elemento encontrado: {elemento.__class__.__name__}")
    
    print("\nRecorriendo todos los elementos de la habitación 1 con bombas:")
    for elemento in hab1_bombas.recorrer_hijos():
        print(f"  - Elemento encontrado: {elemento.__class__.__name__}")
    
    print("\n=== Fin de la demostración del Iterator ===")
    
    print("\n=== Demostración completa finalizada ===" )
