import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from path import *
from graph import *

# Variables globales
selected_nodes = []
G = Graph()

# Crear nodos de ejemplo
n1 = Node("A", 0, 0)
n2 = Node("B", 2, 4)
n3 = Node("C", 6, 8)

p = Path()
print("Path inicial:", p)
AddNodeToPath(p, n1)
AddNodeToPath(p, n2)
AddNodeToPath(p, n3)

# Crear un grafo nuevo
G = Graph()

# Funciones para crear grafos
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

# Funciones de botones
def graph1():
    fig, ax = plt.subplots()
    global G
    G = CreateGraph_1()
    Plot(G)
    plt.show()

def graph2():
    fig, ax = plt.subplots()
    global G
    G = CreateGraph_2()
    Plot(G)
    plt.show()

def nodo():
    fig, ax = plt.subplots()
    global G
    G = CreateGraph_1()
    Plot(G)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

def files():
    file_path = entry.get()
    if file_path:
        fig, ax = plt.subplots()
        global G
        G = LoadGraphFromFile(file_path)
        Plot(G)
        plt.show()

def path():
    fig, ax = plt.subplots()
    PlotPath(G, p)
    plt.show()

def shortest_path():
    global selected_nodes
    if len(selected_nodes) != 2:
        print("Selecciona exactamente 2 nodos haciendo clic.")
        return
    origin = selected_nodes[0].name
    destination = selected_nodes[1].name
    fig, ax = plt.subplots()
    path = FindShortestPath(G, origin, destination)

    if path:
        print("Path found:", [n.name for n in path.nodes])
        print("Total cost:", path.cost)
        PlotPath(G, path)
    else:
        print("No path found.")
    selected_nodes.clear()
    plt.show()

def reachable():
    global selected_nodes
    if len(selected_nodes) != 1:
        print("Selecciona un único nodo.")
        return
    origin = selected_nodes[0]
    visited = set()
    to_visit = [origin]
    while to_visit:
        current = to_visit.pop()
        if current not in visited:
            visited.add(current)
            to_visit.extend(current.neighbors)
    fig, ax = plt.subplots()
    for node in G.nodes:
        color = 'green' if node in visited else 'gray'
        plt.plot(node.x, node.y, 'o', color=color)
        plt.text(node.x, node.y, node.name, fontsize=9)
    plt.title(f"Nodos alcanzables desde {origin.name}")
    plt.grid()
    plt.show()
    selected_nodes.clear()

def on_click(event: MouseEvent):
    global selected_nodes
    if event.inaxes:
        x, y = event.xdata, event.ydata
        node = GetClosest(G, x, y)
        if node and node not in selected_nodes:
            selected_nodes.append(node)
            print(f"Seleccionado: {node.name}")
            if len(selected_nodes) > 2:
                selected_nodes = selected_nodes[-2:]


root = tk.Tk()
root.geometry('800x400')
root.title('Gráficos y nodos')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

button_graph_frame = tk.LabelFrame(root, text='Gráficos, nodos y paths')
button_graph_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button1 = tk.Button(button_graph_frame, text='Gráfico', command=graph1)
button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button2 = tk.Button(button_graph_frame, text='Gráfico inventado', command=graph2)
button2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

button3 = tk.Button(button_graph_frame, text='Nodo', command=nodo)
button3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button4 = tk.Button(button_graph_frame, text='Path', command=path)
button4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button5 = tk.Button(button_graph_frame, text='Shortest Path', command=shortest_path)
button5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button6 = tk.Button(button_graph_frame, text='Reachable', command=reachable)
button6.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Entrada
input_frame = tk.LabelFrame(root, text='File:')
input_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
entry = tk.Entry(input_frame)
entry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
button_file = tk.Button(input_frame, text='Input', command=files)
button_file.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

picture_frame = tk.LabelFrame(root, text='Gráficos')
picture_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")

root.mainloop()