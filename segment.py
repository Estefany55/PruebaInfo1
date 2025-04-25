# Importa todas las clases y funciones del archivo node.py
from node import *

# Define la clase Segment, que representa un segmento (arista) entre dos nodos en un grafo.
class Segment():
 def __init__(self, n1, n2):
   """Constructor de la clase Segment.
   Parámetros:
   n1 -- Nodo de origen del segmento
   n2 -- Nodo de destino del segmento
   """

   self.origin_node = n1  # Almacena el nodo de origen
   self.destination_node = n2  # Almacena el nodo de destino
   self.cost = Distance(n1, n2)  # Calcula y almacena la distancia entre los nodos como costo del segmento