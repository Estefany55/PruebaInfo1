import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
from tkinter import simpledialog, filedialog
import os
import matplotlib
matplotlib.use('TkAgg')
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
from graph import NodeToKML
from path import pathToKML
from airSpace import *
from path import *
from graph import *

A = buildAirSpace("Cat")
L = buildAirGraf(A)


def CreateGraph_1():
 G = Graph()
 AddNode(G, Node("A", 1, 20))
 AddNode(G, Node("B", 8, 17))
 AddNode(G, Node("C", 15, 20))
 AddNode(G, Node("D", 18, 15))
 AddNode(G, Node("E", 2, 4))
 AddNode(G, Node("F", 6, 5))
 AddNode(G, Node("G", 12, 12))
 AddNode(G, Node("H", 10, 3))
 AddNode(G, Node("I", 19, 1))
 AddNode(G, Node("J", 13, 5))
 AddNode(G, Node("K", 3, 15))
 AddNode(G, Node("L", 4, 10))
 AddSegment(G, "AB", "A", "B")
 AddSegment(G, "AE", "A", "E")
 AddSegment(G, "AK", "A", "K")
 AddSegment(G, "BA", "B", "A")
 AddSegment(G, "BC", "B", "C")
 AddSegment(G, "BF", "B", "F")
 AddSegment(G, "BK", "B", "K")
 AddSegment(G, "BG", "B", "G")
 AddSegment(G, "CD", "C", "D")
 AddSegment(G, "CG", "C", "G")
 AddSegment(G, "DG", "D", "G")
 AddSegment(G, "DH", "D", "H")
 AddSegment(G, "DI", "D", "I")
 AddSegment(G, "EF", "E", "F")
 AddSegment(G, "FL", "F", "L")
 AddSegment(G, "GB", "G", "B")
 AddSegment(G, "GF", "G", "F")
 AddSegment(G, "GH", "G", "H")
 AddSegment(G, "ID", "I", "D")
 AddSegment(G, "IJ", "I", "J")
 AddSegment(G, "JI", "J", "I")
 AddSegment(G, "KA", "K", "A")
 AddSegment(G, "KL", "K", "L")
 AddSegment(G, "LK", "L", "K")
 AddSegment(G, "LF", "L", "F")
 return G

def CreateGraph_2():
 G = Graph()
 AddNode(G, Node("A", 1, 20))
 AddNode(G, Node("B", 7, 17))
 AddNode(G, Node("C", 1, 20))
 AddNode(G, Node("D", 8, 15))
 AddNode(G, Node("E", 2, 4))
 AddNode(G, Node("F", 6, 5))
 AddNode(G, Node("G", 12, 12))
 AddSegment(G, "AB", "A", "B")
 AddSegment(G, "AE", "A", "E")
 AddSegment(G, "AK", "A", "K")
 AddSegment(G, "BA", "B", "A")
 AddSegment(G, "BC", "B", "C")
 AddSegment(G, "BF", "B", "F")
 AddSegment(G, "BK", "B", "K")
 AddSegment(G, "FL", "F", "L")
 AddSegment(G, "GB", "G", "B")
 AddSegment(G, "GF", "G", "F")
 AddSegment(G, "GH", "G", "H")
 AddSegment(G, "ID", "I", "D")
 AddSegment(G, "IJ", "I", "J")
 AddSegment(G, "JI", "J", "I")
 AddSegment(G, "KA", "K", "A")
 AddSegment(G, "KL", "K", "L")
 AddSegment(G, "LK", "L", "K")
 AddSegment(G, "LF", "L", "F")
 return G


