# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys

# BLINDAJE DE RUTAS: Detecta la carpeta raíz 'Laberinto26' dinámicamente
ruta_actual = os.path.abspath(os.path.dirname(__file__))
if os.path.basename(ruta_actual) == "Solucion":
    ruta_raiz = os.path.abspath(os.path.join(ruta_actual, '..'))
else:
    ruta_raiz = ruta_actual

if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from Builder.director import Director

class VentanaJuego:
    def __init__(self, root, juego):
        self.root = root
        self.juego = juego
        self.root.title("Laberinto Arquitectura 2026 - Vista Gráfica e Interactiva")
        self.root.geometry("950x650")
        self.root.resizable(False, False)

        if not self.juego.person:
            self.juego.agregar_personaje("Héroe")

        # Mapeo de coordenadas calculadas para renderizar las habitaciones en el Canvas
        self.posiciones_habitaciones = {}
        self.calcular_coordenadas_mapa()

        self.crear_componentes()
        self.actualizar_pantalla()
        if self.resolver_combate_en_habitacion_actual():
            self.actualizar_pantalla()

    def calcular_coordenadas_mapa(self):
        """Asigna coordenadas X, Y automáticas a las habitaciones recorriendo sus conexiones."""
        if not self.juego.laberinto:
            return
        
        hab_inicial = self.juego.obtener_habitacion(1)
        if not hab_inicial:
            return

        cola = [(hab_inicial, 250, 150)]  # (Habitacion, X, Y)
        self.posiciones_habitaciones[hab_inicial.num] = (250, 150)

        while cola:
            hab, x, y = cola.pop(0)
            if not hab.forma:
                continue

            for or_obj in hab.forma.orientaciones:
                elemento = hab.forma.obtener_elemento(or_obj)
                if elemento and elemento.es_puerta():
                    # Averiguar cuál es la habitación vecina al otro lado de la puerta
                    vecino = elemento.lado2 if elemento.lado1 == hab else elemento.lado1
                    if vecino and vecino.num not in self.posiciones_habitaciones:
                        dir_name = or_obj.__class__.__name__
                        dx, dy = 0, 0
                        if dir_name == "Norte": dy = -90
                        elif dir_name == "Sur": dy = 90
                        elif dir_name == "Este": dx = 110
                        elif dir_name == "Oeste": dx = -110
                        elif dir_name == "Noreste": dx, dy = 80, -60
                        elif dir_name == "Noroeste": dx, dy = -80, -60
                        elif dir_name == "Sureste": dx, dy = 80, 60
                        elif dir_name == "Suroeste": dx, dy = -80, 60

                        nx, ny = x + dx, y + dy
                        self.posiciones_habitaciones[vecino.num] = (nx, ny)
                        cola.append((vecino, nx, ny))

    def crear_componentes(self):
        # ------------------- PANEL SUPERIOR STATUS -------------------
        self.panel_status = ttk.LabelFrame(self.root, text=" Estado del Personaje ", padding=10)
        self.panel_status.pack(fill="x", padx=15, pady=5)

        self.lbl_nombre = ttk.Label(self.panel_status, text="Personaje: -", font=("Arial", 11, "bold"))
        self.lbl_nombre.pack(side="left", padx=15)

        self.lbl_vidas = ttk.Label(self.panel_status, text="Vidas: -", foreground="red", font=("Arial", 11, "bold"))
        self.lbl_vidas.pack(side="left", padx=15)

        self.lbl_puntos = ttk.Label(self.panel_status, text="Puntos: -", foreground="blue", font=("Arial", 11, "bold"))
        self.lbl_puntos.pack(side="left", padx=15)

        self.lbl_fase = ttk.Label(self.panel_status, text="Fase: -", font=("Arial", 10, "italic"))
        self.lbl_fase.pack(side="right", padx=15)

        # ------------------- ZONA CENTRAL SEPARADA EN 3 PANALES -------------------
        self.zona_central = ttk.Frame(self.root, padding=5)
        self.zona_central.pack(fill="both", expand=True, padx=15)

        # 1. CANVA GRÁFICO (Izquierda)
        self.panel_mapa_visual = ttk.LabelFrame(self.zona_central, text=" Mapa del Laberinto en Tiempo Real ", padding=5)
        self.panel_mapa_visual.pack(side="left", fill="both", expand=True, padx=(0, 5))

        self.canvas = tk.Canvas(self.panel_mapa_visual, bg="#1e1e24", highlightthickness=1, highlightbackground="#333")
        self.canvas.pack(fill="both", expand=True)

        # 2. PANEL DE INFORMACIÓN TEXTUAL (Centro)
        self.panel_hab = ttk.LabelFrame(self.zona_central, text=" Datos de la Sala ", padding=10, width=280)
        self.panel_hab.pack_propagate(False)
        self.panel_hab.pack(side="left", fill="both", padx=(0, 5))

        self.lbl_hab_num = ttk.Label(self.panel_hab, text="Habitación", font=("Arial", 11, "bold"), foreground="#2b2d42")
        self.lbl_hab_num.pack(pady=2)

        self.lbl_contenido_titulo = ttk.Label(self.panel_hab, text="Cosas en el suelo:", font=("Arial", 9, "underline"))
        self.lbl_contenido_titulo.pack(anchor="w", pady=(8, 2))
        
        self.txt_contenido = tk.Text(self.panel_hab, height=8, font=("Courier", 9), bg="#f8f9fa")
        self.txt_contenido.pack(fill="x", pady=2)
        self.txt_contenido.config(state="disabled")

        self.lbl_radar_titulo = ttk.Label(self.panel_hab, text="Salidas / Alrededores:", font=("Arial", 9, "underline"))
        self.lbl_radar_titulo.pack(anchor="w", pady=(8, 2))

        self.txt_radar = tk.Text(self.panel_hab, height=8, font=("Courier", 9), bg="#f8f9fa")
        self.txt_radar.pack(fill="x", pady=2)
        self.txt_radar.config(state="disabled")

        # 3. PANEL DE INVENTARIO (Derecha)
        self.panel_inv = ttk.LabelFrame(self.zona_central, text=" Inventario ", padding=10, width=180)
        self.panel_inv.pack_propagate(False)
        self.panel_inv.pack(side="right", fill="both")

        self.lista_inv = tk.Listbox(self.panel_inv, font=("Arial", 9), bg="#fff")
        self.lista_inv.pack(fill="both", expand=True, pady=2)

        self.btn_usar_item = ttk.Button(self.panel_inv, text="Usar Ítem", command=self.action_usar_item)
        self.btn_usar_item.pack(fill="x", pady=2)

        # ------------------- PANEL INFERIOR CONTROLES -------------------
        self.panel_controles = ttk.LabelFrame(self.root, text=" Panel de Control Direccional ", padding=5)
        self.panel_controles.pack(fill="x", padx=15, pady=10)

        self.btn_norte = ttk.Button(self.panel_controles, text="▲ Norte", command=lambda: self.action_moverse("Norte"))
        self.btn_sur = ttk.Button(self.panel_controles, text="▼ Sur", command=lambda: self.action_moverse("Sur"))
        self.btn_este = ttk.Button(self.panel_controles, text="Este ▶", command=lambda: self.action_moverse("Este"))
        self.btn_oeste = ttk.Button(self.panel_controles, text="◀ Oeste", command=lambda: self.action_moverse("Oeste"))

        self.btn_norte.grid(row=0, column=1, pady=2)
        self.btn_oeste.grid(row=1, column=0, padx=20, pady=2)
        self.btn_este.grid(row=1, column=2, padx=20, pady=2)
        self.btn_sur.grid(row=2, column=1, pady=2)

        self.panel_controles.grid_columnconfigure(0, weight=1)
        self.panel_controles.grid_columnconfigure(1, weight=1)
        self.panel_controles.grid_columnconfigure(2, weight=1)

        self.btn_abrir_puertas = ttk.Button(self.panel_controles, text="Abrir puertas", command=self.action_abrir_puertas)
        self.btn_cerrar_puertas = ttk.Button(self.panel_controles, text="Cerrar puertas", command=self.action_cerrar_puertas)
        self.btn_abrir_puertas.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=(6, 2))
        self.btn_cerrar_puertas.grid(row=3, column=2, columnspan=2, sticky="ew", padx=5, pady=(6, 2))

        # Teclado físico vinculado
        self.root.bind("<Up>", lambda e: self.action_moverse("Norte"))
        self.root.bind("<Down>", lambda e: self.action_moverse("Sur"))
        self.root.bind("<Left>", lambda e: self.action_moverse("Oeste"))
        self.root.bind("<Right>", lambda e: self.action_moverse("Este"))

    def resolver_combate_en_habitacion_actual(self):
        personaje = self.juego.person
        bicho_local = self.juego.buscar_bicho()
        if bicho_local and bicho_local.esta_vivo():
            print(f"[GUI] Batalla iniciada contra {bicho_local}!")
            bicho_local.atacar()
            if personaje.esta_vivo():
                personaje.atacar()
            return True
        return False

    def dibujar_mapa_visual(self):
        """Borra y vuelve a dibujar las salas y pasillos en el Canvas gráfico."""
        self.canvas.delete("all")
        personaje = self.juego.person
        hab_actual_num = personaje.posicion.num if personaje.posicion else -1

        # 1. Dibujar conexiones (Puertas/Pasillos) primero para que queden de fondo
        for num_hab, (x, y) in self.posiciones_habitaciones.items():
            hab = self.juego.obtener_habitacion(num_hab)
            if not hab or not hab.forma: continue
            
            for or_obj in hab.forma.orientaciones:
                el = hab.forma.obtener_elemento(or_obj)
                if el and el.es_puerta():
                    vecino = el.lado2 if el.lado1 == hab else el.lado1
                    if vecino and vecino.num in self.posiciones_habitaciones:
                        vx, vy = self.posiciones_habitaciones[vecino.num]
                        # Dibujar línea de pasillo puente
                        self.canvas.create_line(x, y, vx, vy, fill="#5c677d", width=4)

        # 2. Dibujar los nodos de las habitaciones
        for num_hab, (x, y) in self.posiciones_habitaciones.items():
            hab = self.juego.obtener_habitacion(num_hab)
            es_rombo = hab.forma.__class__.__name__ == "Rombo" if hab else False

            # Colores según si es la sala del personaje o no
            color_fondo = "#4a4e69" if num_hab != hab_actual_num else "#e63946"
            color_borde = "#f2e9e1" if num_hab != hab_actual_num else "#fff"
            grosor_borde = 2 if num_hab != hab_actual_num else 4

            if es_rombo:
                # Dibujar un rombo geométrico usando 4 puntos
                puntos = [x, y - 35, x + 45, y, x, y + 35, x - 45, y]
                self.canvas.create_polygon(puntos, fill=color_fondo, outline=color_borde, width=grosor_borde)
            else:
                # Dibujar un cuadrado tradicional
                self.canvas.create_rectangle(x - 35, y - 35, x + 35, y + 35, fill=color_fondo, outline=color_borde, width=grosor_borde)

            # Texto identificador de la habitación
            self.canvas.create_text(x, y, text=f"Hab {num_hab}", fill="#fff", font=("Arial", 10, "bold"))

            # Si hay bichos custodiando la sala, pintar una marca de aviso
            for bicho in self.juego.bichos:
                if bicho.esta_vivo() and bicho.posicion == hab:
                    self.canvas.create_text(x, y + 20, text="⚠️ BICHO", fill="#ffb703", font=("Arial", 8, "bold"))

        # 3. Dibujar indicador del Avatar del Jugador
        if hab_actual_num in self.posiciones_habitaciones:
            hx, hy = self.posiciones_habitaciones[hab_actual_num]
            # Pequeño círculo verde brillante sobre la sala actual
            self.canvas.create_oval(hx - 10, hy - 45, hx + 10, hy - 25, fill="#52b788", outline="#fff", width=2)

    def actualizar_pantalla(self):
        personaje = self.juego.person
        hab_actual = personaje.posicion

        # Guardar vidas previas para comprobar si el bicho nos ha quitado salud
        vidas_antes = personaje.vidas

        # Actualizar datos numéricos de la cabecera
        puntos_actuales = getattr(personaje, 'puntos', 0)
        self.lbl_nombre.config(text=f"Héroe: {personaje.nombre}")
        self.lbl_vidas.config(text=f"Vidas: {personaje.vidas}")
        self.lbl_puntos.config(text=f"Puntos: {puntos_actuales}")
        self.lbl_fase.config(text=f"Fase: {self.juego.fase.nombre()}")

        if not self.juego.esta_activo():
            self.dibujar_mapa_visual()
            messagebox.showinfo("Fin de la partida", f"Estado final: {self.juego.fase.nombre()}\n¡Revisa la consola!")
            self.root.destroy()
            return

        # Refrescar panel de datos de texto
        if hab_actual:
            self.lbl_hab_num.config(text=f"Estás en: {hab_actual}")
            
            self.txt_contenido.config(state="normal")
            self.txt_contenido.delete("1.0", tk.END)
            if not hab_actual.hijos:
                self.txt_contenido.insert(tk.END, "Suelo limpio de objetos.")
            else:
                for hijo in hab_actual.hijos:
                    self.txt_contenido.insert(tk.END, f"• [{hijo.__class__.__name__}]\n  {hijo}\n")
            self.txt_contenido.config(state="disabled")

            self.txt_radar.config(state="normal")
            self.txt_radar.delete("1.0", tk.END)
            if hab_actual.forma:
                for or_obj in hab_actual.forma.orientaciones:
                    elemento = hab_actual.forma.obtener_elemento(or_obj)
                    self.txt_radar.insert(tk.END, f"{or_obj.__class__.__name__}: {elemento}\n")
            self.txt_radar.config(state="disabled")

        # Refrescar inventario
        self.lista_inv.delete(0, tk.END)
        if hasattr(personaje, 'inventario') and personaje.inventario:
            for item in personaje.inventario.items:
                self.lista_inv.insert(tk.END, str(item))

        # Redibujar los elementos del Canvas
        self.dibujar_mapa_visual()

    def action_abrir_puertas(self):
        print("[GUI] Abriendo puertas...")
        self.juego.abrir_puertas()
        self.actualizar_pantalla()

    def action_cerrar_puertas(self):
        print("[GUI] Cerrando puertas...")
        self.juego.cerrar_puertas()
        self.actualizar_pantalla()

    def action_moverse(self, str_direccion):
        personaje = self.juego.person
        hab_actual = personaje.posicion
        if not hab_actual or not hab_actual.forma: return

        orientacion_objetivo = None
        for or_obj in hab_actual.forma.orientaciones:
            if or_obj.__class__.__name__ == str_direccion:
                orientacion_objetivo = or_obj
                break

        if orientacion_objetivo:
            elemento = hab_actual.forma.obtener_elemento(orientacion_objetivo)
            print(f"\n[GUI] Desplazamiento hacia {str_direccion}...")
            posicion_anterior = personaje.posicion
            elemento.entrar(personaje)

            if personaje.posicion == posicion_anterior and elemento.es_puerta() and elemento.esta_cerrada():
                print(f"[GUI] La puerta {elemento} estaba cerrada; se abre al chocar.")
                elemento.abrir()
                elemento.entrar(personaje)

            if personaje.posicion == posicion_anterior:
                print("[GUI] No se pudo mover; la posición no cambió.")
                self.actualizar_pantalla()
                return

            # Recolectar/accionar de forma automática lo que haya en la nueva habitación
            nueva_hab = personaje.posicion
            for item_suelo in list(nueva_hab.hijos):
                item_suelo.entrar(personaje)

            # Comprobar si hay bichos y resolver el turno de combate síncrono
            self.resolver_combate_en_habitacion_actual()

            self.actualizar_pantalla()
        else:
            print(f"[GUI] No hay salida física hacia el {str_direccion}")

    def action_usar_item(self):
        seleccion = self.lista_inv.curselection()
        if not seleccion: return

        indice = seleccion[0]
        personaje = self.juego.person
        item = personaje.inventario.items[indice]

        print(f"[GUI] Activando objeto: {item}")
        if hasattr(personaje, 'usar_objeto'):
            personaje.usar_objeto(item.__class__, consumir=True)
        else:
            item.usar(personaje)
            personaje.inventario.eliminar(item)

        self.actualizar_pantalla()

if __name__ == "__main__":
    director = Director()
    ruta_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "laberinto4.json"))
    
    if os.path.exists(ruta_json):
        juego_instanciado = director.procesar(ruta_json)
        root_tk = tk.Tk()
        app = VentanaJuego(root_tk, juego_instanciado)
        root_tk.mainloop()
    else:
        print(f"Error crítico: No se encontró el archivo {ruta_json}")