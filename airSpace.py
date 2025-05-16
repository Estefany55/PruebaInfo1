from navAirport import NavAirport
# Importa la clase NavPoint del módulo navPoint
from navPoint import NavPoint
# Importa la clase NavSegment del módulo navSegment
from navSegment import NavSegment
# Importa la función CalculateDistance del módulo navSegment
from navSegment import CalculateDistance
# Importa todo del módulo graph
from graph import*


# Clase que representa el espacio aéreo
class AirSpace:
   def __init__(self):
       self.NavPoints = []     # Lista de puntos de navegación
       self.NavSegments = []   # Lista de segmentos entre puntos
       self.NavAirports = []   # Lista de aeropuertos


# Función para agregar un punto de navegación
def addPoint(air: AirSpace, point: NavPoint):
   for i in air.NavPoints:
       if i == point:  # Si el punto ya existe, no se agrega
           print("Point already been added")
           return False


   air.NavPoints.append(point)  # Agrega el punto si no existe
   return True


# Función para agregar una SID (Standard Instrument Departure)
def addSID(air, nameAirport, nameSID):
   orig = None
   dest = None
   numDest = None
   numOrig = None
   found = False
   i = 0


   # Buscar el punto de destino SID por nombre
   while i < len(air.NavPoints) and not found:
       if air.NavPoints[i].name == nameSID:
           dest = air.NavPoints[i]
           found = True
       i = i + 1


   if found:
       numDest = dest.num  # Guarda el número del punto destino
   else:
       print("Destination not found")


   j = 0
   found2 = False


   # Buscar el aeropuerto por nombre
   while j < len(air.NavAirports) and not found2:
       if air.NavAirports[j].name == nameAirport:
           for SID in air.NavAirports[j].SID:  # Recorre las SID del aeropuerto
               orig = SID
               numOrig = SID.num
               found2 = True
       j = j + 1


   # Si se encuentran ambos puntos, se agrega el segmento
   if found2:
       addSegment(air, numOrig, numDest, distance=CalculateDistance(dest, orig))
       print("SID added correctly")
       print(f"NUM: {numOrig} and {numDest}")
   else:
       print("Failed to add SID: origin or destination not found.")


# Función para agregar una STAR (Standard Terminal Arrival Route)
def addSTAR(air, nameAirport, nameSTAR):
   orig = None
   dest = None
   numDest = None
   numOrig = None
   found = False
   i = 0


   # Buscar punto de origen STAR por nombre
   while i < len(air.NavPoints) and not found:
       if air.NavPoints[i].name == nameSTAR:
           orig = air.NavPoints[i]
           found = True
       i += 1


   if found:
       numOrig = orig.num
   else:
       print("Destination not found")


   j = 0
   found2 = False


   # Buscar aeropuerto por nombre
   while j < len(air.NavAirports) and not found2:
       if air.NavAirports[j].name == nameAirport:
           for STAR in air.NavAirports[j].STAR:
               dest = STAR
               numDest = STAR.num
               found2 = True
       j += 1


   if found2:
       addSegment(air, numOrig, numDest, distance=CalculateDistance(dest, orig))
       print("STAR added correctly")
       print(f"NUM: {numOrig} and {numDest}")
   else:
       print("Failed to add STAR: origin or destination not found.")


# Agrega un segmento entre dos puntos si ambos existen
def addSegment(air: AirSpace, numOrig, numDst, distance):
   orig = None
   dest = None
   for point in air.NavPoints:
       if point.num == numOrig:
           orig = point
   for point in air.NavPoints:
       if point.num == numDst:
           dest = point
   if orig is None or dest is None:
       print("One or both of the points specified in the segment do not exist.")
       return False
   new_segment = NavSegment(orig, dest, distance)
   if new_segment in air.NavSegments:
       print("Segment already exists.")
       return False


   air.NavSegments.append(new_segment)
   return True


# Agrega un aeropuerto si no existe aún
def addAirport(air: AirSpace, name):
   SID_NavPoints = []
   STAR_NavPoints = []
   for existing_airport in air.NavAirports:
       if existing_airport.name.lower() == name.lower():
           print("The airport already exists.")
           return False
   new_airport = NavAirport(name)


   # Asocia puntos SID y STAR (aunque aquí no hay lógica de llenado)
   for point in SID_NavPoints:
       new_airport.SID.append(point)
   for point in STAR_NavPoints:
       new_airport.STAR.append(point)


   air.NavAirports.append(new_airport)
   return True


