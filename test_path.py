from node import Node
from path import *
from graph import *
from node import Node
from path import *
from graph import*
# Crear algunos nodos
n1 = Node("A", 0, 0)
n2 = Node("B", 3, 4)
n3 = Node("C", 6, 7)


# Crear un camino
p = Path()
print("Path inicial:", p)


# Agregar nodos al camino
AddNodeToPath(p, n1)
AddNodeToPath(p, n2)
AddNodeToPath(p, n3)
print("Path tras agregar nodos:", p)


# Verificar si contiene nodos
print("Contiene B?", ContainsNode(p, n2))  # True
print("Contiene D?", ContainsNode(p, Node("D", 1, 1)))  # False


# Verificar coste hasta un nodo
print("Coste hasta B:", CostToNode(p, n2))  # Debe ser 5.0
print("Coste hasta C:", CostToNode(p, n3))  # Debe ser 10.0
print("Coste hasta D:", CostToNode(p, Node("D", 1, 1)))  # -1

G = Graph()


a = PlotPath(G,p)
print(a)