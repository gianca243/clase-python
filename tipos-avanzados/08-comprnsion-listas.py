usuarios = [
    ["chanchito", 1],
    ["monguito", 6],
    ["pulga", 5]
]
# nombres = [usuario[0] for usuario in usuarios]

# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


nombres = list(map(lambda usuario: usuario[0], usuarios))
omg = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres, omg)
