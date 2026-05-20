# -*- coding: utf-8 -*-
"""Pruebas simples para el inventario del personaje."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Builder.laberinto_builder import LaberintoBuilder
from Solucion.inventario import Inventario
from Solucion.moneda import Moneda
from Solucion.personaje import Personaje
from Solucion.pocion import Pocion


def test_builder_fabricar_inventario():
    builder = LaberintoBuilder()
    inventario = builder.fabricarInventario()

    assert isinstance(inventario, Inventario)
    assert inventario.items == []
    print("test_builder_fabricar_inventario PASSED")


def test_personaje_recoge_pocion_y_la_usa_desde_inventario():
    personaje = Personaje("Heroe", vidas=40)
    pocion = Pocion(25)

    pocion.entrar(personaje)

    assert personaje.tiene_objeto(Pocion) is True
    assert personaje.vidas == 40

    usado = personaje.usar_objeto(Pocion)

    assert usado is True
    assert personaje.vidas == 65
    assert personaje.tiene_objeto(Pocion) is False
    print("test_personaje_recoge_pocion_y_la_usa_desde_inventario PASSED")


def test_personaje_recoge_moneda_y_suma_puntos():
    personaje = Personaje("Heroe")
    moneda = Moneda(7)

    moneda.entrar(personaje)

    assert personaje.puntos == 7
    assert personaje.tiene_objeto(Moneda) is True
    print("test_personaje_recoge_moneda_y_suma_puntos PASSED")


def test_usar_objeto_inexistente_devuelve_false():
    personaje = Personaje("Heroe")

    assert personaje.usar_objeto(Pocion) is False
    print("test_usar_objeto_inexistente_devuelve_false PASSED")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Inventario ===\n")

    tests = [
        test_builder_fabricar_inventario,
        test_personaje_recoge_pocion_y_la_usa_desde_inventario,
        test_personaje_recoge_moneda_y_suma_puntos,
        test_usar_objeto_inexistente_devuelve_false,
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