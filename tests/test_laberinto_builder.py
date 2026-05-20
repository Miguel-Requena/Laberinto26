import unittest
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solucion.juego import Juego
from Solucion.tunel import Tunel
from Solucion.bomba import Bomba
from Solucion.bicho import Bicho
from Solucion.agresivo import Agresivo
from Solucion.perezoso import Perezoso


class LaberintoBuilderTest(unittest.TestCase):

    def setUp(self):
        # Cargar dict desde el JSON del repo
        ruta = os.path.join(os.path.dirname(__file__), '..', 'laberinto4.json')
        with open(ruta, 'r', encoding='utf-8') as f:
            self.dict = json.load(f)

        # Construir juego usando Juego y las factory methods
        self.juego = Juego()
        self.juego.fabricar_lab_4hab()

        # Añadir bombas 
        for entry in self.dict.get('laberinto', []):
            if entry.get('tipo') == 'habitacion':
                num = entry.get('num')
                hab = self.juego.obtener_habitacion(num)
                if hab is None:
                    continue
                for hijo in entry.get('hijos', []):
                    if hijo.get('tipo') == 'bomba':
                        hab.agregar_hijo(Bomba())
                    # Añadir cofres
                    elif hijo.get('tipo') == 'cofre':  
                        from Solucion.cofre import Cofre
                        contenido = hijo.get('contenido', 'moneda')
                        hab.agregar_hijo(Cofre(contenido))
                    elif hijo.get('tipo') == 'pocion':
                        from Solucion.pocion import Pocion
                        curacion = hijo.get('curacion', 25)
                        hab.agregar_hijo(Pocion(curacion))
                    elif hijo.get('tipo') == 'trampa':
                        from Solucion.trampa import Trampa
                        dano = hijo.get('dano', 10)
                        hab.agregar_hijo(Trampa(dano))

        # Añadir bichos 
        for b in self.dict.get('bichos', []):
            modo = b.get('modo')
            pos = b.get('posicion')
            modo_obj = Agresivo() if modo == 'Agresivo' else Perezoso()
            bicho = Bicho(modo_obj)
            hab = self.juego.obtener_habitacion(pos)
            if hab:
                hab.entrar(bicho)
            self.juego.agregar_bicho(bicho)

        # Guardar director-like wrapper para compatibilidad de tests
        class D:
            pass

        self.director = D()
        self.director.builder = None  

        # Agregar personaje
        self.juego.agregar_personaje('Miguel')

    def comprobar_armario(self, num, contenedor):
        arm = None
        for each in getattr(contenedor, 'hijos', []):
            if hasattr(each, 'es_armario') and each.es_armario():
                arm = each
                break
        self.assertIsNotNone(arm)
        self.assertTrue(arm.es_armario())
        return arm

    def comprobar_bomba_en(self, contenedor):
        bmb = None
        for each in getattr(contenedor, 'hijos', []):
            if hasattr(each, 'es_bomba') and each.es_bomba():
                bmb = each
                break
        self.assertIsNotNone(bmb)
        self.assertTrue(bmb.es_bomba())
        self.comprobar_funcionamiento_bomba(bmb)

    def comprobar_funcionamiento_bomba(self, una_bomba):
        # comprobar activar/desactivar
        self.assertFalse(getattr(una_bomba, 'activa', False))
        una_bomba.activar()
        self.assertTrue(una_bomba.activa)
        una_bomba.desactivar()
        self.assertFalse(una_bomba.activa)

    def comprobar_funcionamiento_tunel(self, un_tunel):
        self.assertTrue(un_tunel.es_tunel())
        self.assertIsNone(un_tunel.laberinto)
        self.assertIsNotNone(self.juego.person)
        un_tunel.entrar(self.juego.person)
        self.assertIsNotNone(un_tunel.laberinto)
        self.assertEqual(self.juego.numero_habitaciones(), un_tunel.laberinto.numero_habitaciones())

    def comprobar_habitacion(self, num):
        hab = self.juego.obtener_habitacion(num)
        self.assertIsNotNone(hab)
        self.assertEqual(hab.num, num)
        return hab

    def comprobar_laberinto_recursivo(self, unDic, padre):
        contenedor = None
        nada = True

        if unDic.get('tipo') == 'habitacion':
            nada = False
            contenedor = self.comprobar_habitacion(unDic.get('num'))
        if unDic.get('tipo') == 'armario':
            nada = False
            contenedor = self.comprobar_armario(unDic.get('num'), padre)

        if unDic.get('tipo') == 'bomba':
            nada = False
            self.comprobar_bomba_en(padre)
        if unDic.get('tipo') == 'tunel':
            nada = False
            self.comprobar_tunel_en(padre)

        lista = unDic.get('hijos', None)
        if lista is not None:
            for each in lista:
                self.comprobar_laberinto_recursivo(each, contenedor)

        if unDic.get('tipo') == 'cofre':
            nada = False
            self.comprobar_cofre_en(padre)

        if unDic.get('tipo') == 'pocion':
            nada = False
            self.comprobar_pocion_en(padre)

        if unDic.get('tipo') == 'trampa':
            nada = False
            self.comprobar_trampa_en(padre)

        if nada:
            self.fail('Elemento desconocido en el diccionario: %s' % unDic)

    def comprobar_cofre_en(self, unContenedor):
        cofre = None
        for each in getattr(unContenedor, 'hijos', []):
            if hasattr(each, 'es_cofre') and each.es_cofre():
                cofre = each
                break
        self.assertIsNotNone(cofre)
        self.assertTrue(cofre.es_cofre())

    def comprobar_pocion_en(self, unContenedor):
        pocion = None
        for each in getattr(unContenedor, 'hijos', []):
            if hasattr(each, 'es_pocion') and each.es_pocion():
                pocion = each
                break
        self.assertIsNotNone(pocion)
        self.assertTrue(pocion.es_pocion())

    def comprobar_trampa_en(self, unContenedor):
        trampa = None
        for each in getattr(unContenedor, 'hijos', []):
            if hasattr(each, 'es_trampa') and each.es_trampa():
                trampa = each
                break
        self.assertIsNotNone(trampa)
        self.assertTrue(trampa.es_trampa())

    def comprobar_puerta_de(self, unNum, unaOr, otroNum, otraOr):
        unaHab = self.juego.obtener_habitacion(unNum)
        otraHab = self.juego.obtener_habitacion(otroNum)

        self.assertIsNotNone(unaHab)
        self.assertIsNotNone(otraHab)
        self.assertEqual(unaHab.num, unNum)
        self.assertEqual(otraHab.num, otroNum)

        # fabricar orientaciones usando las clases del juego (Norte/Sur/Este/Oeste)
        from Solucion.norte import Norte
        from Solucion.sur import Sur
        from Solucion.este import Este
        from Solucion.oeste import Oeste

        orient_map = {'Norte': Norte.default(), 'Sur': Sur.default(), 'Este': Este.default(), 'Oeste': Oeste.default()}

        or1 = orient_map.get(unaOr)
        or2 = orient_map.get(otraOr)

        pt1 = unaHab.obtener_elemento(or1)
        pt2 = otraHab.obtener_elemento(or2)

        self.assertIsNotNone(pt1)
        self.assertIsNotNone(pt2)
        self.assertTrue(pt1.es_puerta())
        self.assertTrue(pt2.es_puerta())
        self.assertIs(pt1, pt2)
        self.assertFalse(pt1.esta_abierta())

    def comprobar_tunel_en(self, unContenedor):
        tunel = None
        for each in getattr(unContenedor, 'hijos', []):
            if hasattr(each, 'es_tunel') and each.es_tunel():
                tunel = each
                break
        self.assertIsNotNone(tunel)
        self.assertTrue(tunel.es_tunel())
        self.assertIsNone(tunel.laberinto)
        self.comprobar_funcionamiento_tunel(tunel)

    def test_iniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        self.assertIsNotNone(self.juego.person)

    def test_laberinto(self):
        for each in self.dict.get('laberinto', []):
            self.comprobar_laberinto_recursivo(each, 'root')

        for cada in self.dict.get('puertas', []):
            self.comprobar_puerta_de(cada[0], cada[1], cada[2], cada[3])

    def test_puertas(self):
        puertas = set()

        def collect(e):
            if hasattr(e, 'es_puerta') and e.es_puerta():
                puertas.add(e)

        self.juego.laberinto.recorrer(lambda e: collect(e))

        self.assertTrue(all(not p.esta_abierta() for p in puertas))
        self.juego.abrir_puertas()
        self.assertTrue(all(not p.esta_cerrada() for p in puertas))
        self.juego.cerrar_puertas()
        self.assertTrue(all(not p.esta_abierta() for p in puertas))

        unaPuerta = next(iter(puertas)) if puertas else None
        if unaPuerta:
            persona = self.juego.person
            posicion = persona.posicion
            unaPuerta.entrar(persona)
            self.assertEqual(posicion, persona.posicion)
            self.juego.abrir_puertas()
            unaPuerta.entrar(persona)
            self.assertNotEqual(posicion, persona.posicion)

    def test_puertas_abiertas_visitor(self):
        puertas = set()

        def collect(e):
            if hasattr(e, 'es_puerta') and e.es_puerta():
                puertas.add(e)

        self.juego.laberinto.recorrer(lambda e: collect(e))
        self.assertTrue(all(not p.esta_abierta() for p in puertas))

        class VisitorAbrirPuertas:
            def visitar_armario(self, armario):
                pass

            def visitar_bomba(self, bomba):
                pass

            def visitar_habitacion(self, habitacion):
                pass

            def visitar_pared(self, pared):
                pass

            def visitar_puerta(self, puerta):
                puerta.abrir()

            def visitar_tunel(self, tunel):
                pass

            def visitar_cofre(self, cofre):
                pass

            def visitar_pocion(self, pocion):
                pass

            def visitar_trampa(self, trampa):
                pass

        class VisitorCerrarPuertas:
            def visitar_armario(self, armario):
                pass

            def visitar_bomba(self, bomba):
                pass

            def visitar_habitacion(self, habitacion):
                pass

            def visitar_pared(self, pared):
                pass

            def visitar_puerta(self, puerta):
                puerta.cerrar()

            def visitar_tunel(self, tunel):
                pass

            def visitar_cofre(self, cofre):
                pass

            def visitar_pocion(self, pocion):
                pass

            def visitar_trampa(self, trampa):
                pass

        vAP = VisitorAbrirPuertas()
        self.juego.laberinto.aceptar(vAP)
        self.assertTrue(all(not p.esta_cerrada() for p in puertas))

        vCP = VisitorCerrarPuertas()
        self.juego.laberinto.aceptar(vCP)
        self.assertTrue(all(not p.esta_abierta() for p in puertas))

    def test_gana_personaje(self):
        self.juego.terminar_todos_los_bichos()
        self.assertTrue(self.juego.todos_muertos())

    def test_ganan_bichos(self):
        self.skipTest('ToDo')


if __name__ == '__main__':
    unittest.main()