# Variables globales
global G, selected_nodes, selected_node, accion_en_espera, modo_visualizacion, canvas_picture
G = None
selected_nodes = []
selected_node = None
accion_en_espera = None
modo_visualizacion = "vecinos"
canvas_picture = None
ultima_ruta = None
animacion_activa = None
boton_pausa = None
pausado = False

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# Dibuja la figura matplotlib en el panel gráfico de la interfaz Tkinter.
def draw_on_canvas(fig):
    global canvas_picture, canvas_toolbar

    # Limpia el panel gráfico de Tkinter
    for widget in picture_frame.winfo_children():
        widget.destroy()

    # Crea un canvas de Matplotlib para la figura dada
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


    # Inserta el widget en el grid de Tk
    toolbar_frame = tk.Frame(picture_frame)
    toolbar_frame.grid(row=1, column=0, sticky="ew")

    # Crear toolbar y ponerlo en toolbar_frame
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()

    # Guardar referencias
    canvas_picture = canvas_widget
    canvas_toolbar = toolbar

    fig.canvas.mpl_connect('button_press_event', on_click)



# Función al hacer clic en un nodo
# Maneja los clics del usuario sobre el gráfico y ejecuta la acción correspondiente (vecinos, alcanzables, camino).
def on_click(event: MouseEvent):
  global selected_nodes, accion_en_espera, G
  # Ignora clics fuera del área del gráfico o sin grafo cargado
  if G is None or not event.inaxes:
      return

  # Obtiene coordenadas del clic
  x, y = event.xdata, event.ydata

  # Busca el nodo más cercano a esas coordenadas
  node = GetClosest(G, x, y)
  if node is None:
      return

  # Modo “vecinos”: resalta solo vecinos del nodo clicado
  if accion_en_espera == "vecinos":
      selected_nodes[:] = [node]
      fig, ax = plt.subplots()
      draw_on_canvas(fig)
      for n in G.nodes:
          color = 'blue' if n == node else ('green' if n in node.neighbors else 'gray')
          plt.plot(n.x, n.y, 'o', color=color)
          plt.text(n.x, n.y, n.name, fontsize=9)
      for neighbor in node.neighbors:
          plt.plot([node.x, neighbor.x], [node.y, neighbor.y], 'r--')
      plt.title(f"Vecinos de {node.name}")
      plt.grid()
      accion_en_espera = None

  # Modo “alcanzables”: pinta todos los nodos accesibles desde el nodo
  elif accion_en_espera == "alcanzables":
      selected_nodes[:] = [node]
      visited = set()
      to_visit = [node]
      while to_visit:
          current = to_visit.pop()
          if current not in visited:
              visited.add(current)
              to_visit.extend(current.neighbors)
      fig, ax = plt.subplots()
      draw_on_canvas(fig)
      for n in G.nodes:
          color = 'green' if n in visited else 'gray'
          plt.plot(n.x, n.y, 'o', color=color)
          plt.text(n.x, n.y, n.name, fontsize=8)
      plt.title(f"Nodos alcanzables desde {node.name}")
      plt.grid()
      accion_en_espera = None

  # Modo “camino”: tras dos clics, busca y dibuja la ruta más corta
  elif accion_en_espera == "camino":
      selected_nodes.append(node)
      if len(selected_nodes) == 2:
          origin, destination = selected_nodes[0].name, selected_nodes[1].name
          path = FindShortestPath(G, origin, destination)
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          if path:
              PlotPath(G, path)
              print("Camino encontrado:", [n.name for n in path.nodes])
              global ultima_ruta
              ultima_ruta = path
          else:
              print("No se encontró camino.")
          selected_nodes.clear()
          accion_en_espera = None




# Activar modo al pulsar botón
# Establece el modo de acción que se ejecutará al hacer clic sobre los nodos del grafo.
def set_accion(modo):
  global accion_en_espera, selected_nodes
  accion_en_espera = modo
  selected_nodes.clear()
  # Mensaje guiando al usuario
  if modo == "camino":
      print("Modo activo: camino más corto. Haz clic sobre dos nodos.")
  elif modo == "vecinos":
      print("Modo activo: vecinos. Haz clic sobre un nodo.")
  elif modo == "alcanzables":
      print("Modo activo: alcanzables. Haz clic sobre un nodo.")

#LUPA
# Activa la herramienta de zoom del gráfico si se ha cargado alguno.
def activate_zoom_mode():
    if hasattr(picture_frame, "canvas") and hasattr(picture_frame, "toolbar"):
        toolbar = picture_frame.toolbar
        toolbar.zoom()
        print("Zoom mode activated.")
    else:
        print("No graph loaded yet.")