# Carga puntos de navegación desde archivo
def loadNavPoints(air: AirSpace, filename):
   try:
       F = open(filename, 'r')
   except FileNotFoundError:
       print(f"File {filename} not found")
       return False
   line = F.readline()
   num_lines = 0
   while line != "":
       line = line.rstrip()
       elements = line.split()
       if len(elements) == 4:
           point = NavPoint(elements[0], elements[1], elements[2], elements[3])
           addPoint(air, point)
       else:
           print(f"The format of the file is not correct at line {num_lines + 1}")
       num_lines += 1
       line = F.readline().rstrip()
   F.close()


# Carga segmentos desde archivo
def loadSegments(air, filename):
   try:
       F = open(filename, 'r')
   except FileNotFoundError:
       print(f"File {filename} not found")
       return False
   line = F.readline()
   num_lines = 0
   while line != "":
       line = line.rstrip()
       elements = line.split()
       if len(elements) == 3:
           addSegment(air, float(elements[0]), float(elements[1]), float(elements[2]))
       else:
           print(f"The format of the file is not correct at line {num_lines + 1}")
       num_lines += 1
       line = F.readline()
   F.close()


# Carga aeropuertos con sus SID y STAR desde archivo
def loadAirports(air, filename):
   try:
       F = open(filename, 'r')
   except FileNotFoundError:
       print(f"File {filename} not found")
       return False
   lines = F.readlines()
   line_number = 0
   total_lines = len(lines)


   if total_lines % 3 == 0:
       for line in lines:
           if line_number % 3 == 0:
               name = line.strip()
           elif line_number % 3 == 1:
               SID_name = line.strip()
           elif line_number % 3 == 2:
               STAR_name = line.strip()
               SID = None
               STAR = None
               for point in air.NavPoints:
                   if point.name == SID_name:
                       SID = point
                   elif point.name == STAR_name:
                       STAR = point
                   if SID and STAR:
                       new_airport = NavAirport(name)
                       new_airport.SID.append(SID)
                       new_airport.STAR.append(STAR)
                       air.NavAirports.append(new_airport)
                       break
               else:
                   print(f"SID or STAR not found in NavPoints at line {line_number + 1}")
           line_number += 1
       F.close()
   else:
       print("The format of the file is not correct")


# Construye todo el espacio aéreo a partir de archivos
def buildAirSpace(filename):
   nav_file = filename + '_nav.txt'
   seg_file = filename + '_seg.txt'
   aer_file = filename + '_aer.txt'
   air = AirSpace()
   loadNavPoints(air, nav_file)
   loadAirports(air, aer_file)
   loadSegments(air, seg_file)
   return air


# Busca un nodo por nombre
def find_node_by_name(nodes, name):
   for node in nodes:
       if node.name == name:
           return node
   return None


# Construye el grafo a partir del espacio aéreo
def buildAirGraf(air):
   G = Graph()


   # Agrega nodos del grafo desde los puntos de navegación
   for point in air.NavPoints:
       node = Node(point.name, point.lon, point.lat)
       G.nodes.append(node)


   # Agrega nodos y segmentos para SID y STAR
   for airport in air.NavAirports:
       for SID in airport.SID:
           airport_node = Node(airport.name, SID.lon, SID.lat)
           G.nodes.append(airport_node)
           for nodes in G.nodes:
               if nodes.name == SID.name:
                   origin_node = find_node_by_name(G.nodes, SID.name)
                   newseg = Segment(airport_node, origin_node)
                   newseg.cost = Distance(airport_node, origin_node)
                   G.segments.append(newseg)
                   airport_node.neighbors.append(origin_node)


       for STAR in airport.STAR:
           airport_node = Node(airport.name, STAR.lon, STAR.lat)
           G.nodes.append(airport_node)
           for nodes1 in G.nodes:
               if nodes1.name == STAR.name:
                   origin_node = find_node_by_name(G.nodes, STAR.name)
                   newseg1 = Segment(origin_node, airport_node)
                   newseg1.cost = Distance(origin_node, airport_node)
                   G.segments.append(newseg1)
                   origin_node.neighbors.append(airport_node)


   # Agrega los segmentos de navegación generales
   for navsegment in air.NavSegments:
       orig_node = find_node_by_name(G.nodes, navsegment.orig.name)
       dest_node = find_node_by_name(G.nodes, navsegment.dest.name)
       if orig_node and dest_node:
           segment = Segment(orig_node, dest_node)
           segment.cost = navsegment.dist
           G.segments.append(segment)
           orig_node.neighbors.append(dest_node)
       else:
           print(f"Warning: Node not found for segment {navsegment.orig.name} -> {navsegment.dest.name}")


   return G
