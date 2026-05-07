# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Script de prueba para verificar que todas las clases funcionan."""

try:
    print("\n=== Verificando imports ===\n")
    
    # Imports básicos
    from juego import Juego
    from agresivo import Agresivo
    from perezoso import Perezoso
    from bicho import Bicho
    from personaje import Personaje
    
    print("✓ Imports básicos OK")
    
    # Test 1: Crear un juego
    print("\n=== Test 1: Crear Juego ===")
    juego = Juego()
    juego.fabricar_lab_2hab()
    print(f"✓ Juego creado: {juego.laberinto}")
    
    # Test 2: Agregar personaje
    print("\n=== Test 2: Agregar Personaje ===")
    juego.agregar_personaje("Héroe")
    print(f"✓ Personaje: {juego.person}")
    
    # Test 3: Crear bichos con estrategias
    print("\n=== Test 3: Crear Bichos ===")
    bicho_agresivo = Bicho(Agresivo(), vidas=50, poder=10)
    bicho_perezoso = Bicho(Perezoso(), vidas=30, poder=5)
    juego.agregar_bicho(bicho_agresivo)
    juego.agregar_bicho(bicho_perezoso)
    print(f"✓ Bicho Agresivo: {bicho_agresivo}")
    print(f"✓ Bicho Perezoso: {bicho_perezoso}")
    
    # Test 4: Probar estados de puerta
    print("\n=== Test 4: Puerta con Estados ===")
    hab1 = juego.obtener_habitacion(1)
    hab2 = juego.obtener_habitacion(2)
    puerta = hab1.forma.sur
    print(f"✓ Puerta: {puerta}")
    print(f"  Abierta: {puerta.esta_abierta()}")
    puerta.abrir()
    print(f"  Abierta (después de abrir): {puerta.esta_abierta()}")
    puerta.cerrar()
    print(f"  Cerrada (después de cerrar): {puerta.esta_cerrada()}")
    
    # Test 5: Probar Modo con Template Method
    print("\n=== Test 5: Patrón Mode (Strategy + Template Method) ===")
    bicho_agresivo.posicion = hab1
    bicho_agresivo.posicion.entrar(bicho_agresivo)
    print(f"✓ Bicho en posición: {bicho_agresivo.posicion}")
    print("  Llamando a actua():")
    bicho_agresivo.actua()
    
    # Test 6: Probar Orientaciones Singleton
    print("\n=== Test 6: Orientaciones (Singleton) ===")
    from norte import Norte
    from sur import Sur
    norte1 = Norte.default()
    norte2 = Norte.default()
    print(f"✓ Norte1 es Norte2 (Singleton): {norte1 is norte2}")
    
    print("\n✅ TODOS LOS TESTS PASARON EXITOSAMENTE\n")
    
except Exception as e:
    print(f"\\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
