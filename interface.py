import tkinter as tk
from graph import*
from tkinter import *
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from airSpace import *
from tkinter import simpledialog, filedialog
n1 = Node("A", 0, 0)
n2 = Node("B", 2, 4)
n3 = Node("C", 6, 8)

selected_nodes=[]

# Crear un camino
p = Path()
print("Path inicial:", p)


# Agregar nodos al camino
AddNodeToPath(p, n1)
AddNodeToPath(p, n2)
AddNodeToPath(p, n3)




G = Graph()
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


from graph import *
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


from path import *




def graph1():
  global G, click_mode, canvas_picture
  click_mode = "show_neighbors"
  fig, ax=plt.subplots()
  canvas = FigureCanvasTkAgg(fig, master=picture_frame)
  canvas.draw()
  if 'canvas_picture' in globals():
      canvas_picture.grid_forget()
  canvas_picture= canvas.get_tk_widget()
  canvas_picture.config(width=600, height=400)
  canvas_picture.grid(row=0,column=0,padx=5,pady=5,
                      sticky=tk.N + tk.E + tk.W + tk.S)
  G = CreateGraph_1()
  Plot(G)




def graph2():
  global G, click_mode, canvas_picture
  click_mode = "show_neighbors"
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
  G = CreateGraph_2()
  Plot(G)


#Función para manejar el clic del ratón

click_mode = None  # Puede ser "select_node", "shortest_path", etc.

def handle_click(event: MouseEvent):
    global click_mode, selected_nodes

    if not event.inaxes:
        return

    x, y = event.xdata, event.ydata
    n = GetClosest(G, x, y)
    print(f"Click en: {x:.2f}, {y:.2f}")

    if not n:
        print("No se encontró nodo cercano.")
        return

    if click_mode == "show_neighbors":
        show_node_graph(n.name)

    elif click_mode == "shortest_path":
        selected_nodes.append(n)
        print(f"Nodo seleccionado: {n.name}")

        if len(selected_nodes) == 2:
            origin = selected_nodes[0].name
            destination = selected_nodes[1].name
            path = FindShortestPath(G, origin, destination)
            if path:
                print("Camino encontrado:", [node.name for node in path.nodes])
                print("Coste total:", path.cost)
                PlotPath(G, path)  # ✅ SIN ax=
                plt.draw()
            else:
                print("No se encontró camino.")
            selected_nodes.clear()
            click_mode = "show_neighbors"


"""def on_click(event:MouseEvent):
  if event.inaxes: #verificar si el clic ocurrió dentro de la gráfica
      x,y =event.xdata, event.ydata
      n=GetClosest(G,x,y)
      print(x,y)

      if n:
          show_node_graph(n.name)"""


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
    PlotNode(G, node_name, ax=ax)

def nodo():
    global G, click_mode, canvas_picture

    # Establecer modo de clic para mostrar vecinos
    click_mode = "show_neighbors"

    # Crear el grafo de ejemplo
    G = CreateGraph_1()

    # Crear nueva figura y canvas para graficar
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()

    # Si ya había un gráfico anterior, eliminarlo del grid
    if 'canvas_picture' in globals() and canvas_picture:
        canvas_picture.grid_forget()

    # Guardar el nuevo canvas y agregarlo al layout
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)

    # Dibujar el grafo
    Plot(G)

    # Conectar el evento de clic con la función de manejo
    fig.canvas.mpl_connect('button_press_event', handle_click)

    print("Grafo de ejemplo cargado.")



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



"""def on_click2(event:MouseEvent):
    if event.inaxes:
        x, y = event.xdata, event.ydata
        n = GetClosest(G, x, y)
        print(x, y)

        if n:
            selected_nodes.append(n)
            show_shortest_path()"""

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

"""def shortest_path():
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
    fig.canvas.mpl_connect('button_press_event', on_click2)"""

def shortest_path():
    global click_mode, selected_nodes
    if not G or not G.nodes:
        print("No hay un grafo cargado.")
        return

    selected_nodes.clear()
    click_mode = "shortest_path"
    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', handle_click)
    print("Selecciona dos nodos para encontrar el camino más corto.")





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
  G = Graph()
  a = PlotPath(G, p)
  print(a)