# Funciones de carga y edición de grafos
def load_real_airspace_cat():
  global G
  air = buildAirSpace("Cat")
  G = buildAirGraf(air)
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Espacio aéreo real cargado.")

def load_real_airspace_esp():
  global G
  air = buildAirSpace("Spain")
  G = buildAirGraf(air)
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Espacio aéreo real cargado.")

def load_real_airspace_eu():
  global G
  air = buildAirSpace("ECAC")
  G = buildAirGraf(air)
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Espacio aéreo real cargado.")

# Carga un grafo de ejemplo predefinido para mostrar en la interfaz.
def show_example_graph():
  global G
  G = CreateGraph_1()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Grafo de ejemplo cargado.")


# Carga un grafo de ejemplo predefinido para mostrar en la interfaz.
def show_custom_graph():
  global G
  G = CreateGraph_2()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Grafo inventado cargado.")


# Permite al usuario cargar un grafo desde un archivo de texto.
def load_graph_from_file():
  global G
  file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
  if file_path:
      G = LoadGraphFromFile(file_path)
      if G:
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          Plot(G)
          print(f"Grafo cargado desde: {file_path}")

# Solicita datos al usuario para añadir un nuevo nodo al grafo actual.
def add_node():
  global G
  if G is None:
      return
  name = simpledialog.askstring("Añadir nodo", "Nombre:")
  x = simpledialog.askfloat("Añadir nodo", "X:")
  y = simpledialog.askfloat("Añadir nodo", "Y:")
  if name and x is not None and y is not None:
      node = Node(name, x, y)
      if AddNode(G, node):
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          Plot(G)

# Añade una conexión entre dos nodos existentes si ambos están presentes.
def add_segment():
  global G
  if G is None:
      print("Crea o carga primero un grafo.")
      return
  origin = simpledialog.askstring("Añadir segmento", "Nombre del nodo origen:")
  destination = simpledialog.askstring("Añadir segmento", "Nombre del nodo destino:")




  if origin and destination:
      name = origin + destination
      if AddSegment(G, name, origin, destination):
          print(f"Segmento {name} añadido correctamente.")
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          Plot(G)
          fig.canvas.mpl_connect('button_press_event', on_click)
      else:
          print("Error: uno o ambos nodos no existen.")



# Elimina un nodo especificado por el usuario del grafo actual.
def delete_node():
  global G
  if G is None:
      print("Crea o carga primero un grafo.")
      return

  name = simpledialog.askstring("Eliminar nodo", "Nombre del nodo a eliminar:")
  if name:
      if DeleteNode(G, name):
          print(f"Nodo {name} eliminado correctamente.")
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          Plot(G)
          fig.canvas.mpl_connect('button_press_event', on_click)
      else:
          print(f"El nodo {name} no existe.")

# Elimina un segmento especificado por el usuario del grafo actual.
def delete_segment():
  global G
  if G is None:
      print("Crea o carga primero un grafo.")
      return

  name = simpledialog.askstring("Eliminar segmento", "Nombre del segmento (ej. AB):")
  if name:
      if DeleteSegment(G, name):
          print(f"Segmento {name} eliminado correctamente.")
          fig, ax = plt.subplots()
          draw_on_canvas(fig)
          Plot(G)
          fig.canvas.mpl_connect('button_press_event', on_click)
      else:
          print(f"El segmento {name} no existe.")

# Crea un grafo vacío listo para editar desde la interfaz.
def create_empty_graph():
  global G
  G = Graph()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  print("Nuevo grafo vacío creado.")


