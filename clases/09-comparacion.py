class Coordenadas:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, __value: object) -> bool:
        return self.lat == __value.lat and self.lon == __value.lon

    def __ne__(self, __value: object) -> bool:
        return self.lat != __value.lat and self.lon != __value.lon

    def __lt__(self, value: object) -> bool:
        return self.lat + self.lon < value.lat + value.lon

    def __le__(self, value: object) -> bool:
        return self.lat + self.lon <= value.lat + value.lon


coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)


print(coords, coords2)
print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)
print(coords > coords2)
