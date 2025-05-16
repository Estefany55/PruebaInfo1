import math  # Importa la librería math para cálculos matemáticos

class Node:
   def __init__(self, name, x, y):
       """Constructor de la clase Node.
       Parámetros:
       name -- Nombre del nodo
       x -- Coordenada X del nodo
       y -- Coordenada Y del nodo
       """
       self.name = name  # Nombre del nodo
       self.x = float(x)  # Coordenada X o longitud
       self.y = float(y)  # Coordenada Y o latitud
       self.lon = self.x  # Alias para longitud
       self.lat = self.y  # Alias para latitud
       self.neighbors = []  # Lista de nodos vecinos


def AddNeighbor(n1, n2):
   """Añade un nodo n2 como vecino de n1 si no está ya en la lista de vecinos.

   Parámetros:
   n1 -- Nodo de origen
   n2 -- Nodo a agregar como vecino

   Retorna:
   True si el nodo fue agregado, False si ya estaba en la lista de vecinos.
   """
   if n2 in n1.neighbors:
       return False  # No se agrega porque ya es vecino
   else:
       n1.neighbors.append(n2)
       return True  # Se agrega con éxito


def Distance(n1, n2):
   """Calcula la distancia euclidiana entre dos nodos.
   Parámetros:
   n1 -- Primer nodo
   n2 -- Segundo nodo

   Retorna:
   La distancia euclidiana entre los dos nodos.
   """
   return math.sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)