#version4
"""def generate_kml():
    try:
        name1 = simpledialog.askstring("Nodo 1", "Dime el nodo 1 (en mayúscula):")
        name2 = simpledialog.askstring("Nodo 2", "Dime el nodo 2 (en mayúscula):")

        if not name1 or not name2:
            messagebox.showwarning("Entrada inválida", "Debes introducir ambos nodos.")
            return

        # L = your graph object (should be globally accessible or passed in)
        NodeToKML(L, name1, name2, 'node.kml')

        name3 = simpledialog.askstring("Ruta nodo 1", "Dime el nodo INICIAL para la ruta (en mayúscula):")
        name4 = simpledialog.askstring("Ruta nodo 2", "Dime el nodo FINAL para la ruta (en mayúscula):")

        if not name3 or not name4:
            messagebox.showwarning("Entrada inválida", "Debes introducir ambos nodos para la ruta.")
            return

        path = FindShortestPath(L, name3, name4)  # Make sure this function is available
        if path:
            pathToKML(path, "path.kml")
            messagebox.showinfo("Éxito", "Archivos KML generados con éxito: node.kml y path.kml")
        else:
            messagebox.showerror("Error", f"No se encontró una ruta entre {name3} y {name4}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


def open_in_google_earth():
    try:
        # Path to the generated KML files
        node_kml = os.path.abspath("node.kml")
        path_kml = os.path.abspath("path.kml")

        # Check if files exist
        if not os.path.exists(node_kml) or not os.path.exists(path_kml):
            messagebox.showwarning("Advertencia", "Primero genera los archivos KML.")
            return

        # Open both in default KML viewer (usually Google Earth)
        os.startfile(node_kml)
        os.startfile(path_kml)

        # Optional: Inform the user
        messagebox.showinfo("Abierto", "Los archivos se han abierto en Google Earth.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir Google Earth: {str(e)}")

"""
# Genera archivos KML con nodos y rutas para visualización en Google Earth.
def generar_y_abrir_kml():
    try:
        # Introducir nodos
        nodo1 = simpledialog.askstring("Entrada", "Dime el nodo 1 para marcar en KML (en mayúsculas):")
        nodo2 = simpledialog.askstring("Entrada", "Dime el nodo 2 para marcar en KML (en mayúsculas):")
        # Si alguno de los dos nodos no fue ingresado, muestra advertencia y sale de la función
        if not nodo1 or not nodo2:
            messagebox.showwarning("Cancelado", "No se ingresaron nodos.")
            return

        # Genera el archivo 'node.kml' con los puntos de los dos nodos indicados
        NodeToKML(L, nodo1, nodo2, 'node.kml')
        # Busca el camino más corto entre los dos nodos
        path = FindShortestPath(L, nodo1, nodo2)
        if not path:
            messagebox.showerror("Error", f"No se encontró un camino entre {nodo1} y {nodo2}.")
            return
        # Genera el archivo 'path.kml' con la ruta del camino más corto
        pathToKML(path, 'path.kml')

        # Abre el archivo 'node.kml' en la aplicación asociada (Google Earth si está configurado)
        os.startfile(os.path.abspath("node.kml"))
        # Abre el archivo 'path.kml' también
        os.startfile(os.path.abspath("path.kml"))

        # Muestra mensaje informando que todo fue exitoso
        messagebox.showinfo("Éxito", "Archivos KML generados y abiertos en Google Earth.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Guarda el grafo actual en un archivo de texto.
def save_graph_to_file():
    global G
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        save_to_file(G, file_path)  # ✅ CORRECTO: llamamos la función externa, no un método de la clase
        print(f"Grafo guardado en: {file_path}")

# Extrae listas de coordenadas X e Y de una ruta para graficar o simular.
def extraer_coordenadas_de_ruta(ruta):
    xs = [n.x for n in ruta]  # o n.longitude si estás en versión con datos reales
    ys = [n.y for n in ruta]
    return xs, ys


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import linspace, concatenate

# Anima el vuelo de un avión sobre la ruta más corta usando matplotlib.
def simular_vuelo(ruta, velocidad_kmh=900):

    from numpy import linspace, concatenate
    global canvas_picture

    # Prepara lista de puntos X e Y según la ruta dada
    ruta = ruta.nodes if hasattr(ruta, 'nodes') else ruta
    if not ruta or len(ruta) < 2:
        print("Ruta no válida")
        return

    xs, ys = extraer_coordenadas_de_ruta(ruta)

    # Dibuja la línea de ruta y crea el marcador del avión
    fig, ax = plt.subplots()
    ax.plot(xs, ys, 'bo-', label='Ruta')
    avion, = ax.plot([], [], 'ro', label='Avión')
    ax.set_title("Simulación de vuelo")
    ax.grid(True)
    ax.legend()

    # Mostrar la figura en el canvas de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()

    if canvas_picture:
        canvas_picture.destroy()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    # Genera puntos intermedios para animar suavemente
    puntos_x = concatenate([linspace(xs[i], xs[i + 1], 20) for i in range(len(xs) - 1)])
    puntos_y = concatenate([linspace(ys[i], ys[i + 1], 20) for i in range(len(ys) - 1)])


    # Animación del avión
    def init():
        avion.set_data([], [])
        return avion,

    def update(frame):
        avion.set_data([puntos_x[frame]], [puntos_y[frame]])
        return avion,

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(puntos_x),
        init_func=init,
        interval=100,
        blit=False,  # 👈 CAMBIA ESTO A False
        repeat=False
    )

    def actualizar_canvas():
        canvas.draw()
        canvas._tkcanvas.after(100, actualizar_canvas)

    actualizar_canvas()

    # --- Botón de pausa/reanudar ---
    def pausar_reanudar():
        global pausado
        if pausado:
            ani.event_source.start()
            boton_pausa.config(text="⏸️ Pausar")
        else:
            ani.event_source.stop()
            boton_pausa.config(text="▶️ Reanudar")
        pausado = not pausado

    # Si ya existe el botón de pausa, destrúyelo
    global boton_pausa
    if boton_pausa:
        boton_pausa.destroy()

    # Crear nuevo botón solo durante la simulación
    boton_pausa = tk.Button(picture_frame, text="⏸️ Pausar", command=pausar_reanudar)
    boton_pausa.grid(row=1, column=0, pady=5)

