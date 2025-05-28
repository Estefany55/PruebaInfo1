from segment import Segment
import matplotlib.pyplot as plt
import math
from node import *
from path import *

class Graph:
  def __init__(self):
      """Constructor de la clase Graph.




      Inicializa listas vacías para almacenar nodos y segmentos.
      """
      self.nodes = []  # Lista de nodos en el grafo
      self.segments = []  # Lista de segmentos (aristas) en el grafo


# Función para agregar un nodo al grafo
def AddNode(g, n):
  """Añade un nodo al grafo si no está ya en la lista.




  Parámetros:
  g -- Objeto de la clase Graph
  n -- Nodo a agregar




  Retorna:
  True si se agregó correctamente, False si el nodo ya existía.
  """
  if n in g.nodes:
      return False  # No se agrega porque ya está en la lista
  else:
      g.nodes.append(n)  # Se agrega a la lista de nodos
      return True  # Nodo agregado correctamente








# Función para agregar un segmento entre dos nodos del grafo
def AddSegment(g, a, name1, name2):
  """Añade un segmento entre dos nodos si ambos existen en el grafo.




  Parámetros:
  g -- Objeto de la clase Graph
  name1 -- Nombre del nodo de origen
  name2 -- Nombre del nodo de destino




  Retorna:
  True si se agregó correctamente, False si algún nodo no existe.
  """
  n1 = n2 = None  # Inicializa las variables para buscar los nodos




  # Busca los nodos por nombre en la lista de nodos del grafo
  for n in g.nodes:
      if n.name == name1:
          n1 = n
      if n.name == name2:
          n2 = n




  # Si no se encontraron ambos nodos, no se puede agregar el segmento
  if n1 is None or n2 is None:
      return False
  else:
      s = Segment(n1, n2)  # Crea un nuevo segmento entre los nodos
      g.segments.append(s)  # Agrega el segmento a la lista de segmentos del grafo
      n1.neighbors.append(n2)  # Agrega el nodo destino como vecino del origen
      return True  # Segmento agregado correctamente








# Función para encontrar el nodo más cercano a una coordenada (x, y)
def GetClosest(self, x, y):
  """Encuentra el nodo más cercano a una posición (x, y).




  Parámetros:
  x -- Coordenada X
  y -- Coordenada Y




  Retorna:
  El nodo más cercano o None si no hay nodos en el grafo.
  """
  if not self.nodes:
      return None  # Retorna None si no hay nodos
  return min(self.nodes, key=lambda node: math.sqrt((node.x - x) ** 2 + (node.y - y) ** 2))








# Función para graficar el grafo
def Plot(g):
  """Dibuja el grafo mostrando nodos y segmentos.




  Parámetros:
  g -- Objeto de la clase Graph
  """
  for segment in g.segments:
      # Dibuja las líneas que representan los segmentos
      plt.plot([segment.origin_node.x, segment.destination_node.x],
               [segment.origin_node.y, segment.destination_node.y], 'blue')




      # Calcula el punto medio del segmento para mostrar el costo
      midpoint_x = (segment.origin_node.x + segment.destination_node.x) / 2
      midpoint_y = (segment.origin_node.y + segment.destination_node.y) / 2




      # Muestra el costo del segmento en el punto medio
      plt.text(midpoint_x, midpoint_y, round(segment.cost, 2))




      # Dibuja una flecha en el segmento para indicar dirección
      plt.arrow(segment.origin_node.x, segment.origin_node.y,
                segment.destination_node.x - segment.origin_node.x,
                segment.destination_node.y - segment.origin_node.y,
                head_width=0.1, head_length=0.1, fc='blue', ec='blue', length_includes_head=True)




  # Dibuja los nodos del grafo
  for node in g.nodes:
      plt.plot(node.x, node.y, marker='o', linestyle='', color='black', markersize=5)
      plt.text(node.x, node.y, node.name, horizontalalignment='left', verticalalignment='bottom', color='red',
               fontsize=7)




  # Etiquetas y título del gráfico
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title("Graph with nodes and segments")
  plt.grid()
