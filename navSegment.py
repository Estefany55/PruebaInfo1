from math import radians, sin, cos, sqrt, atan2

class NavSegment:
    def __init__(self, orig, dest, dist):
        self.orig = orig  # NavPoint
        self.dest = dest  # NavPoint
        self.dist = float(dist)

# Función para calcular la distancia geográfica entre dos NavPoints (haversine formula)
def CalculateDistance(p1, p2):
    R = 6371.0  # Radio de la Tierra en km
    lat1 = radians(p1.lat)
    lon1 = radians(p1.lon)
    lat2 = radians(p2.lat)
    lon2 = radians(p2.lon)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c