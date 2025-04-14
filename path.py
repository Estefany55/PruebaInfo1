from node import Distance
import matplotlib.pyplot as plt


class Path:
   def __init__(self):
       self.nodes = []  # Lista de nodos en el camino
       self.cost = 0.0   # Coste total del camino

def AddNodeToPath(path, node):
   if path.nodes:
       path.cost += Distance(path.nodes[-1], node)
   path.nodes.append(node)


def ContainsNode(path, node):
   return node in path.nodes


def CostToNode(path, node):
   if node not in path.nodes:
       return -1
   cost = 0
   for i in range(1, path.nodes.index(node)+1):
       cost += Distance(path.nodes[i-1], path.nodes[i])
   return cost


def PlotPath(graph, path):
   if len(path.nodes) < 2:
       print("Path too short to plot.")
       return
   for i in range(len(path.nodes) - 1):
       n1 = path.nodes[i]
       n2 = path.nodes[i+1]
       plt.plot([n1.x, n2.x], [n1.y, n2.y], color='red', linewidth=2)
       mid_x = (n1.x + n2.x) / 2
       mid_y = (n1.y + n2.y) / 2
       plt.text(mid_x, mid_y, round(Distance(n1, n2), 2), fontsize=9, color='darkred')


   for node in graph.nodes:
       color = 'green' if node in path.nodes else 'gray'
       plt.plot(node.x, node.y, 'o', color=color)
       plt.text(node.x, node.y, node.name, fontsize=9, verticalalignment='bottom')


   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title('Path in Graph')
   plt.grid()
   plt.show()