#EXAMEN
def change_color():
    global G

    if 'G' not in globals() or not G.nodes:

        G = CreateGraph_1()

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=picture_frame)
    canvas.draw()


    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N + tk.E + tk.W + tk.S)


    if not G.nodes:
        print("No nodes in the graph")
        return

    # PUNTO MEDIO
    x_values = [node.x for node in G.nodes]
    mid_x = (max(x_values) + min(x_values)) / 2
    print(f"Midpoint x: {mid_x}")
    print(f"Number of nodes: {len(G.nodes)}")
    print(f"Number of segments: {len(G.segments)}")

    for node in G.nodes:
        plt.plot(node.x, node.y, marker='o', linestyle='', color='black', markersize=5)
        plt.text(node.x, node.y, node.name, horizontalalignment='left',
                 verticalalignment='bottom', color='red', fontsize=7)

    for segment in G.segments:
        origin_node = segment.origin_node
        dest_node = segment.destination_node

        if origin_node.x <= mid_x:
            color = 'red'  # NODOS DE LA MITAD IZQUIERDA
        else:
            color = 'blue'

        plt.plot([origin_node.x, dest_node.x],
                 [origin_node.y, dest_node.y], color=color)

        #PUNTO MEDIO
        midpoint_x = (origin_node.x + dest_node.x) / 2
        midpoint_y = (origin_node.y + dest_node.y) / 2


        plt.text(midpoint_x, midpoint_y, round(segment.cost, 2))
        plt.arrow(origin_node.x, origin_node.y,
                  dest_node.x - origin_node.x,
                  dest_node.y - origin_node.y,
                  head_width=0.4, head_length=0.4, fc=color, ec=color, length_includes_head=True)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    canvas.draw()


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
    global G,click_mode
    click_mode = "show_neighbors"
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    air = buildAirSpace("Cat")
    G = buildAirGraf(air)
    Plot(G)
    fig.canvas.mpl_connect('button_press_event', handle_click)
    print("Espacio aéreo real cargado.")

def add_node():
    global G
    """if G is None:
        print("Crea o carga primero un grafo.")
        return"""
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    air = buildAirSpace("Cat")
    G = buildAirGraf(air)
    Plot(G)

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
            fig.canvas.mpl_connect('button_press_event', handle_click)
        else:
            print(f"El nodo {name} ya existe.")

def add_segment():
    global G
    """if G is None:
        print("Crea o carga primero un grafo.")
        return"""
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    air = buildAirSpace("Cat")
    G = buildAirGraf(air)
    Plot(G)

    origin = simpledialog.askstring("Añadir segmento", "Nombre del nodo origen:")
    destination = simpledialog.askstring("Añadir segmento", "Nombre del nodo destino:")

    if origin and destination:
        name = origin + destination
        if AddSegment(G, name, origin, destination):
            print(f"Segmento {name} añadido correctamente.")
            fig, ax = plt.subplots()
            draw_on_canvas(fig)
            Plot(G)
            fig.canvas.mpl_connect('button_press_event', handle_click)
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
            fig.canvas.mpl_connect('button_press_event', handle_click)
        else:
            print(f"El nodo {name} no existe.")

def delete_segment():
    global G,click_mode
    if not G or not G.segments:
        print("Crea o carga primero un grafo con segmentos.")
        return

    name = simpledialog.askstring("Eliminar segmento", "Nombre del segmento (ej. AB):")
    if not name:
        print("No se ingresó un nombre de segmento.")
        return

    # Intentar eliminar el segmento usando la función de graph.py
    success = DeleteSegment(G, name)

    if success:
        print(f"Segmento '{name}' eliminado correctamente.")

        # Redibujar el grafo actualizado
        fig, ax = plt.subplots()
        draw_on_canvas(fig)
        Plot(G)

        # Restaurar el modo de clic
        click_mode = "show_neighbors"
        fig.canvas.mpl_connect('button_press_event', handle_click)
    else:
        print(f"El segmento '{name}' no existe o no pudo eliminarse.")


def create_empty_graph():
    global G
    G = Graph()
    fig, ax = plt.subplots()
    draw_on_canvas(fig)
    print("Nuevo grafo vacío creado.")
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
            fig.canvas.mpl_connect('button_press_event', handle_click)
        else:
            print(f"El nodo {name} ya existe.")

def save_graph_to_file():
    global G
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        G.save_to_file(file_path)
        print(f"Grafo guardado en: {file_path}")


root= tk.Tk()
root.geometry('1100x700')
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
button_graph_frame.rowconfigure(6,weight=1)
button_graph_frame.rowconfigure(7,weight=1)
button_graph_frame.rowconfigure(8,weight=1)
button_graph_frame.rowconfigure(9,weight=1)
button_graph_frame.rowconfigure(10,weight=1)
button_graph_frame.rowconfigure(11,weight=1)
button_graph_frame.rowconfigure(12,weight=1)
button_graph_frame.rowconfigure(13,weight=1)
#EXAMEN
button_graph_frame.rowconfigure(5,weight=1)
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

button7 = tk.Button(button_graph_frame, text='Real Airspace', command=load_real_airspace)
button7.grid(row=6, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button8 = tk.Button(button_graph_frame, text='Add Node', command=add_node)
button8.grid(row=7, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button9 = tk.Button(button_graph_frame, text='Add Segment', command=add_segment)
button9.grid(row=8, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button10 = tk.Button(button_graph_frame, text='Delete Node', command=delete_node)
button10.grid(row=9, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button11 = tk.Button(button_graph_frame, text='Delete Segment', command=delete_segment)
button11.grid(row=10, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button12 = tk.Button(button_graph_frame, text='Create empty graph', command=create_empty_graph)
button12.grid(row=11, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)

button13 = tk.Button(button_graph_frame, text='Save graph to file', command=save_graph_to_file)
button13.grid(row=12, column=0, padx=5, pady=5,
           sticky=tk.N + tk.E + tk.W + tk.S)


#EXAMEN
button6 = tk.Button(button_graph_frame, text='Change Color', command=change_color)
button6.grid(row=5, column=0, padx=5, pady=5,
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

