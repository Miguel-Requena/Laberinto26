# -*- coding: utf-8 -*-
"""Pruebas simples para Moneda (item recolectable)."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.moneda import Moneda
from Solucion.personaje import Personaje
from Builder.laberinto_builder import LaberintoBuilder


def test_moneda_creacion():
    moneda = Moneda(5)
    assert moneda.valor == 5
    assert moneda.recogida is False
    assert moneda.es_moneda() is True
    print("test_moneda_creacion PASSED")


def test_moneda_recoger_sobre_personaje():
    personaje = Personaje("Heroe")
    moneda = Moneda(7)

    moneda.recoger(personaje)

    assert personaje.puntos == 7
    assert moneda.recogida is True
    print("test_moneda_recoger_sobre_personaje PASSED")


def test_moneda_no_se_reutiliza():
    personaje = Personaje("Heroe")
    moneda = Moneda(7)

    moneda.recoger(personaje)
    moneda.recoger(personaje)

    assert personaje.puntos == 7
    print("test_moneda_no_se_reutiliza PASSED")


def test_builder_fabricar_moneda():
    builder = LaberintoBuilder()
    moneda = builder.fabricarMoneda(3)

    assert moneda.es_moneda() is True
    assert moneda.valor == 3
    print("test_builder_fabricar_moneda PASSED")


def test_builder_fabricar_moneda_en_habitacion():
    builder = LaberintoBuilder()
    habitacion = builder.fabricarHabitacion(1)
    moneda = builder.fabricarMonedaEn(habitacion, 9)

    assert moneda in habitacion.hijos
    assert moneda.es_moneda() is True
    print("test_builder_fabricar_moneda_en_habitacion PASSED")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Moneda ===\n")

    tests = [
        test_moneda_creacion,
        test_moneda_recoger_sobre_personaje,
        test_moneda_no_se_reutiliza,
        test_builder_fabricar_moneda,
        test_builder_fabricar_moneda_en_habitacion,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as exc:
            print(f"x {test.__name__} FAILED: {exc}")
            failed += 1

    print("\n=== Resumen ===")
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\nTODOS LOS TESTS PASARON\n")
    else:
        print(f"\n{failed} TESTS FALLARON\n")
