# -*- coding: utf-8 -*-
"""
Script de prueba simple para la extensión Cofre (sin pytest).
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.cofre import Cofre
from Solucion.personaje import Personaje
from Builder.laberinto_builder import LaberintoBuilder

def test_cofre_creacion():
    """Test: Cofre se crea correctamente con contenido."""
    cofre = Cofre("tesoro")
    assert cofre.contenido == "tesoro"
    assert cofre.abierto == False
    assert cofre.es_cofre() == True
    print("test_cofre_creacion PASSED")

def test_cofre_abrir_sin_personaje():
    """Test: Cofre se abre y imprime contenido."""
    cofre = Cofre("recompensa")
    cofre.abrir()
    assert cofre.abierto == True
    print("test_cofre_abrir_sin_personaje PASSED")

def test_cofre_abrir_ya_abierto():
    """Test: Cofre ya abierto no puede abrirse de nuevo."""
    cofre = Cofre("recompensa")
    cofre.abrir()
    cofre.abrir()  # Intenta abrir de nuevo
    assert cofre.abierto == True
    print("test_cofre_abrir_ya_abierto PASSED")

def test_cofre_abrir_con_personaje():
    """Test: Cofre entrega contenido al personaje."""
    personaje = Personaje("Héroe")
    cofre = Cofre("recompensa")
    cofre.abrir(personaje)
    assert cofre.abierto == True
    print("test_cofre_abrir_con_personaje PASSED")

def test_cofre_entrar_auto_abre():
    """Test: Al entrar, el cofre se abre automáticamente."""
    cofre = Cofre("tesoro")
    cofre.entrar()
    assert cofre.abierto == True
    print("test_cofre_entrar_auto_abre PASSED")

def test_cofre_es_hoja():
    """Test: Cofre es considerado una hoja."""
    cofre = Cofre("tesoro")
    assert cofre.es_pared() == False
    assert cofre.es_puerta() == False
    assert cofre.es_tunel() == False
    assert cofre.es_cofre() == True
    print("test_cofre_es_hoja PASSED")

def test_cofre_str():
    """Test: Representación en string."""
    cofre = Cofre("tesoro")
    assert "Cofre" in str(cofre)
    assert "cerrado" in str(cofre)
    
    cofre.abrir()
    cofre_str = str(cofre)
    assert "abierto" in cofre_str
    print("test_cofre_str PASSED")

def test_builder_fabricar_cofre():
    """Test: Builder puede fabricar un Cofre."""
    builder = LaberintoBuilder()
    cofre = builder.fabricarCofre("recompensa")
    assert cofre.es_cofre() == True
    assert cofre.contenido == "recompensa"
    print("test_builder_fabricar_cofre PASSED")

def test_builder_fabricar_cofre_en_habitacion():
    """Test: Builder puede agregar Cofre a una habitación."""
    builder = LaberintoBuilder()
    habitacion = builder.fabricarHabitacion(1)
    cofre = builder.fabricarCofreEn(habitacion, "tesoro")
    
    assert cofre in habitacion.hijos
    assert cofre.es_cofre() == True
    print("test_builder_fabricar_cofre_en_habitacion PASSED")

if __name__ == "__main__":
    print("\n=== Ejecutando Tests de Cofre ===\n")
    
    tests = [
        test_cofre_creacion,
        test_cofre_abrir_sin_personaje,
        test_cofre_abrir_ya_abierto,
        test_cofre_abrir_con_personaje,
        test_cofre_entrar_auto_abre,
        test_cofre_es_hoja,
        test_cofre_str,
        test_builder_fabricar_cofre,
        test_builder_fabricar_cofre_en_habitacion,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
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
        print(f"\n{failed} TESTS FALLARON\n")
