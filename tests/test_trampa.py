# -*- coding: utf-8 -*-
"""Pruebas simples para la trampa de pinchos."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.trampa import Trampa
from Solucion.personaje import Personaje
from Builder.laberinto_builder import LaberintoBuilder


def test_trampa_creacion():
    trampa = Trampa(20)
    assert trampa.dano == 20
    assert trampa.activada is False
    assert trampa.es_trampa() is True
    print("test_trampa_creacion PASSED")


def test_trampa_activar_sobre_personaje():
    personaje = Personaje("Héroe", vidas=100)
    trampa = Trampa(30)

    trampa.activar(personaje)

    assert personaje.vidas == 70
    assert trampa.activada is True
    print("test_trampa_activar_sobre_personaje PASSED")


def test_trampa_no_se_reutiliza():
    personaje = Personaje("Héroe", vidas=100)
    trampa = Trampa(30)

    trampa.activar(personaje)
    trampa.activar(personaje)

    assert personaje.vidas == 70
    print("test_trampa_no_se_reutiliza PASSED")


def test_trampa_entrar():
    personaje = Personaje("Héroe", vidas=100)
    trampa = Trampa(15)

    trampa.entrar(personaje)

    assert personaje.vidas == 85
    assert trampa.activada is True
    print("test_trampa_entrar PASSED")


def test_builder_fabricar_trampa():
    builder = LaberintoBuilder()
    trampa = builder.fabricarTrampa(25)

    assert trampa.es_trampa() is True
    assert trampa.dano == 25
    print("test_builder_fabricar_trampa PASSED")


def test_builder_fabricar_trampa_en_habitacion():
    builder = LaberintoBuilder()
    habitacion = builder.fabricarHabitacion(1)
    trampa = builder.fabricarTramapaEn(habitacion, 20)

    assert trampa in habitacion.hijos
    assert trampa.es_trampa() is True
    print("test_builder_fabricar_trampa_en_habitacion PASSED")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Trampa ===\n")

    tests = [
        test_trampa_creacion,
        test_trampa_activar_sobre_personaje,
        test_trampa_no_se_reutiliza,
        test_trampa_entrar,
        test_builder_fabricar_trampa,
        test_builder_fabricar_trampa_en_habitacion,
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
