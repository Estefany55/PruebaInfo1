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
    plt.close('all')  # Cierra cualquier ventana de matplotlib anterior
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

from tkinter import simpledialog, filedialog
import os

def show_example_graph():
    global G
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    G = CreateGraph_1()
    Plot(G)
    fig.canvas.mpl_connect('button_press_event', on_click)
    print("Grafo de ejemplo cargado.")

def show_custom_graph():
    global G
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    G = CreateGraph_2()
    Plot(G)
    fig.canvas.mpl_connect('button_press_event', on_click)
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
            fig.canvas.mpl_connect('button_press_event', on_click)
            print(f"Grafo cargado desde: {file_path}")
        else:
            print("No se pudo cargar el grafo.")

def add_node():
    global G
    if G is None:
        print("Crea o carga primero un grafo.")
        return

    name = simpledialog.askstring("Añadir nodo", "Nombre del nodo:")
    x = simpledialog.askfloat("Añadir nodo", "Coordenada X:")
    y = simpledialog.askfloat("Añadir nodo", "Coordenada Y:")

    if name and x is not None and y is not None:
        new_node = Node(name, x, y)
        if AddNode(G, new_node):
            print(f"Nodo {name} añadido correctamente.")
            fig, ax = plt.subplots()
            draw_on_canvas(fig)
            Plot(G)
            fig.canvas.mpl_connect('button_press_event', on_click)
        else:
            print(f"El nodo {name} ya existe.")

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

button5 = tk.Button(button_frame, text='Grafo de ejemplo', command=show_example_graph)
button5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button6 = tk.Button(button_frame, text='Grafo inventado', command=show_custom_graph)
button6.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

button7 = tk.Button(button_frame, text='Cargar grafo desde archivo', command=load_graph_from_file)
button7.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

button8 = tk.Button(button_frame, text='Añadir nodo', command=add_node)
button8.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

button9 = tk.Button(button_frame, text='Añadir segmento', command=add_segment)
button9.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")

button10 = tk.Button(button_frame, text='Eliminar nodo', command=delete_node)
button10.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

button11 = tk.Button(button_frame, text='Eliminar segmento', command=delete_segment)
button11.grid(row=10, column=0, padx=5, pady=5, sticky="nsew")

button12 = tk.Button(button_frame, text='Nuevo grafo vacío', command=create_empty_graph)
button12.grid(row=11, column=0, padx=5, pady=5, sticky="nsew")

button13 = tk.Button(button_frame, text='Guardar grafo a archivo', command=save_graph_to_file)
button13.grid(row=12, column=0, padx=5, pady=5, sticky="nsew")

picture_frame = tk.LabelFrame(root, text='Gráfico')
picture_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")

root.mainloop()