class NavAirport:
    def __init__(self, name):
        self.name = name
        self.SID = []  # Lista de NavPoints para salidas
        self.STAR = []  # Lista de NavPoints para llegadas