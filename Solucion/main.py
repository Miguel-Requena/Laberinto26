# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from Solucion.juego import Juego
from Solucion.juegobombas import JuegoBombas
from Solucion.bicho import Bicho
from Solucion.agresivo import Agresivo
from Solucion.perezoso import Perezoso
from Solucion.cofre import Cofre
from Solucion.pocion import Pocion
from Builder.laberinto_builder import LaberintoBuilder


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
    
    print("\nIntentando atravesar la puerta del este (normal):")
    hab1_bombas.este.abierta = True
    hab1_bombas.este.entrar()
    
    print("\n=== Fin de la demostración del Decorator ===")
    
    # ====== Extensión 1: Cofre como hoja nueva ======
    print("\n\n=== Demostración de la Extensión Cofre ===\n")
    
    # Crear cofres de forma manual
    print("Creando cofres manualmente:")
    cofre1 = Cofre("tesoro")
    cofre2 = Cofre("recompensa")
    
    print(f"  - Cofre 1: {cofre1}")
    print(f"  - Cofre 2: {cofre2}")
    
    print("\nAbrir el cofre 1:")
    cofre1.abrir(juego.person)
    
    print(f"\nEstado después de abrir: {cofre1}")
    print(f"¿Es un cofre? {cofre1.es_cofre()}")
    print(f"¿Es una puerta? {cofre1.es_puerta()}")
    
    # Crear cofres usando el Builder
    print("\n\nUsando el Builder para crear cofres:")
    builder = LaberintoBuilder()
    
    hab_test = builder.fabricarHabitacion(10)
    cofre_builder = builder.fabricarCofreEn(hab_test, "tesoro_especial")
    
    print(f"  - Cofre creado con Builder: {cofre_builder}")
    print(f"  - Contenido: {cofre_builder.contenido}")
    print(f"  - Agregado a habitación {hab_test.num}: {cofre_builder in hab_test.hijos}")
    
    # Demostrar entrada automática al cofre
    print("\nPersonaje entra a la habitación y el cofre se abre automáticamente:")
    cofre_nuevo = Cofre("gema")
    cofre_nuevo.entrar(juego.person)
    print(f"  - Cofre después de entrar: {cofre_nuevo}")
    
    print("\n=== Fin de la demostración de Cofre ===")

    # ====== Extensión 2: Pocion de curacion como hoja nueva ======
    print("\n\n=== Demostración de la Extensión Pocion ===\n")

    pocion = Pocion(30)
    print(f"Pocion creada: {pocion}")
    print(f"Vidas iniciales del personaje: {juego.person.vidas}")

    juego.person.vidas = 40
    print("\nUsando la pocion sobre el personaje:")
    pocion.usar(juego.person)
    print(f"Vidas tras usar la pocion: {juego.person.vidas}")

    print(f"¿Es una pocion? {pocion.es_pocion()}")
    print(f"Estado final de la pocion: {pocion}")

    builder = LaberintoBuilder()
    hab_pocion = builder.fabricarHabitacion(20)
    pocion_builder = builder.fabricarPocionEn(hab_pocion, 15)
    print(f"Pocion creada con Builder: {pocion_builder}")
    print(f"Agregada a habitación {hab_pocion.num}: {pocion_builder in hab_pocion.hijos}")

    print("\n=== Fin de la demostración de Pocion ===")
    
    
    print("Recorriendo todos los elementos de la habitación 1:")
    for elemento in hab1.recorrer_hijos():
        print(f"  - Elemento encontrado: {elemento.__class__.__name__}")
    
    print("\nRecorriendo todos los elementos de la habitación 1 con bombas:")
    for elemento in hab1_bombas.recorrer_hijos():
        print(f"  - Elemento encontrado: {elemento.__class__.__name__}")
    
    print("\n=== Fin de la demostración del Iterator ===")
    
    print("\n=== Demostración completa finalizada ===" )
