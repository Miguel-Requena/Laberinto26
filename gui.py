# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox

from Solucion.juego import Juego
from Solucion.juegobombas import JuegoBombas
from Solucion.bicho import Bicho
from Solucion.agresivo import Agresivo
from Solucion.perezoso import Perezoso


class LaberintoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Laberinto - GUI")
        self.geometry("980x600")

        self.juego = None
        self.laberinto = None
        self.modo_bombas = False

        # Widgets
        toolbar = ttk.Frame(self)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=6, pady=6)

        self.btn_create = ttk.Button(toolbar, text="Crear laberinto (normal)", command=lambda: self.crear_laberinto(False))
        self.btn_create.pack(side=tk.LEFT)

        self.btn_create_bombas = ttk.Button(toolbar, text="Crear laberinto (bombas)", command=lambda: self.crear_laberinto(True))
        self.btn_create_bombas.pack(side=tk.LEFT, padx=(6, 0))

        self.lbl_count = ttk.Label(toolbar, text="Habitaciones: 0")
        self.lbl_count.pack(side=tk.LEFT, padx=10)

        self.lbl_mode = ttk.Label(toolbar, text="Modo: normal")
        self.lbl_mode.pack(side=tk.LEFT, padx=10)

        main = ttk.Frame(self)
        main.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Left: lista de habitaciones
        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(left, text="Habitaciones").pack(anchor=tk.W)
        self.lst_habs = tk.Listbox(left, height=20, width=24)
        self.lst_habs.pack(fill=tk.Y, expand=False)
        self.lst_habs.bind("<<ListboxSelect>>", self.on_hab_select)

        ttk.Label(left, text="Bichos").pack(anchor=tk.W, pady=(10, 0))
        self.lst_bichos = tk.Listbox(left, height=10, width=24)
        self.lst_bichos.pack(fill=tk.Y, expand=False)

        bicho_actions = ttk.Frame(left)
        bicho_actions.pack(fill=tk.X, pady=(6, 0))
        self.btn_add_aggressive = ttk.Button(bicho_actions, text="Añadir agresivo", command=self.anadir_bicho_agresivo)
        self.btn_add_aggressive.pack(fill=tk.X)
        self.btn_add_lazy = ttk.Button(bicho_actions, text="Añadir perezoso", command=self.anadir_bicho_perezoso)
        self.btn_add_lazy.pack(fill=tk.X, pady=(4, 0))
        self.btn_run_bichos = ttk.Button(bicho_actions, text="Lanzar bichos", command=self.lanzar_bichos)
        self.btn_run_bichos.pack(fill=tk.X, pady=(4, 0))

        self.lbl_bicho_hint = ttk.Label(left, text="Usa estos botones para crear bichos.")
        self.lbl_bicho_hint.pack(anchor=tk.W, pady=(6, 0))

        self.lbl_state = ttk.Label(left, text="Estado: sin juego")
        self.lbl_state.pack(anchor=tk.W, pady=(10, 0))

        # Right: detalles
        right = ttk.Frame(main)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(right, text="Detalles").pack(anchor=tk.W)
        self.txt_detalles = tk.Text(right, wrap=tk.WORD, height=8)
        self.txt_detalles.pack(fill=tk.X, expand=False)

        # Canvas para la vista jugable
        self.canvas = tk.Canvas(right, bg="#f0f0f0")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Estado gráfico
        self.room_items = {}  # room.num -> rect id
        self.door_items = []  # list of (line_id, puerta)
        self.player_item = None
        self.bicho_items = []

        # Footer with actions
        footer = ttk.Frame(self)
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=6, pady=6)

        self.btn_toggle = ttk.Button(footer, text="Abrir/Cerrar puerta seleccionada", command=self.toggle_puerta)
        self.btn_toggle.pack(side=tk.LEFT)
        self.btn_open = ttk.Button(footer, text="Abrir puerta", command=self.abrir_puerta_seleccionada)
        self.btn_open.pack(side=tk.LEFT, padx=(6, 0))
        self.btn_close = ttk.Button(footer, text="Cerrar puerta", command=self.cerrar_puerta_seleccionada)
        self.btn_close.pack(side=tk.LEFT, padx=(6, 0))

        self.btn_activate_bombs = ttk.Button(footer, text="Activar bombas", command=self.activar_bombas)
        self.btn_activate_bombs.pack(side=tk.LEFT, padx=(18, 0))
        self.btn_deactivate_bombs = ttk.Button(footer, text="Desactivar bombas", command=self.desactivar_bombas)
        self.btn_deactivate_bombs.pack(side=tk.LEFT, padx=(6, 0))

        # Bind teclas para mover
        self.bind_all("<Up>", lambda e: self.mover_personaje('N'))
        self.bind_all("<Down>", lambda e: self.mover_personaje('S'))
        self.bind_all("<Left>", lambda e: self.mover_personaje('W'))
        self.bind_all("<Right>", lambda e: self.mover_personaje('E'))
        # Bind click en canvas para alternar puertas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def crear_laberinto(self, con_bombas: bool = False):
        self.modo_bombas = con_bombas
        self.juego = JuegoBombas() if con_bombas else Juego()
        self.laberinto = self.juego.fabricarLab2Hab()
        if con_bombas:
            self.juego.activar_bombas()
        self.lbl_mode.config(text=f"Modo: {'bombas activas' if con_bombas else 'normal'}")
        # Añadir personaje automáticamente
        try:
            self.juego.agregar_personaje("Jugador")
        except Exception:
            pass
        self.actualizar_lista()
        self.actualizar_lista_bichos()
        self.actualizar_estado_juego()
        # seleccionar la primera habitacion por defecto
        if self.lst_habs.size() > 0:
            self.lst_habs.select_set(0)
            self.on_hab_select(None)
        self.redibujar()
        messagebox.showinfo("Laberinto", f"Laberinto con 2 habitaciones creado en modo {'bombas' if con_bombas else 'normal'}")

    def actualizar_lista(self):
        self.lst_habs.delete(0, tk.END)
        if not self.laberinto:
            self.lbl_count.config(text="Habitaciones: 0")
            return
        for hab in self.laberinto.habitaciones:
            self.lst_habs.insert(tk.END, f"Hab {hab.num}")
        self.lbl_count.config(text=f"Habitaciones: {len(self.laberinto.habitaciones)}")

    def actualizar_lista_bichos(self):
        self.lst_bichos.delete(0, tk.END)
        if not self.juego:
            return
        for idx, bicho in enumerate(getattr(self.juego, 'bichos', []), start=1):
            posicion = getattr(bicho.posicion, 'num', '?') if getattr(bicho, 'posicion', None) else '?'
            estado = 'vivo' if bicho.esta_vivo() else 'muerto'
            self.lst_bichos.insert(tk.END, f"{idx}. {bicho} | {estado} | Hab {posicion} | V:{bicho.vidas} P:{bicho.poder}")

    def actualizar_estado_juego(self):
        if not self.juego or not getattr(self.juego, 'person', None):
            self.lbl_state.config(text="Estado: sin personaje")
            return
        personaje = self.juego.person
        pos = getattr(personaje.posicion, 'num', '?') if getattr(personaje, 'posicion', None) else '?'
        self.lbl_state.config(text=f"Estado: {personaje.nombre} | V:{personaje.vidas} P:{personaje.poder} | Hab {pos}")

    def on_hab_select(self, event):
        sel = self.lst_habs.curselection()
        if not sel or not self.laberinto:
            return
        idx = sel[0]
        hab = self.laberinto.habitaciones[idx]
        self.mostrar_detalles_habitacion(hab)

    def mostrar_detalles_habitacion(self, hab):
        self.txt_detalles.delete(1.0, tk.END)
        self.txt_detalles.insert(tk.END, f"Habitacion {hab.num}\n")
        self.txt_detalles.insert(tk.END, "Orientaciones:\n")
        for o in hab.forma.orientaciones:
            try:
                elem = hab.forma.obtener_elemento(o)
            except Exception:
                elem = None
            nombre_ori = str(o)
            if elem is None:
                self.txt_detalles.insert(tk.END, f"  - {nombre_ori}: <vacio>\n")
            else:
                tipo = elem.__class__.__name__
                extra = ""
                if hasattr(elem, 'abierta'):
                    extra = f" (abierta={elem.abierta})"
                if hasattr(elem, 'activa'):
                    extra += f" (activa={elem.activa})"
                self.txt_detalles.insert(tk.END, f"  - {nombre_ori}: {tipo}{extra}\n")

        if self.juego:
            bichos_en_hab = []
            for bicho in getattr(self.juego, 'bichos', []):
                if getattr(bicho, 'posicion', None) is hab:
                    bichos_en_hab.append(f"{bicho} (V:{bicho.vidas} P:{bicho.poder})")
            if bichos_en_hab:
                self.txt_detalles.insert(tk.END, "\nBichos en la habitacion:\n")
                for texto in bichos_en_hab:
                    self.txt_detalles.insert(tk.END, f"  - {texto}\n")

    def redibujar(self):
        """Dibuja habitaciones, puertas y jugador en el canvas."""
        self.canvas.delete("all")
        self.room_items.clear()
        self.door_items.clear()
        self.bicho_items.clear()
        if not self.laberinto:
            return

        # Layout: admite hasta 4 habitaciones (1,2 o 4)
        n = len(self.laberinto.habitaciones)
        positions = {}
        if n == 1:
            positions = {self.laberinto.habitaciones[0].num: (1, 1)}
        elif n == 2:
            positions = {self.laberinto.habitaciones[0].num: (0, 0), self.laberinto.habitaciones[1].num: (0, 1)}
        else:
            # Asume 4 o más: coloca en una cuadrícula 2x2 con primeros 4
            coords = [(0, 0), (0, 1), (1, 0), (1, 1)]
            for i, hab in enumerate(self.laberinto.habitaciones[:4]):
                positions[hab.num] = coords[i]

        w = self.canvas.winfo_width() or 400
        h = self.canvas.winfo_height() or 300
        margin = 20
        cols = 2
        rows = 2
        cell_w = (w - margin * 2) / cols
        cell_h = (h - margin * 2) / rows

        # Dibujar habitaciones
        for hab in self.laberinto.habitaciones:
            pos = positions.get(hab.num, (0, 0))
            r = pos[0]
            c = pos[1]
            x1 = margin + c * cell_w + 10
            y1 = margin + r * cell_h + 10
            x2 = x1 + cell_w - 20
            y2 = y1 + cell_h - 20
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#ffffff", outline="#444")
            self.canvas.create_text((x1 + x2) / 2, y1 + 12, text=f"Hab {hab.num}")
            self.room_items[hab.num] = (rect, (x1, y1, x2, y2))

        # Dibujar puertas entre habitaciones (si las hay)
        for hab in self.laberinto.habitaciones:
            rect, bbox = self.room_items.get(hab.num, (None, None))
            if bbox is None:
                continue
            x1, y1, x2, y2 = bbox
            # Para cada orientacion, si es puerta y conecta con otra habitacion, dibujar un segmento
            for o in hab.forma.orientaciones:
                try:
                    elem = hab.forma.obtener_elemento(o)
                except Exception:
                    elem = None
                if elem is None:
                    continue
                if hasattr(elem, 'es_puerta') and elem.es_puerta():
                    # detectar la habitación opuesta
                    otro = getattr(elem, 'lado1', None) if getattr(elem, 'lado1', None) is not hab else getattr(elem, 'lado2', None)
                    if otro is None:
                        # puerta hacia afuera, dibujar en borde
                        cx = (x1 + x2) / 2
                        cy = (y1 + y2) / 2
                    else:
                        other_bbox = self.room_items.get(otro.num, (None, None))[1]
                        if other_bbox is None:
                            continue
                        ox1, oy1, ox2, oy2 = other_bbox
                        cx = ( (x1 + x2) / 2 + (ox1 + ox2) / 2 ) / 2
                        cy = ( (y1 + y2) / 2 + (oy1 + oy2) / 2 ) / 2
                    color = "green" if getattr(elem, 'abierta', False) else "red"
                    line = self.canvas.create_line((x1 + x2) / 2, (y1 + y2) / 2, cx, cy, fill=color, width=6)
                    # store mapping to puerta object
                    self.door_items.append((line, elem))
                    # tag for easier lookup
                    self.canvas.addtag_withtag("door", line)

        # Dibujar jugador
        if self.juego and getattr(self.juego, 'person', None) and getattr(self.juego.person, 'posicion', None):
            pos_hab = self.juego.person.posicion
            if pos_hab and pos_hab.num in self.room_items:
                _, bbox = self.room_items[pos_hab.num]
                x1, y1, x2, y2 = bbox
                px = (x1 + x2) / 2
                py = (y1 + y2) / 2
                r = 12
                self.player_item = self.canvas.create_oval(px - r, py - r, px + r, py + r, fill="#0077ff")

        # Dibujar bichos
        if self.juego:
            offsets = [(-26, -16), (26, -16), (-26, 16), (26, 16), (0, -30), (0, 30)]
            for idx, bicho in enumerate(getattr(self.juego, 'bichos', [])):
                if not getattr(bicho, 'posicion', None):
                    continue
                pos_hab = bicho.posicion
                if pos_hab and pos_hab.num in self.room_items:
                    _, bbox = self.room_items[pos_hab.num]
                    x1, y1, x2, y2 = bbox
                    px = (x1 + x2) / 2
                    py = (y1 + y2) / 2
                    ox, oy = offsets[idx % len(offsets)]
                    r = 10
                    fill = "#ff7f0e" if bicho.esta_vivo() else "#888888"
                    item = self.canvas.create_oval(px + ox - r, py + oy - r, px + ox + r, py + oy + r, fill=fill)
                    self.canvas.create_text(px + ox, py + oy - 16, text=f"{bicho.modo}")
                    self.bicho_items.append(item)

    def mover_personaje(self, direccion: str):
        """Mueve el personaje según la tecla (N/S/E/W)."""
        if not self.juego or not getattr(self.juego, 'person', None):
            return
        person = self.juego.person
        try:
            if direccion == 'N':
                from Solucion.norte import Norte
                Norte.default().caminar(person)
            elif direccion == 'S':
                from Solucion.sur import Sur
                Sur.default().caminar(person)
            elif direccion == 'E':
                from Solucion.este import Este
                Este.default().caminar(person)
            elif direccion == 'W':
                from Solucion.oeste import Oeste
                Oeste.default().caminar(person)
        except Exception as e:
            print("Movimiento falló:", e)
        # actualizar vista
        self.redibujar()
        self.actualizar_estado_juego()
        self.actualizar_lista_bichos()

    def toggle_puerta(self):
        sel = self.lst_habs.curselection()
        if not sel or not self.laberinto:
            messagebox.showwarning("Selecciona", "Selecciona una habitación primero")
            return
        idx = sel[0]
        hab = self.laberinto.habitaciones[idx]
        # Buscar primera puerta en orientaciones
        for o in hab.forma.orientaciones:
            try:
                elem = hab.forma.obtener_elemento(o)
            except Exception:
                elem = None
            if elem is None:
                continue
            if hasattr(elem, 'es_puerta') and elem.es_puerta():
                # Toggle abierta property
                estado = elem.abierta
                elem.abierta = not estado
                self.mostrar_detalles_habitacion(hab)
                return
        messagebox.showinfo("Puerta", "No se encontró una puerta en la habitación seleccionada")

    def get_puerta_en_habitacion(self, hab):
        """Devuelve la primera puerta encontrada en la habitación o None."""
        for o in hab.forma.orientaciones:
            try:
                elem = hab.forma.obtener_elemento(o)
            except Exception:
                elem = None
            if elem is None:
                continue
            if hasattr(elem, 'es_puerta') and elem.es_puerta():
                return elem
        return None

    def abrir_puerta_seleccionada(self):
        sel = self.lst_habs.curselection()
        if not sel or not self.laberinto:
            messagebox.showwarning("Selecciona", "Selecciona una habitación primero")
            return
        hab = self.laberinto.habitaciones[sel[0]]
        puerta = self.get_puerta_en_habitacion(hab)
        if puerta is None:
            messagebox.showinfo("Puerta", "No se encontró una puerta en la habitación seleccionada")
            return
        try:
            puerta.abierta = True
        except Exception:
            try:
                puerta.abrir()
            except Exception:
                pass
        self.mostrar_detalles_habitacion(hab)
        self.redibujar()

    def anadir_bicho(self, modo):
        if not self.juego or not self.laberinto:
            messagebox.showwarning("Primero crea", "Crea un laberinto antes de añadir bichos")
            return
        bicho = Bicho(modo, vidas=100, poder=20)
        bicho.juego = self.juego
        habitacion_inicial = self.laberinto.habitaciones[0] if self.laberinto.habitaciones else None
        if habitacion_inicial is not None:
            habitacion_inicial.entrar(bicho)
        self.juego.agregar_bicho(bicho)
        self.actualizar_lista_bichos()
        self.redibujar()

    def anadir_bicho_agresivo(self):
        self.anadir_bicho(Agresivo())

    def anadir_bicho_perezoso(self):
        self.anadir_bicho(Perezoso())

    def lanzar_bichos(self):
        if not self.juego:
            return
        self.juego.lanzar_todos_los_bichos()
        self.redibujar()
        self.actualizar_lista_bichos()
        self.actualizar_estado_juego()

    def activar_bombas(self):
        if not self.juego:
            return
        self.juego.activar_bombas()
        self.redibujar()

    def desactivar_bombas(self):
        if not self.juego:
            return
        self.juego.desactivar_bombas()
        self.redibujar()

    def cerrar_puerta_seleccionada(self):
        sel = self.lst_habs.curselection()
        if not sel or not self.laberinto:
            messagebox.showwarning("Selecciona", "Selecciona una habitación primero")
            return
        hab = self.laberinto.habitaciones[sel[0]]
        puerta = self.get_puerta_en_habitacion(hab)
        if puerta is None:
            messagebox.showinfo("Puerta", "No se encontró una puerta en la habitación seleccionada")
            return
        try:
            puerta.abierta = False
        except Exception:
            try:
                puerta.cerrar()
            except Exception:
                pass
        self.mostrar_detalles_habitacion(hab)
        self.redibujar()

    def on_canvas_click(self, event):
        """Detecta si se ha hecho clic en una puerta y la alterna.

        Usa varias estrategias: área de búsqueda aumentada, búsqueda del
        elemento más cercano como fallback y registro en consola para depuración.
        """
        x, y = event.x, event.y
        radius = 10
        items = self.canvas.find_overlapping(x - radius, y - radius, x + radius, y + radius)
        door_ids = [line_id for (line_id, _) in self.door_items]

        # Intento por solapamiento
        for it in items:
            if it in door_ids:
                puerta = next(p for (line, p) in self.door_items if line == it)
                try:
                    puerta.abierta = not puerta.abierta
                    print(f"Toggled puerta {puerta} -> abierta={puerta.abierta}")
                except Exception as e:
                    print("Error toggling puerta:", e)
                self.redibujar()
                sel = self.lst_habs.curselection()
                if sel:
                    self.on_hab_select(None)
                return

        # Fallback: buscar el elemento más cercano
        try:
            closest = self.canvas.find_closest(x, y)
            if closest:
                it = closest[0]
                if it in door_ids:
                    puerta = next(p for (line, p) in self.door_items if line == it)
                    try:
                        puerta.abierta = not puerta.abierta
                        print(f"Toggled puerta (closest) {puerta} -> abierta={puerta.abierta}")
                    except Exception as e:
                        print("Error toggling puerta (closest):", e)
                    self.redibujar()
                    sel = self.lst_habs.curselection()
                    if sel:
                        self.on_hab_select(None)
                    return
        except Exception:
            pass

        # Si no se encontró ninguna puerta cercana, mostrar debug
        print(f"Click en canvas en ({x},{y}) - items encontrados: {items} - puertas dibujadas: {door_ids}")


if __name__ == "__main__":
    app = LaberintoGUI()
    app.mainloop()