# Dispara la simulación de vuelo desde la interfaz si existe una ruta.
def simular_vuelo_desde_gui():
    global ultima_ruta
    print("Botón 'Simular vuelo' pulsado")

    if ultima_ruta:
        print("Simulando vuelo con ruta guardada...")
        simular_vuelo(ultima_ruta)
    else:
        print("Selecciona dos nodos primero y genera un camino con el botón 'Camino más corto'.")

# Colorea nodos del grafo según la provincia de Catalunya donde se encuentren.
def colorear_por_provincia():
   global G
   if G is None:
       print("Carga primero un grafo.")
       return

   provincia_colores = {
       "Tarragona": "red",
       "Lleida": "orange",
       "Barcelona": "blue",
       "Girona": "green"
   }

   def detectar_provincia(nodo):
       lat = nodo.y
       lon = nodo.x

       if lat < 41.3 and lon < 1.6:
           return "Tarragona"
       elif lon < 1.4:
           return "Lleida"
       elif lon > 2.4 and lat > 41.6:
           return "Girona"
       else:
           return "Barcelona"

   fig, ax = plt.subplots()
   draw_on_canvas(fig)

   leyenda = {}

   for nodo in G.nodes:
       provincia = detectar_provincia(nodo)
       color = provincia_colores[provincia]
       punto = plt.plot(nodo.x, nodo.y, 'o', color=color, label=provincia)
       leyenda[provincia] = punto[0]
       plt.text(nodo.x, nodo.y, nodo.name, fontsize=7)


   handles = [leyenda[p] for p in provincia_colores if p in leyenda]
   labels = [p for p in provincia_colores if p in leyenda]
   plt.legend(handles, labels, title="Provincia")
   plt.title("Nodos coloreados por provincia")
   plt.grid()

# Muestra una lista de funcionalidades implementadas adicionales.
def load_list():
    messagebox.showinfo("Lista","\n·Colorear la interfaz \n ·Simular vuelo a partir de una ruta \n ·Abrir des de la interfaz el Google Earth \n ·Colorear por provincias de CAT \n ·Foto grupal")


from PIL import Image, ImageTk

