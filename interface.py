import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from test_graph import *
from graph import *


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



root= tk.Tk()
root.geometry('800x400')
root.title('Gráficos y nodos')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=10)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

#Columna 0, fila 0: Botones para ver los diferentes gráficos o nodos
button_graph_frame = tk.LabelFrame(root, text='Gráficos y nodos')
button_graph_frame.grid (row=0, column=0, padx=5, pady=5,
                            sticky=tk.N + tk.E + tk.W + tk.S)
button_graph_frame.rowconfigure(0,weight=1)
button_graph_frame.rowconfigure(1,weight=1)
button_graph_frame.rowconfigure(2,weight=1)
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