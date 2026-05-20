# -*- coding: utf-8 -*-
"""Pruebas simples para la Estrategia Tanque (nuevo modo bicho)."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.tanque import Tanque
from Solucion.bicho import Bicho
from Builder.laberinto_builder import LaberintoBuilder


def test_tanque_creacion():
    """Verifica que la estrategia concreta se instancie de forma correcta."""
    tanque_modo = Tanque()
    assert tanque_modo.es_tanque() is True
    assert tanque_modo.es_agresivo() is False
    assert tanque_modo.es_perezoso() is False
    print("test_tanque_creacion PASSED")


def test_bicho_delegacion_tanque():
    """Verifica que el Bicho delegue polimórficamente las consultas a su modo."""
    tanque_modo = Tanque()
    bicho = Bicho(modo=tanque_modo)
    
    assert bicho.es_tanque() is True
    assert bicho.es_agresivo() is False
    assert bicho.es_perezoso() is False
    print("test_bicho_delegacion_tanque PASSED")


def test_builder_fabricar_tanque():
    """Verifica que el Builder pueda fabricar de forma aislada el objeto de la estrategia."""
    builder = LaberintoBuilder()
    modo_tanque = builder.fabricarTanque()

    assert modo_tanque.es_tanque() is True
    print("test_builder_fabricar_tanque PASSED")


def test_builder_fabricar_bicho_modo_tanque():
    """Verifica que al construir un bicho con modo 'Tanque', el Builder altere dinámicamente sus atributos."""
    builder = LaberintoBuilder()
    # Forzamos la creación de una habitación para alojar al bicho en el builder
    builder.fabricarHabitacion(1)
    
    # Invocamos el método de fabricación pasando la cadena "Tanque"
    bicho_tanque = builder.fabricarBichoModo("Tanque", 1)

    assert bicho_tanque.es_tanque() is True
    assert bicho_tanque.vidas == 150  # Atributo de salud aumentado 
    assert bicho_tanque.poder == 5    # Atributo de daño reducido 
    print("test_builder_fabricar_bicho_modo_tanque PASSED")


def test_builder_bicho_tanque_en_habitacion():
    """Verifica que el bicho con el modo Tanque se instale correctamente en su contenedor."""
    builder = LaberintoBuilder()
    habitacion = builder.fabricarHabitacion(5)
    bicho_tanque = builder.fabricarBichoModo("Tanque", 5)

    # Verificamos que esté agregado tanto en la lista global de bichos como en la habitación
    assert bicho_tanque in builder.juego.bichos
    assert bicho_tanque.posicion == habitacion
    print("test_builder_bicho_tanque_en_habitacion PASSED")


if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Tanque ===\n")

    tests = [
        test_tanque_creacion,
        test_bicho_delegacion_tanque,
        test_builder_fabricar_tanque,
        test_builder_fabricar_bicho_modo_tanque,
        test_builder_bicho_tanque_en_habitacion,
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