# Muestra una imagen grupal con nombres del equipo.
def load_photo():
    global canvas_picture  # reutilizamos la variable para limpiar el frame

    # Limpiar el frame donde está el gráfico
    for widget in picture_frame.winfo_children():
        widget.destroy()

    # Cargar y redimensionar la imagen
    try:
        imagen_original = Image.open("grupo.jpeg")
        imagen_redimensionada = imagen_original.resize((1000, 800), Image.Resampling.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Mostrar en un Label dentro del picture_frame
        label_imagen = tk.Label(picture_frame, image=imagen_tk)
        label_imagen.image = imagen_tk  # Guardar referencia para evitar que se borre
        label_imagen.grid(row=0, column=0, padx=5, pady=5)

        canvas_picture = label_imagen  # Actualizar referencia

        messagebox.showinfo("Integrantes del Grupo",
                            "Estefany Martinez Diaz\n Roger Zaragoza Rius \n Núria Gemma Berenguer Castellón \n Diana María Diaconu Cotoara")

    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'grupo.png' en la carpeta del proyecto.")



# Interfaz

azul_fondo = "#bad4e0"
root = tk.Tk()
root.geometry('1300x900')
root.title('Espacio aéreo')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, columnspan=2, pady=5)

button_frame = tk.LabelFrame(root, text='Opciones')
button_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

picture_frame = tk.LabelFrame(root, text='Gráfico')
picture_frame.grid(row=1, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")
picture_frame.rowconfigure(0, weight=1)
picture_frame.columnconfigure(0, weight=1)


# Botones de modo
btn_vecinos = tk.Button(top_frame, text="Vecinos", command=lambda: set_accion("vecinos"))
btn_vecinos.pack(side="left", padx=5)

btn_alcanzables = tk.Button(top_frame, text="Alcanzables", command=lambda: set_accion("alcanzables"))
btn_alcanzables.pack(side="left", padx=5)

btn_camino = tk.Button(top_frame, text="Camino más corto", command=lambda: set_accion("camino"))
btn_camino.pack(side="left", padx=5)



# Botones de acciones
buttons = [
  ("Espacio aéreo real Catalunya", load_real_airspace_cat),
  ("Espacio aéreo real España", load_real_airspace_esp),
  ("Espacio aéreo real Europa", load_real_airspace_eu),
  ("Grafo de ejemplo", show_example_graph),
  ("Grafo inventado", show_custom_graph),
  ("Cargar desde archivo", load_graph_from_file),
  ("Añadir nodo", add_node),
  ("Añadir segmento", add_segment),
  ("Eliminar nodo", delete_node),
  ("Eliminar segmento", delete_segment),
  ("Crear grafo en blanco", create_empty_graph),
  ("Guardar grafo", save_graph_to_file),
  ("General y abrir KML", generar_y_abrir_kml),
  ("Colorear por provincia Cat", colorear_por_provincia),
  ("Foto grupal", load_photo),
  ("Lista de funciones extras", load_list)

]

"""""("Generear KML", generate_kml),
("Abrir Google Earth", open_in_google_earth)"""

tk.Button(button_frame, text="Simular vuelo", command=simular_vuelo_desde_gui).grid(row=len(buttons), column=0, sticky="nsew", padx=5, pady=5)


for i, (label, command) in enumerate(buttons):
  button_frame.rowconfigure(i,weight=3)
  tk.Button(button_frame, text=label, command=command).grid(row=i, column=0, sticky="nsew", padx=5, pady=5)


root.configure(bg=azul_fondo)
top_frame.configure(bg=azul_fondo)
button_frame.configure(bg=azul_fondo)
picture_frame.configure(bg=azul_fondo)


# Recolorear botones de modo
btn_vecinos.configure(bg=azul_fondo)
btn_alcanzables.configure(bg=azul_fondo)
btn_camino.configure(bg=azul_fondo)


# Recolorear todos los botones de acciones dentro de button_frame
for child in button_frame.winfo_children():
    if isinstance(child, tk.Button):
        child.configure(bg=azul_fondo)

root.mainloop()