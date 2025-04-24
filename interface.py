import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
G = Graph()


from path import *



def graph1():
    fig, ax=plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture= canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0,column=0,padx=5,pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)
    g = CreateGraph_1()
    Plot(g)

def graph2():
    fig,ax=plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                            sticky=tk.N + tk.E + tk.W + tk.S)
    k = CreateGraph_2()
    Plot(k)


#Función para manejar el clic del ratón


def on_click(event:MouseEvent):
    if event.inaxes: #verificar si el clic ocurrió dentro de la gráfica
        x,y =event.xdata, event.ydata
        n=GetClosest(G,x,y)
        print(x,y)

        if n:
            show_node_graph(n.name)


def show_node_graph(node_name):


    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()


    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()

    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)

    # Dibujar el nodo seleccionado
    print(node_name)
    PlotNode(G, node_name)

def nodo():
    global G  # Asegurar que el grafo sea accesible en toda la aplicación
    G = CreateGraph_1()

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()

    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()

    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)

    Plot(G)
    fig.canvas.mpl_connect('button_press_event',on_click)



def files():
    f = LoadGraphFromFile(entry.get())
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)
    Plot(f)

def shortest_path():
    fig,ax=plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                            sticky=tk.N + tk.E + tk.W + tk.S)
    G=CreateGraph_1()
    path = FindShortestPath(G, "A", "B")
    if path:
        print("Path found:", [n.name for n in path.nodes])
        print("Total cost:", path.cost)
        PlotPath(G, path)
    else:
        print("No path found.")

def path():
    fig,ax=plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()
    global canvas_picture
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                            sticky=tk.N + tk.E + tk.W + tk.S)

    a = PlotPath(G, p)
    print(a)


root= tk.Tk()
root.geometry('800x400')
root.title('Gráficos y nodos')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=10)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

#Columna 0, fila 0: Botones para ver los diferentes gráficos o nodos
button_graph_frame = tk.LabelFrame(root, text='Gráficos, nodos y paths')
button_graph_frame.grid (row=0, column=0, padx=5, pady=5,
                            sticky=tk.N + tk.E + tk.W + tk.S)
button_graph_frame.rowconfigure(0,weight=1)
button_graph_frame.rowconfigure(1,weight=1)
button_graph_frame.rowconfigure(2,weight=1)
button_graph_frame.rowconfigure(3,weight=1)
button_graph_frame.rowconfigure(4,weight=1)
button_graph_frame.columnconfigure(0,weight=1)

button1 = tk.Button(button_graph_frame, text='Gráfico', command=graph1)
button1.grid(row=0, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)
button2 = tk.Button(button_graph_frame, text='Gráfico inventado', command=graph2)
button2.grid(row=1, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)
button3 = tk.Button(button_graph_frame, text='Nodo', command=nodo)
button3.grid(row=2, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)

button4 = tk.Button(button_graph_frame, text='Path', command=path)
button4.grid(row=3, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)

button5 = tk.Button(button_graph_frame, text='Shortest Path', command=shortest_path)
button5.grid(row=4, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)


#Columna 0, fila 1: introducir un file para poder ver su gráfico
input_frame = tk.LabelFrame(root,text='File y su respectivo gráfico:')
input_frame.grid(row=1, column=0, padx=5, pady=5,
                 sticky=tk.N + tk.E + tk.W + tk.S)
input_frame.rowconfigure(0, weight=1)
input_frame.rowconfigure(1, weight=1)
input_frame.columnconfigure(0, weight=1)

entry = tk.Entry(input_frame)
entry.grid(row=0, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)
button4 = tk.Button(input_frame, text='Input', command=files)
button4.grid(row=1, column=0, padx=5, pady=5,
             sticky=tk.N + tk.E + tk.W + tk.S)


picture_frame = tk.LabelFrame(root, text='Gráficos')
picture_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky = "nsew")
picture_frame.rowconfigure(0, weight=1)
picture_frame.columnconfigure(0, weight=1)


root.mainloop()