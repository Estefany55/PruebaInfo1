import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
from tkinter import simpledialog, filedialog
import os


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




from graph import *
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


from airSpace import *
from graph import *
from path import *




# Variables globales
global G, selected_nodes, selected_node, accion_en_espera, modo_visualizacion, canvas_picture
G = None
selected_nodes = []
selected_node = None
accion_en_espera = None
modo_visualizacion = "vecinos"
canvas_picture = None




# Función para actualizar el canvas
def draw_on_canvas(fig):
  global canvas_picture
  canvas = FigureCanvasTkAgg(fig, master=picture_frame)
  canvas.draw()




  if canvas_picture:
      canvas_picture.destroy()




  canvas_picture = canvas.get_tk_widget()
  canvas_picture.config(width=600, height=400)
  canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")




  fig.canvas.mpl_connect('button_press_event', on_click)




# Función al hacer clic en un nodo
def on_click(event: MouseEvent):
  global selected_nodes, accion_en_espera, G
  if G is None or not event.inaxes:
      return




  x, y = event.xdata, event.ydata
  node = GetClosest(G, x, y)
  if node is None:
      return




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
          else:
              print("No se encontró camino.")
          selected_nodes.clear()
          accion_en_espera = None




# Activar modo al pulsar botón
def set_accion(modo):
  global accion_en_espera, selected_nodes
  accion_en_espera = modo
  selected_nodes.clear()
  if modo == "camino":
      print("Modo activo: camino más corto. Haz clic sobre dos nodos.")
  elif modo == "vecinos":
      print("Modo activo: vecinos. Haz clic sobre un nodo.")
  elif modo == "alcanzables":
      print("Modo activo: alcanzables. Haz clic sobre un nodo.")




# Funciones de carga y edición de grafos
def load_real_airspace():
  global G
  air = buildAirSpace("Cat")
  G = buildAirGraf(air)
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Espacio aéreo real cargado.")




def show_example_graph():
  global G
  G = CreateGraph_1()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Grafo de ejemplo cargado.")




def show_custom_graph():
  global G
  G = CreateGraph_2()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  Plot(G)
  print("Grafo inventado cargado.")




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




def create_empty_graph():
  global G
  G = Graph()
  fig, ax = plt.subplots()
  draw_on_canvas(fig)
  print("Nuevo grafo vacío creado.")




def save_graph_to_file():
  global G
  file_path = filedialog.asksaveasfilename(defaultextension=".txt")
  if file_path:
      G.save_to_file(file_path)
      print(f"Grafo guardado en: {file_path}")












# Interfaz
root = tk.Tk()
root.geometry('1100x600')
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
  ("Espacio aéreo real", load_real_airspace),
  ("Grafo de ejemplo", show_example_graph),
  ("Grafo inventado", show_custom_graph),
  ("Cargar desde archivo", load_graph_from_file),
  ("Añadir nodo", add_node),
  ("Añadir segmento", add_segment),
  ("Eliminar nodo", delete_node),
  ("Eliminar segmento", delete_segment),
  ("Crear grafo en blanco", create_empty_graph),
  ("Guardar grafo", save_graph_to_file)
]

for i, (label, command) in enumerate(buttons):
  button_frame.rowconfigure(i,weight=3)
  tk.Button(button_frame, text=label, command=command).grid(row=i, column=0, sticky="nsew", padx=5, pady=5)

root.mainloop()