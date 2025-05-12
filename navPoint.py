class NavPoint:
    def __init__(self, num, name, lat, lon):
        self.num = int(num)
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __eq__(self, other):
        if isinstance(other, NavPoint):
            return self.num == other.num
        return False