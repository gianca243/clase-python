lista = [1, 2, 3, 4]
print(*lista)

lista2 = [5, 6]

combinada = ["hola", *lista, *lista2, 3, "chanchito"]
print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevo_punto = {**punto1, "lala": "holamundo", **punto2, "z": "mundo"}
print(nuevo_punto)
