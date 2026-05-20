# -*- coding: utf-8 -*-
"""Pruebas simples para la pocion de curacion."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.pocion import Pocion
from Solucion.personaje import Personaje
from Builder.laberinto_builder import LaberintoBuilder


def test_pocion_creacion():
    pocion = Pocion(30)
    assert pocion.curacion == 30
    assert pocion.usada is False
    assert pocion.es_pocion() is True
    print("test_pocion_creacion PASSED")


def test_pocion_usar_sobre_personaje():
    personaje = Personaje("Héroe", vidas=40)
    pocion = Pocion(25)

    pocion.usar(personaje)

    assert personaje.vidas == 65
    assert pocion.usada is True
    print("test_pocion_usar_sobre_personaje PASSED")


def test_pocion_no_se_reutiliza():
    personaje = Personaje("Héroe", vidas=40)
    pocion = Pocion(25)

    pocion.usar(personaje)
    pocion.usar(personaje)

    assert personaje.vidas == 65
    print("test_pocion_no_se_reutiliza PASSED")


def test_builder_fabricar_pocion():
    builder = LaberintoBuilder()
    pocion = builder.fabricarPocion(15)

    assert pocion.es_pocion() is True
    assert pocion.curacion == 15
    print("test_builder_fabricar_pocion PASSED")


def test_builder_fabricar_pocion_en_habitacion():
    builder = LaberintoBuilder()
    habitacion = builder.fabricarHabitacion(1)
    pocion = builder.fabricarPocionEn(habitacion, 20)

    assert pocion in habitacion.hijos
    assert pocion.es_pocion() is True
    print("test_builder_fabricar_pocion_en_habitacion PASSED")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Pocion ===\n")

    tests = [
        test_pocion_creacion,
        test_pocion_usar_sobre_personaje,
        test_pocion_no_se_reutiliza,
        test_builder_fabricar_pocion,
        test_builder_fabricar_pocion_en_habitacion,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as exc:
            print(f"✗ {test.__name__} FAILED: {exc}")
            failed += 1

    print("\n=== Resumen ===")
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\nTODOS LOS TESTS PASARON\n")
    else:
        print(f"\n{failed} TESTS FALLARON\n")