# Muestra el gráfico








# Función para graficar un nodo y sus vecinos
"""
def PlotNode(g, name):
  """"""Dibuja el grafo resaltando un nodo específico y sus vecinos con flechas.




  Parámetros:
  g -- Objeto de la clase Graph
  name -- Nombre del nodo a resaltar
  """"""
  target_node = None  # Variable para almacenar el nodo buscado




  # Busca el nodo por nombre en la lista de nodos del grafo
  for node in g.nodes:
      if node.name == name:
          target_node = node
          break  # Termina la búsqueda una vez encontrado




  # Si el nodo no existe, muestra un mensaje y termina la función
  if target_node is None:
      print(f"Node '{name}' does not exist in the graph.")
      return




  plt.figure()  # Crea una nueva figura para la gráfica




  # Dibuja todos los nodos en color negro
  for node in g.nodes:
      plt.plot(node.x, node.y, marker='o', linestyle='', color='black', markersize=5)
      plt.text(node.x, node.y, node.name, horizontalalignment='left', verticalalignment='bottom', color='red')




  # Dibuja los segmentos con flechas entre el nodo objetivo y sus vecinos
  for neighbor in target_node.neighbors:
      for segment in g.segments:
          if (segment.origin_node == target_node and segment.destination_node == neighbor) or \
                  (segment.origin_node == neighbor and segment.destination_node == target_node):
              # Dibuja el segmento con flecha
              plt.arrow(segment.origin_node.x, segment.origin_node.y,
                        segment.destination_node.x - segment.origin_node.x,
                        segment.destination_node.y - segment.origin_node.y,
                        head_width=0.4, head_length=0.4, fc='blue', ec='blue', length_includes_head=True)




              # Calcula el punto medio del segmento para mostrar el costo
              midpoint_x = (segment.origin_node.x + segment.destination_node.x) / 2
              midpoint_y = (segment.origin_node.y + segment.destination_node.y) / 2
              plt.text(midpoint_x, midpoint_y, round(segment.cost, 2))




  # Etiquetas y título del gráfico
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(f"Graph with nodes and segments for node '{name}'")
  plt.grid()
  plt.show()




# Muestra el gráfico




"""
def PlotNode(g, name, ax=None):
   """Dibuja el grafo resaltando un nodo específico y sus vecinos con flechas."""
   target_node = next((n for n in g.nodes if n.name == name), None)
   if target_node is None:
       print(f"Node '{name}' does not exist in the graph.")
       return


   if ax is None:
       fig, ax = plt.subplots()


   ax.clear()


   # Dibuja todos los nodos
   for node in g.nodes:
       ax.plot(node.x, node.y, marker='o', linestyle='', color='black', markersize=5)
       ax.text(node.x, node.y, node.name, ha='left', va='bottom', color='red', fontsize=7)


   # Dibuja los segmentos entre el nodo seleccionado y sus vecinos
   for neighbor in target_node.neighbors:
       for segment in g.segments:
           if (segment.origin_node == target_node and segment.destination_node == neighbor) or \
              (segment.origin_node == neighbor and segment.destination_node == target_node):
               dx = segment.destination_node.x - segment.origin_node.x
               dy = segment.destination_node.y - segment.origin_node.y
               ax.arrow(segment.origin_node.x, segment.origin_node.y, dx, dy,
                        head_width=0.1, length_includes_head=True, fc='blue', ec='blue')
               mx = (segment.origin_node.x + segment.destination_node.x) / 2
               my = (segment.origin_node.y + segment.destination_node.y) / 2
               ax.text(mx, my, round(segment.cost, 2), fontsize=8)


   ax.set_title(f"Nodo seleccionado: {target_node.name}")
   ax.set_aspect('equal', adjustable='datalim')
   ax.grid()




