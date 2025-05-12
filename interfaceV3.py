import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent

from airSpace import *
from graph import *
from path import *

selected_nodes = []
G = None  # Se cargará con el espacio aéreo real

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

def draw_on_canvas(fig):
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

def load_real_airspace():
    global G
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    air = buildAirSpace("Cat")
    G = buildAirGraf(air)
    Plot(G)
    fig.canvas.mpl_connect('button_press_event', on_click)
    print("Espacio aéreo real cargado.")

def show_selected_node_neighbors():
    global selected_nodes
    if len(selected_nodes) != 1:
        print("Selecciona un único nodo haciendo clic.")
        return

    origin = selected_nodes[0]

    fig, ax = plt.subplots()
    draw_on_canvas(fig)

    for node in G.nodes:
        if node == origin:
            plt.plot(node.x, node.y, 'o', color='blue')  # origen
        elif node in origin.neighbors:
            plt.plot(node.x, node.y, 'o', color='green')  # vecinos
        else:
            plt.plot(node.x, node.y, 'o', color='gray')  # el resto
        plt.text(node.x, node.y, node.name, fontsize=9)

    for neighbor in origin.neighbors:
        plt.plot([origin.x, neighbor.x], [origin.y, neighbor.y], 'r--')
        mid_x = (origin.x + neighbor.x) / 2
        mid_y = (origin.y + neighbor.y) / 2
        dist = Distance(origin, neighbor)
        plt.text(mid_x, mid_y, f"{dist:.1f}", fontsize=8, color='red')

    plt.title(f"Vecinos de {origin.name}")
    plt.grid()
    selected_nodes.clear()

def show_shortest_path():
    global selected_nodes
    if len(selected_nodes) != 2:
        print("Selecciona exactamente 2 nodos haciendo clic.")
        return
    origin = selected_nodes[0].name
    destination = selected_nodes[1].name
    path = FindShortestPath(G, origin, destination)
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    if path:
        print("Camino encontrado:", [n.name for n in path.nodes])
        print("Coste total:", path.cost)
        PlotPath(G, path)
    else:
        print("No se encontró camino.")
    selected_nodes.clear()

def show_reachability():
    global selected_nodes
    if len(selected_nodes) != 1:
        print("Selecciona un único nodo haciendo clic.")
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
    draw_on_canvas(fig)
    for node in G.nodes:
        color = 'green' if node in visited else 'gray'
        plt.plot(node.x, node.y, 'o', color=color)
        plt.text(node.x, node.y, node.name, fontsize=8)
    plt.title(f"Nodos alcanzables desde {origin.name}")
    plt.grid()
    selected_nodes.clear()

# Interfaz gráfica
root = tk.Tk()
root.geometry('800x400')
root.title('Espacio aéreo - Versión 3')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

button_frame = tk.LabelFrame(root, text='Opciones')
button_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button1 = tk.Button(button_frame, text='Cargar espacio aéreo real', command=load_real_airspace)
button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button2 = tk.Button(button_frame, text='Vecinos del nodo', command=show_selected_node_neighbors)
button2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

button3 = tk.Button(button_frame, text='Camino más corto', command=show_shortest_path)
button3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button4 = tk.Button(button_frame, text='Alcanzables', command=show_reachability)
button4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

picture_frame = tk.LabelFrame(root, text='Gráfico')
picture_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")

root.mainloop()