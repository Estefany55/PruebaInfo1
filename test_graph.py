from graph import *

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






print("Probando el grafo...")
G = CreateGraph_1()
Plot(G)
PlotNode(G, "C")
n = GetClosest(G, 15, 5)
print(n.name)  # La respuesta debe ser J
n = GetClosest(G, 8, 19)
print(n.name)  # La respuesta debe ser B




def CreateGraph_2():
   G = Graph()
   AddNode(G, Node("A", 1, 20))
   AddNode(G, Node("B", 7, 17))
   AddNode(G, Node("C", 1, 20))
   AddNode(G, Node("D", 8, 15))
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




print("Probando el grafo...")
G = CreateGraph_2()
Plot(G)
PlotNode(G, "B")




print("Testing LoadGraphFromFile...")


G = LoadGraphFromFile("graph_data")
Plot(G)


from graph import *  # Importamos las funciones del grafo


# Crear un nuevo grafo
G = Graph()


# Agregar nodos
print("Agregando nodos...")
AddNode(G, Node("Z", 0, 0))
AddNode(G, Node("Y", 3, 4))
AddNode(G, Node("H", 6, 8))
AddNode(G, Node("V", 1, 0))
AddNode(G, Node("N", 1, 4))
AddNode(G, Node("K", 1, 8))
print(f"Nodos en el grafo: {[node.name for node in G.nodes]}")


# Agregar segmentos
print("Agregando segmentos...")
AddSegment(G, "YH", "Y", "H")
AddSegment(G, "ZY", "Z", "Y")
AddSegment(G, "KN", "K", "N")
AddSegment(G, "ZK", "Z", "K")
AddSegment(G, "KV", "K", "V")
AddSegment(G, "VY", "V", "Y")
print(f"Segmentos en el grafo: {[(seg.origin_node.name, seg.destination_node.name) for seg in G.segments]}")


# Graficar el grafo inicial
Plot(G)


# Eliminar un nodo y verificar
print("Eliminando nodo Y...")
delete_node(G, "Y")  # Función que debes haber implementado en graph.py
print(f"Nodos después de eliminar Y: {[node.name for node in G.nodes]}")
print(f"Segmentos después de eliminar Y: {[(seg.origin_node.name, seg.destination_node.name) for seg in G.segments]}")


# Graficar después de eliminar nodo
Plot(G)
# Guardar el grafo en un archivo
file_path = "graph_data1"
print(f"Guardando grafo en {file_path}...")
save_to_file(G, file_path)


# Cargar el grafo desde el archivo
# Graficar el grafo cargado
G = LoadGraphFromFile("graph_data1")
Plot(G)

#VERSION 2

G = Graph()
AddNode(G, Node("A", 0, 0))
AddNode(G, Node("B", 2, 2))
AddNode(G, Node("C", 4, 0))
AddNode(G, Node("D", 1, 0))
AddNode(G, Node("E", 1, 2))
AddNode(G, Node("F", 1, 3))
AddNode(G, Node("Z", 8, 0))
AddNode(G, Node("Y", 3, 4))
AddNode(G, Node("H", 6, 8))
AddNode(G, Node("V", 1, 9))
AddNode(G, Node("N", 1, 4))
AddNode(G, Node("K", 1, 8))
AddSegment(G, "AB", "A", "B")
AddSegment(G, "BC", "B", "C")
AddSegment(G, "AC", "A", "C")
AddSegment(G, "DF", "D", "F")
AddSegment(G, "FA", "F", "A")
AddSegment(G, "BE", "B", "E")
AddSegment(G, "YH", "Y", "H")
AddSegment(G, "ZY", "Z", "Y")
AddSegment(G, "KN", "K", "N")
AddSegment(G, "ZK", "Z", "K")
AddSegment(G, "KV", "K", "V")
AddSegment(G, "VY", "V", "Y")


path = FindShortestPath(G, "A", "B")
if path:
   print("Path found:", [n.name for n in path.nodes])
   print("Total cost:", path.cost)
   PlotPath(G, path)
else:
   print("No path found.")