def LoadGraphFromFile(file_path):
  """Carga un grafo desde un archivo de texto.
  Parámetros:
  file_path -- Ruta del archivo que contiene la definición del grafo.
  Retorna:
  Un objeto Graph si la carga es exitosa, o None si hay un error.
  """
  g = Graph()  # Se crea una nueva instancia de Graph
  try:
      with open(file_path, 'r') as file:  # Abre el archivo en modo lectura
          mode = None  # Variable para determinar si se están leyendo nodos o segmentos
          for line in file:
              line = line.strip()  # Elimina espacios en blanco al inicio y al final de la línea

              if not line:  # Si la línea está vacía, se ignora
                  continue

              if line.startswith("Nodes:"):  # Si se encuentra la sección de nodos
                  mode = "nodes"
                  continue
              elif line.startswith("Segments:"):  # Si se encuentra la sección de segmentos
                  mode = "segments"
                  continue

              if mode == "nodes":  # Si estamos en la sección de nodos
                  name, x, y = line.split(',')  # Separa los valores por coma
                  AddNode(g, Node(name, float(x), float(y)))  # Crea y añade el nodo al grafo
              elif mode == "segments":  # Si estamos en la sección de segmentos
                  segment_id, origin_name, destination_name = line.split(',')  # Separa los valores por coma
                  AddSegment(g, segment_id, origin_name, destination_name)  # Crea y añade el segmento al grafo

      return g  # Retorna el grafo cargado

  except FileNotFoundError:  # Manejo de error si el archivo no se encuentra
      print(f"Error: File '{file_path}' not found.")
      return None
  except Exception as e:  # Manejo de errores generales
      print(f"Error loading graph: {e}")
      return None


def add_node(self, name, x, y):
  if any(node.name == name for node in self.nodes):
      return False
  self.nodes.append(Node(name, x, y))
  return True


def add_segment(self, name, origin_name, destination_name):
  origin = next((n for n in self.nodes if n.name == origin_name), None)
  destination = next((n for n in self.nodes if n.name == destination_name), None)
  if origin and destination:
      segment = Segment(origin, destination)
      self.segments.append(segment)
      origin.neighbors.append(destination)
      return True
  return False


def delete_node(self, name):
  self.nodes = [n for n in self.nodes if n.name != name]
  self.segments = [s for s in self.segments if s.origin_node.name != name and s.destination_node.name != name]


def save_to_file(self, filename):
  with open(filename, 'w') as f:
      f.write("Nodes:\n")
      for node in self.nodes:
          f.write(f"{node.name},{node.x},{node.y}\n")
      f.write("Segments:\n")
      for segment in self.segments:
          f.write(f"{segment.origin_node.name}{segment.destination_node.name},{segment.origin_node.name},{segment.destination_node.name}\n")


def load_from_file(cls, filename):
  graph = cls()
  with open(filename, 'r') as file:
      mode = None
      for line in file:
          line = line.strip()
          if line.startswith("Nodes:"):
              mode = "nodes"
              continue
          elif line.startswith("Segments:"):
              mode = "segments"
              continue
          if mode == "nodes":
              name, x, y = line.split(',')
              graph.add_node(name, float(x), float(y))
          elif mode == "segments":
              origin, destination = line.split(',')
              graph.add_segment(origin + destination, origin, destination)
      return graph


#VERSION 2


def FindShortestPath(G, nameOrg, nameDst):
  # Buscar nodos origen y destino
  origin = next((n for n in G.nodes if n.name == nameOrg), None)
  destination = next((n for n in G.nodes if n.name == nameDst), None)


  if origin is None or destination is None:
      print("Origen o destino no encontrado en el grafo.")
      return None


  open_paths = []  # Caminos a explorar
  best_path = None
  best_cost = float('inf')


  # Crear camino inicial
  initial_path = Path()
  AddNodeToPath(initial_path, origin)
  open_paths.append(initial_path)


  while open_paths:
      current_path = open_paths.pop(0)
      current_node = current_path.nodes[-1]


      if current_node == destination:
          total_cost = CostToNode(current_path, destination)
          if total_cost < best_cost:
              best_cost = total_cost
              best_path = current_path
          continue


      for neighbor in current_node.neighbors:
          if ContainsNode(current_path, neighbor):
              continue  # Evitar ciclos


          new_path = Path()
          for node in current_path.nodes:
              AddNodeToPath(new_path, node)
          AddNodeToPath(new_path, neighbor)


          estimated_cost = CostToNode(new_path, neighbor) + Distance(neighbor, destination)
          if estimated_cost < best_cost:
              open_paths.append(new_path)


  return best_path


