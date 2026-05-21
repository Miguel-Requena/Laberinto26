# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.cofre import Cofre
from Solucion.personaje import Personaje
from Builder.laberinto_builder import LaberintoBuilder
from Solucion.llave import Llave


def test_cofre_requires_key():
    personaje = Personaje("Explorador")
    cofre = Cofre("secreto", necesita_llave=True)

    # sin llave no se abre
    cofre.abrir(personaje)
    assert cofre.abierto == False

    # personaje recoge llave
    llave = Llave("Llave Test")
    llave.entrar(personaje)
    assert personaje.tiene_objeto(Llave)

    # ahora puede abrir y la llave se consume
    cofre.abrir(personaje)
    assert cofre.abierto == True
    assert not personaje.tiene_objeto(Llave)


def test_builder_crea_llave_en_habitacion():
    builder = LaberintoBuilder()
    hab = builder.fabricarHabitacion(99)
    llave = builder.fabricarLlaveEn(hab, "LlaveBuilder")
    # comprobar que la llave está en los hijos de la habitación
    assert any(child.__class__.__name__ == 'Llave' for child in hab.hijos)


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Llave ===\n")
    tests = [
        test_cofre_requires_key,
        test_builder_crea_llave_en_habitacion,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"{test.__name__} PASSED")
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1

    print(f"\n=== Resumen ===")
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")
    if failed == 0:
        print("\nTODOS LOS TESTS PASARON\n")
    else:
        print(f"\n{failed} TEST(S) FALLARON\n")