#INTERFICIE 2 (DIANA)


def DeleteNode(g, name):
   node_to_remove = next((n for n in g.nodes if n.name == name), None)
   if node_to_remove is None:
       return False


   g.nodes.remove(node_to_remove)
   g.segments = [s for s in g.segments if s.origin_node != node_to_remove and s.destination_node != node_to_remove]


   # Quitar el nodo de las listas de vecinos de otros nodos
   for n in g.nodes:
       if node_to_remove in n.neighbors:
           n.neighbors.remove(node_to_remove)


   return True


def DeleteSegment(g, name):
   # Buscar segmento directo
   segment_to_remove = next((s for s in g.segments if s.origin_node.name + s.destination_node.name == name), None)


   # Si no existe, intenta con el orden inverso
   if not segment_to_remove:
       reversed_name = name[::-1]
       segment_to_remove = next((s for s in g.segments if s.origin_node.name + s.destination_node.name == reversed_name), None)


   if segment_to_remove:
       g.segments.remove(segment_to_remove)


       # Quitar también el vecino
       if segment_to_remove.destination_node in segment_to_remove.origin_node.neighbors:
           segment_to_remove.origin_node.neighbors.remove(segment_to_remove.destination_node)


       return True


   return False


def save_to_file(self, filename):
  with open(filename, 'w') as f:
      f.write("Nodes:\n")
      for node in self.nodes:
          f.write(f"{node.name},{node.x},{node.y}\n")
      f.write("Segments:\n")
      for segment in self.segments:
          f.write(f"{segment.origin_node.name}{segment.destination_node.name},{segment.origin_node.name},{segment.destination_node.name}\n")


def load_from_file(cls, filename):
  graph = cls()
  with open(filename, 'r') as file:
      mode = None
      for line in file:
          line = line.strip()
          if line.startswith("Nodes:"):
              mode = "nodes"
              continue
          elif line.startswith("Segments:"):
              mode = "segments"
              continue
          if mode == "nodes":
              name, x, y = line.split(',')
              graph.add_node(name, float(x), float(y))
          elif mode == "segments":
              origin, destination = line.split(',')
              graph.add_segment(origin + destination, origin, destination)
      return graph


#VERSION 4

def NodeToKML (g,name1,name2, nomFile):
   # Open the specified file for writing
   F = open(nomFile, 'w')
   # Write the initial KML structure and document name
   F.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n<Placemark>\n<name>' + name1 +  '</name>\n')
   target_node = None  # Variable para almacenar el nodo buscado


   # Busca el nodo por nombre en la lista de nodos del grafo
   for node in g.nodes:
       if node.name == name1:
           target_node = node
           break  # Termina la búsqueda una vez encontrado


   # Si el nodo no existe, muestra un mensaje y termina la función
   if target_node is None:
       print(f"Node '{name1}' does not exist in the graph.")
       return
   target_node1 = None
   for node in g.nodes:
       if node.name == name2:
           target_node1 = node
           break  # Termina la búsqueda una vez encontrado


   # Si el nodo no existe, muestra un mensaje y termina la función
   if target_node1 is None:
       print(f"Node '{name2}' does not exist in the graph.")
       return


   F.write('<Point>\n<coordinates>\n')
   F.write(str(target_node.x) + ',' + str(target_node.y)+'\n')
   F.write('</coordinates>\n</Point>\n</Placemark>\n<Placemark> <name>' + name2 +  '</name>\n')
   F.write('<Point>\n<coordinates>\n')
   F.write(str(target_node1.x) + ',' + str(target_node1.y)+'\n')
   # Write the closing tags for coordinates, LineString, Placemark, Document, and KML
   F.write('\n</coordinates>\n</Point>\n')
   F.write('</Placemark>\n</Document>\n</kml>')
   # Close the file
   F.close()
